import importlib


def check_depedencies():
    dep_list = ["numpy", "pandas", "matplotlib", "requests"]
    for dep in dep_list:
        try:
            module = importlib.import_module(dep)
            print(f"[OK] {dep} ({module.__version__}) - is installed.")
        except ImportError:
            print(f"[KO] {dep} is not installed.\n"
                  "To install it, run the following command:\n"
                  f"pip install {dep}\n"
                  "or\n"
                  f"poetry add {dep}\n")


def main():
    check_depedencies()


if __name__ == "__main__":
    main()
