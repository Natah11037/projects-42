from pydantic import BaseModel

from llm_sdk.llm_sdk import Small_LLM_Model
from src.parser import Function


class Function_selector(BaseModel):
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


class Argument_selector(BaseModel):

    def choose_argument(self, model: Small_LLM_Model, context: str):
        good_args = []
        context_ids = model.encode(context)[0].tolist()

        for _ in range(256):
            logits = model.get_logits_from_input_ids(context_ids + good_args)
            next_token_id = max(
                range(len(logits)), key=lambda token_id: logits[token_id])
            good_args.append(next_token_id)
            if "}" in model.decode(next_token_id):
                break
        return (model.decode(good_args))
