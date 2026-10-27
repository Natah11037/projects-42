from pydantic import BaseModel

from llm_sdk.llm_sdk import Small_LLM_Model
from parser import Function


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
