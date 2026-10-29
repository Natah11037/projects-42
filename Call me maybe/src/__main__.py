from src.selector import Function_selector, Argument_selector
from src.parser import loading
from src.context_builder import ContextBuilder
from llm_sdk.llm_sdk import Small_LLM_Model


def main() -> None:
    loader = loading()

    prompts = loader.load_prompts(
        "data/input/function_calling_tests.json"
    )
    # print(prompts, end="\n\n\n")
    functions = loader.load_functions(
        "data/input/functions_definition.json"
    )
    # print(functions, end="\n\n\n")
    selector = Function_selector(function_list=functions)
    model = Small_LLM_Model()
    builder = ContextBuilder(functions=functions)
    argument_selector = Argument_selector()
    choices_functions = []
    answer = {}
    for prompt in prompts:
        context = builder.build_function_selection_context(prompt)
        choices_functions.append(selector.choose_id(context, model))

        for function in choices_functions:
            context_arg = builder.build_argument_context(prompt, function)
            args = argument_selector.choose_argument(model, context_arg)
            answer[function.name] = function
            answer["parameter"] = args
        print("function: "
              f"{answer[function.name]}/n parameter: {answer['parameter']}")


if __name__ == "__main__":
    main()
