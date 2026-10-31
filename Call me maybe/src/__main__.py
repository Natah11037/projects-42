from src.selector import FunctionSelector, ArgumentSelector
from src.parser import FunctionCall, Loading
from src.context_builder import ContextBuilder
from llm_sdk.llm_sdk import Small_LLM_Model
import argparse
from pathlib import Path
import json


def main() -> None:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--functions_definition", type=Path, default=Path(
        "data/input/functions_definition.json"))
    argparser.add_argument("--input", type=Path, default=Path(
        "data/input/function_calling_tests.json"))
    argparser.add_argument("--output", type=Path, default=Path(
        "data/output/function_calls.json"))
    arguments = argparser.parse_args()
    loader = Loading()

    prompts = loader.load_prompts(str(arguments.input))
    functions = loader.load_functions(str(arguments.functions_definition))
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
            FunctionCall(prompt=prompt.prompt, name=function.name,
                         parameters=parameters)
        )
    output = [answer.model_dump(mode='json') for answer in answers]

    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open("w", encoding="utf-8") as file:
        json.dump(output, file, indent=4, allow_nan=False)


if __name__ == "__main__":
    main()
