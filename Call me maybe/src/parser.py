import json
from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, ValidationError


class InputFileError(ValueError):
    """Raised when an input file cannot be "
    read or does not match its schema."""


class Type(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["string", "number", "integer", "boolean"]


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
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as error:
            raise InputFileError(
                f"Invalid JSON in '{file_path}' at line {error.lineno}, "
                f"column {error.colno}."
            ) from error
        except (OSError, UnicodeError) as error:
            raise InputFileError(
                f"Cannot read input file '{file_path}': {error}"
            ) from error

        if not isinstance(data, list):
            raise InputFileError(
                f"Expected a JSON array in '{file_path}', "
                f"got {type(data).__name__}."
            )
        for index, item in enumerate(data):
            if not isinstance(item, dict):
                raise InputFileError(
                    f"Expected an object at index {index} in '{file_path}'."
                )

        return data

    def load_prompts(self, file_path: str) -> list[Prompt]:
        data = self.load(file_path)
        try:
            return [Prompt(**item) for item in data]
        except ValidationError as error:
            raise InputFileError(
                f"Invalid prompt definition in '{file_path}': {error}"
            ) from error

    def load_functions(self, file_path: str) -> list[Function]:
        data = self.load(file_path)
        try:
            return [Function(**item) for item in data]
        except ValidationError as error:
            raise InputFileError(
                f"Invalid function definition in '{file_path}': {error}"
            ) from error
