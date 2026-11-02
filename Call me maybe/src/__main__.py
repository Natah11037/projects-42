import argparse
import json
import sys
from pathlib import Path

from pydantic import ValidationError

from src.context_builder import ContextBuilder
from src.parser import FunctionCall, InputFileError, Loading
from src.selector import ArgumentSelector, FunctionSelector


def main() -> int:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--functions_definition", type=Path, default=Path(
        "data/input/functions_definition.json"))
    argparser.add_argument("--input", type=Path, default=Path(
        "data/input/function_calling_tests.json"))
    argparser.add_argument("--output", type=Path, default=Path(
        "data/output/function_calls.json"))
    arguments = argparser.parse_args()
    loader = Loading()

    try:
        prompts = loader.load_prompts(str(arguments.input))
        functions = loader.load_functions(str(arguments.functions_definition))
    except InputFileError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    if prompts and not functions:
        print(
            "Error: prompts were provided, but the function definition "
            "list is empty.",
            file=sys.stderr,
        )
        return 1

    output = []
    if prompts:
        try:
            from llm_sdk.llm_sdk import Small_LLM_Model

            selector = FunctionSelector(function_list=functions)
            model = Small_LLM_Model()
            builder = ContextBuilder(functions=functions)
            argument_selector = ArgumentSelector()
            answers = []
            for prompt in prompts:
                context = builder.build_function_selection_context(prompt)
                function = selector.choose_id(context, model)
                context_arg = builder.build_argument_context(prompt, function)
                parameters = argument_selector.choose_argument(
                    model, context_arg, function
                )
                answers.append(
                    FunctionCall(
                        prompt=prompt.prompt,
                        name=function.name,
                        parameters=parameters,
                    )
                )
            output = [
                answer.model_dump(mode="json") for answer in answers
            ]
        except (ImportError, OSError, RuntimeError, ValueError, KeyError,
                IndexError) as error:
            print(f"Error while processing prompts: {error}", file=sys.stderr)
            return 1
        except ValidationError as error:
            print(f"Error in generated function call: {error}",
                  file=sys.stderr)
            return 1

    try:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        with arguments.output.open("w", encoding="utf-8") as file:
            json.dump(output, file, indent=4, allow_nan=False)
            file.write("\n")
    except (OSError, TypeError, ValueError) as error:
        print(
            f"Error: cannot write output file '{arguments.output}': {error}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
