from src.function_selector import Function_selector
from src.parser import loading


def main() -> None:
    loader = loading()

    prompts = loader.load_prompts(
        "data/input/function_calling_tests.json"
    )
    functions = loader.load_functions(
        "data/input/functions_definition.json"
    )
    selector = Function_selector(function_list=functions)


if __name__ == "__main__":
    main()
