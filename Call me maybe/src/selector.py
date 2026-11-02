from __future__ import annotations

import json
from typing import Any, Callable, TYPE_CHECKING
import math
from pydantic import BaseModel
from pathlib import Path
from src.parser import Function
import heapq

if TYPE_CHECKING:
    from llm_sdk.llm_sdk import Small_LLM_Model


class FunctionSelector(BaseModel):
    function_list: list[Function]

    def encode_context(
        self, context: str, model: Small_LLM_Model
    ) -> list[int]:
        return model.encode(context)[0].tolist()

    def encode_functions_name(
        self, model: Small_LLM_Model
    ) -> list[list[int]]:
        return [
            model.encode(
                function.name + "\n"
            )[0].tolist()
            for function in self.function_list
        ]

    def choose_id(self, context: str, model: Small_LLM_Model) -> Function:
        context_ids = self.encode_context(context, model)
        functions_ids = self.encode_functions_name(model)
        good_ids: list[int] = []

        if not functions_ids:
            raise ValueError("Function list is empty.")
        active_functions = list(range(len(functions_ids)))

        while active_functions:
            position = len(good_ids)
            good_tokens = {
                functions_ids[index][position]
                for index in active_functions
                if position < len(functions_ids[index])
            }
            if not good_tokens:
                break

            if len(good_tokens) == 1:
                next_token_id = next(iter(good_tokens))

            else:
                logits = model.get_logits_from_input_ids(
                    context_ids + good_ids)
                next_token_id = max(good_tokens,
                                    key=lambda token_id: logits[token_id])

            good_ids.append(next_token_id)
            active_functions = [
                index for index in active_functions
                if position < len(functions_ids[index])
                and functions_ids[index][position] == next_token_id
            ]

            for index in active_functions:
                if good_ids == functions_ids[index]:
                    return self.function_list[index]

        raise RuntimeError("Unable to select "
                           "a function from the available names")


