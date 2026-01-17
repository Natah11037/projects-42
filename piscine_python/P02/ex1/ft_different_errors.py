#!usr/bin/env python3


def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        int("ablabla")
    except ValueError:
        print("Caught ValueError📋: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        11037 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError0️⃣ : division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open("mamereenslip.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError📂: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        test: dict[str] = {"denouveaumamereenslip": 34364667}
        print(test["denouveaumamereenslip2.0"])
    except KeyError:
        print("Caught KeyError🗝️ : 'missing\_plant'\n")
    print("Testing multiple errors together...")
    try:
        int("ablabla")
        11037 / 0
        open("mamereenslip.txt")
        test: dict[str] = {"denouveaumamereenslip": 34364667}
        print(test["denouveaumamereenslip2.0"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    garden_operations()
