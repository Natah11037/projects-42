import sys
import os
import site


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        venv_name = os.path.basename(sys.prefix)
    else:
        venv_name = "None detected"
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}\n")

        print("WARNING: You're in the global environment! \n"
              "The machines can see everything you install.\n")

        print("To enter the construct, run: \n"
              "python -m venv matrix_env \n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n")

        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment! \n"
              "Safe to install packages without affecting "
              "the global system.\n")

        print(f"Package installation path:\n"
              f"{site.getsitepackages()[0]}")
