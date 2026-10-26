import json
from json.decoder import JSONDecodeError
from typing import Any

from pydantic.v1 import BaseModel


class Type(BaseModel):
    type: str


class Function(BaseModel):
    name: str
    description: str
    parameters: dict[str, Type]
    returns: Type


class Prompt(BaseModel):
    prompt: str


class Function_call(BaseModel):
    name: str
    parameterss: dict[str, Type]


class loading(BaseModel):
    def load(self, file_path: str) -> dict[str, Any]:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                raise json.JSONDecodeError(f"Invalid JSON: {file_path}",
                                           doc=error.doc, pos=error.pos)

        return data
