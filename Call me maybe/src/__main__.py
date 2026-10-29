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
    answer = {}
    for prompt in prompts:
        context = builder.build_function_selection_context(prompt)
        function = selector.choose_id(context, model)
        context_arg = builder.build_argument_context(prompt, function)
        args = argument_selector.choose_argument(model, context_arg)
        answer[function.name] = function.name
        answer["parameter"] = args
        print(f"Prompt: {prompt.prompt}\nfunction: "
              f"{answer[function.name]}\nparameter: {answer['parameter']}")


if __name__ == "__main__":
    main()