class ArgumentSelector(BaseModel):

    def __vocabulary_ids(self, path: str) -> tuple[int, ...]:
        try:
            with Path(path).open(encoding="utf-8") as file:
                vocabulary = json.load(file)
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError(f"Cannot read vocabulary: {path}") from error
        if not isinstance(vocabulary, dict):
            raise ValueError("Vocabulary must be a JSON object")
        ids = {
            value for value in vocabulary.values()
            if type(value) is int and value >= 0
        }
        if not ids:
            raise ValueError("Vocabulary has no valid token IDs")
        return tuple(sorted(ids))

    def __string_status(self,
                        model: Small_LLM_Model,
                        potential_answer: list[int],
                        is_integer: bool = False) -> int:
        str_potential_answer = model.decode(potential_answer)
        for i, char in enumerate(str_potential_answer):
            if i == 0:
                if char != '"':
                    return -2
                else:
                    continue
            else:
                if char == '"' and str_potential_answer[i - 1] != '\\':
                    return 0
                else:
                    continue
        return -1

    def __string(self,
                 model: Small_LLM_Model,
                 context_ids: list[int],
                 is_integer: bool = False) -> str:
        answer: list[int] = model.encode('"')[0].tolist()
        allowed_ids = self.__vocabulary_ids(
            model.get_path_to_vocab_file()
        )
        for _ in range(256):
            logits = model.get_logits_from_input_ids(
                context_ids + answer
            )
            candidates = [
                (-logits[token_id], token_id)
                for token_id in allowed_ids
                if token_id < len(logits)
                and math.isfinite(logits[token_id])
            ]
            heapq.heapify(candidates)
            while candidates:
                _, next_token_id = heapq.heappop(candidates)
                potential_answer = answer + [next_token_id]
                status = self.__string_status(model, potential_answer,
                                              is_integer)
                if status in (-1, 0):
                    answer = potential_answer
                    break
            str_answer = model.decode(answer)
            if status == 0:
                while str_answer[-1] != '"':
                    str_answer = str_answer[:-1]
                break
        try:
            return json.loads(str_answer)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"Generated string is not valid JSON: {str_answer!r}"
            ) from error

    def __number_and_integer_status(self,
                                    model: Small_LLM_Model,
                                    potential_answer: list[int],
                                    is_integer: bool) -> int:
        str_potential_answer = model.decode(potential_answer)
        if is_integer:
            if "." in str_potential_answer:
                return -2
        for i, char in enumerate(str_potential_answer):
            if i == len(potential_answer) - 1 and char not in ",\n":
                return -1
            if char.isdigit():
                continue
            else:
                if char == "-":
                    if i == 0:
                        continue
                    else:
                        return -2
                elif char == ".":
                    if str_potential_answer.count(".") > 1 or i == 0:
                        return -2
                    else:
                        continue
                elif char == ",":
                    if i == len(potential_answer) - 1:
                        break
                    else:
                        return -2
                elif char == "}":
                    continue
                elif char == "\n":
                    if i == len(potential_answer) - 1:
                        break
                    else:
                        return -2
                else:
                    return -2
        return 0

    def __number(self,
                 model: Small_LLM_Model,
                 context_ids: list[int],
                 is_integer: bool) -> int | float:
        answer: list[int] = []
        allowed_ids = self.__vocabulary_ids(
            model.get_path_to_vocab_file()
        )
        for _ in range(256):
            logits = model.get_logits_from_input_ids(
                context_ids + answer
            )
            candidates = [
                (-logits[token_id], token_id)
                for token_id in allowed_ids
                if token_id < len(logits)
                and math.isfinite(logits[token_id])
            ]
            heapq.heapify(candidates)
            while candidates:
                _, next_token_id = heapq.heappop(candidates)
                potential_answer = answer + [next_token_id]
                if self.__number_and_integer_status(model,
                                                    potential_answer,
                                                    is_integer) in (-1, 0):
                    answer = potential_answer
                    break
            if answer != [] and model.decode(answer)[-1] in ',}\n':
                str_answer = model.decode(answer)
                if "," in str_answer:
                    str_answer = str_answer[:-1]
                else:
                    str_answer = str_answer[:-3]
                break
        else:
            raise RuntimeError("Could not complete number argument generation")
        if is_integer:
            return int(str_answer)
        return float(str_answer)

    def __boolean_status(
        self,
        model: Small_LLM_Model,
        potential_answer: list[int],
        is_integer: bool = False,
    ) -> int:
        str_potential_answer = model.decode(potential_answer).lower()
        if str_potential_answer.startswith("t"):
            if str_potential_answer in "true":
                return 0 if str_potential_answer == "true" else -1
        elif str_potential_answer.startswith("f"):
            if str_potential_answer in "false":
                return 0 if str_potential_answer == "false" else -1
        else:
            return -2
        return -2

    def __boolean(self,
                  model: Small_LLM_Model,
                  context_ids: list[int],
                  is_integer: bool = False) -> bool:
        answer: list[int] = []
        allowed_ids = self.__vocabulary_ids(
            model.get_path_to_vocab_file()
            )
        for _ in range(256):
            logits = model.get_logits_from_input_ids(
                context_ids + answer
            )
            candidates = [
                (-logits[token_id], token_id)
                for token_id in allowed_ids
                if token_id < len(logits)
                and math.isfinite(logits[token_id])
            ]
            heapq.heapify(candidates)
            while candidates:
                _, next_token_id = heapq.heappop(candidates)
                potential_answer = answer + [next_token_id]
                if self.__boolean_status(
                        model, potential_answer, is_integer) in (-1, 0):
                    answer = potential_answer
                    break
            if model.decode(answer) in ("true", "false"):
                return model.decode(answer) == "true"
        raise RuntimeError("Could not complete boolean argument generation")

    def choose_argument(
        self,
        model: Small_LLM_Model,
        context: str,
        function: Function
    ) -> dict[str, Any]:
        context_ids = model.encode(context)[0].tolist()
        constrained_funcs: dict[
            str,
            Callable[
                [Small_LLM_Model, list[int], bool],
                str | int | float | bool,
            ],
        ] = {
            "boolean": self.__boolean,
            "integer": self.__number,
            "number": self.__number,
            "string": self.__string
        }
        parameters: dict[str, Any] = {}
        for param_key, param_type in function.parameters.items():
            parameters[param_key] = 0
            str_dict = json.dumps(parameters)
            str_dict = str_dict[:-2]
            parameters[param_key] = constrained_funcs[param_type.type](
                model, context_ids + model.encode(str_dict)[0].tolist(),
                param_type.type == "integer"
            )
        return parameters
