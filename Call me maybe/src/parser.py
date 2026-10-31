import json
from typing import Any
from pydantic import BaseModel, ConfigDict, Field


class Type(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Function(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    parameters: dict[str, Type]
    returns: Type


class Prompt(BaseModel):
    model_config = ConfigDict(extra="forbid")
    prompt: str = Field(min_length=1)


class FunctionCall(BaseModel):
    model_config = ConfigDict(extra="forbid")
    prompt: str
    name: str
    parameters: dict[str, Any]


class Loading(BaseModel):
    model_config = ConfigDict(extra="forbid")

    def load(self, file_path: str) -> list[dict[str, Any]]:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as error:
                raise json.JSONDecodeError(f"Invalid JSON: {file_path}",
                                           doc=error.doc, pos=error.pos)

        return data

    def load_prompts(self, file_path: str) -> list[Prompt]:
        data = self.load(file_path)
        prompts = [Prompt(**item) for item in data]
        return prompts

    def load_functions(self, file_path: str) -> list[Function]:
        data = self.load(file_path)
        functions = [Function(**item) for item in data]
        return functions
