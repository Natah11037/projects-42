import importlib
from importlib.metadata import PackageNotFoundError, metadata
import re
import sys
import tomllib


def check_depedencies():
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        dependencies = data["project"].get("dependencies", [])
    except FileNotFoundError:
        return "Error: file pyproject.toml was not found"

    for d in dependencies:
        package_name: str = re.split(r"[><=!;\s\[]", d)[0].strip()
        try:
            meta = metadata(package_name)
            print(f"\r    [OK] {meta['Name']} {meta['Version']} - found")
        except PackageNotFoundError:
            print(f"\r     [KO] package {package_name} "
                  "was not found\n\n"
                  "=======================================\n"
                  "Install it with:\n"
                  "pip install -r requirements.txt\n"
                  "or\n"
                  "poetry install\n"
                  "=======================================\n")
            continue


def main():
    print()
    check_depedencies()
    print()


if __name__ == "__main__":
    main()
