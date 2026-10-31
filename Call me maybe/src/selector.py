import json
from typing import Any
import math
from pydantic import BaseModel
from pathlib import Path
from llm_sdk.llm_sdk import Small_LLM_Model
from src.parser import Function
import heapq


class FunctionSelector(BaseModel):
    function_list: list[Function]

    def encode_context(self, context: str, model: Small_LLM_Model):
        return model.encode(context)[0].tolist()

    def encode_functions_name(self, model: Small_LLM_Model):
        return [
            model.encode(
                function.name + "\n"
            )[0].tolist()
            for function in self.function_list
        ]

    def choose_id(self, context, model: Small_LLM_Model) -> Function:
        context_ids = self.encode_context(context, model)
        functions_ids = self.encode_functions_name(model)
        good_ids = []
        good_tokens = []

        while (True):
            position = len(good_ids)
            for function_id in functions_ids:
                if position >= len(function_id):
                    continue
                good_tokens.append(function_id[position])
            logits = model.get_logits_from_input_ids(context_ids + good_ids)
            next_token_id = max(good_tokens,
                                key=lambda token_id: logits[token_id])
            good_ids.append(next_token_id)

            if any(good_ids == function_ids for function_ids in functions_ids):
                good_ids_deco = model.decode(good_ids).removesuffix("\n")
                for function in self.function_list:
                    if good_ids_deco == function.name:
                        return function


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

    def __string(self,
                 model: Small_LLM_Model,
                 context_ids: list[int],
                 is_integer: bool = False) -> str:
        ...

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
                 is_integer: bool) -> float:
        answer = []
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
                if self.__number_and_integer_status(model, potential_answer, is_integer) in (-1, 0):
                    answer = potential_answer
                    break
            if answer != [] and model.decode(answer)[-1] in ',}\n':
                str_answer = model.decode(answer)
                if "," in str_answer:
                    str_answer = str_answer[:-1]
                else:
                    str_answer = str_answer[:-3]
                break
        if is_integer:
            return int(str_answer)
        else:
            return float(str_answer)

    def __boolean_status(self,
                         model: Small_LLM_Model,
                         potential_answer: list[int],
                         is_integer: bool = False) -> bool:
        str_potential_answer = model.decode(potential_answer).lower()
        if str_potential_answer.startswith("t"):
            if str_potential_answer in "true":
                return 0 if str_potential_answer == "true" else -1
        elif str_potential_answer.startswith("f"):
            if str_potential_answer in "false":
                return 0 if str_potential_answer == "false" else -1
        else:
            return -2

    def __boolean(self,
                  model: Small_LLM_Model,
                  context_ids: list[int],
                  is_integer: bool = False) -> bool:
        answer = []
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
                if self.__boolean_status(model, potential_answer, is_integer) in (-1, 0):
                    answer = potential_answer
                    break
            if model.decode(answer) in ("true", "false"):
                str_answer = model.decode(answer)
                break
        return str_answer.lower() == "true"

    def choose_argument(
        self,
        model: Small_LLM_Model,
        context: str,
        function: Function
    ) -> dict[str, Any]:
        context_ids = model.encode(context)[0].tolist()
        constrained_funcs = {
            "boolean": self.__boolean,
            "integer": self.__number,
            "number": self.__number,
            "string": self.__string
        }
        parameters = {}
        for param_key, param_type in function.parameters.items():
            parameters[param_key] = 0
            str_dict = json.dumps(parameters)
            str_dict = str_dict[:-2]
            parameters[param_key] = constrained_funcs[param_type.type](
                model, context_ids + model.encode(str_dict)[0].tolist(),
                param_type.type == "integer"
            )
        return parameters
