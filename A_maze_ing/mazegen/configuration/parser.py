from pathlib import Path
from pydantic import Field, model_validator, ValidationError
try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ModuleNotFoundError:
    print("\nError: pydantic_settings module not found."
          " Please install it with 'make install'.\n"
          "If you have already installed it, make sure you are running"
          " the script in the correct environment.\n"
          "You can use make run to run the script in a venv\n")
    exit(1)
from typing import Annotated
import random
import sys


# Using Annotated allows the program to make
# a validation condition for each int in the tuple
PositiveInt = Annotated[int, Field(ge=0)]


# Searching with the class 'Path' the file 'config.txt' in the current
# directory and in the previous directory which is actually
# the root from our project
if len(sys.argv) < 2:
    raise FileNotFoundError("Error: Try something like: python3 a_maze_ing.py"
                            " <config_file.txt>")
if ".txt" not in sys.argv[1]:
    raise FileNotFoundError("Error: Try something like: python3 a_maze_ing.py"
                            " <config_file.txt>")
env_file_path = Path.cwd() / sys.argv[1]
if not env_file_path.exists():
    env_file_path = Path(sys.argv[0]).parent / sys.argv[1]
if not env_file_path.exists():
    env_file_path = Path(__file__).parent / sys.argv[1]
if not env_file_path.exists():
    env_file_path = Path(__file__).parent.parent / sys.argv[1]
if not env_file_path.exists():
    raise FileNotFoundError(f"Error: {sys.argv[1]} was not found")
try:
    with env_file_path.open():
        pass
except PermissionError:
    print(f"Error: Permission denied to read {sys.argv[1]}")
    exit(1)


# Valid_Config is a BaseSettings class which search in the root or in
# the configuration directory a file named 'config.txt'
# it takes the value for each key from this file and if there
# is not the key in the file
# it takes a default value
# BaseConfigs ignore the lines beginning with a '#' and is case insensitive
# so it don't care about upper or lower case
class Valid_Config(BaseSettings):
    """Validated maze configuration loaded from a .txt env file.

    Reads width, height, entry, exit, output_file, and perfect from the
    file passed as the first CLI argument. Coordinates are parsed from
    comma-separated strings and validated against the grid bounds.
    """
    # Checking the model at the start and each time you modify a value
    # Check in 'config.txt' and take the value from the key
    model_config = SettingsConfigDict(
        validate_assignment=True,
        env_file=env_file_path,
    )

    # validate the value 'width' only if it is equal or superior to 4
    # or equal or inferior to 150
    # put 4 by default
    width: int = Field(ge=4, default=4, le=127)
    # validate the value 'height' only if it is equal or superior to 4
    # or equal or inferior to 127
    # put 4 by default
    height: int = Field(ge=4, default=4, le=150)
    # validate the value 'entry' only if it is a pair of positive int
    # equal or superior to 4, put 4 by default
    # or equal or inferior to 127,150
    entry: str | tuple[PositiveInt, PositiveInt]
    # validate the value 'exit' only if it is a pair of positive int
    # equal or superior to 4, put 4 by default
    # or equal or inferior to 127,150
    exit: str | tuple[PositiveInt, PositiveInt]

    # the model_validator is transforming the format 'entry=1, 3' in
    # a tuple like '(1, 3)'
    # this also verify if the coordinates x and y are in the maze
    # (between 0 and height for x and between 0 and width for y)
    # finally this is verifying if the coordinates of exit and entry
    # are the same and
    # if the user give the good amount of values (a x and a y)
    @model_validator(mode="after")
    def parse_entry_exit(self) -> "Valid_Config":
        """Parse and validate entry/exit coordinate strings.

        Converts comma-separated strings (e.g. '1,3') to (int, int) tuples,
        checks that both coordinates lie within the grid, and ensures entry
        and exit are not the same cell.

        Returns:
            The updated model instance.

        Raises:
            ValueError: If coordinates are malformed, out of bounds, or equal.
        """
        if isinstance(self.entry, str):
            values = [v.strip() for v in self.entry.split(",")]
            if len(values) != 2:
                raise ValueError("Entry coordinates must contain exactly two "
                                 "non-negative integers")
            try:
                x = int(values[0])
                y = int(values[1])
            except ValueError:
                raise ValueError("Entry coordinates must be two non-negative"
                                 " integers")
            if x < self.width and y < self.height:
                self.entry = (x, y)
            else:
                raise ValueError("Entry coordinates must be in the maze")
        if isinstance(self.exit, str):
            values = [v.strip() for v in self.exit.split(",")]
            if len(values) != 2:
                raise ValueError("Exit coordinates must contain exactly two "
                                 "non-negative integers")
            try:
                x = int(values[0])
                y = int(values[1])
            except ValueError:
                raise ValueError("Exit coordinates must be two non-negative"
                                 " integers")
            if x < self.width and y < self.height:
                self.exit = (x, y)
            else:
                raise ValueError("Exit coordinates must be in the maze")
        if self.entry == self.exit:
            raise ValueError("Entry and Exit coordinates cannot be at the "
                             "same position")
        return self

    # validate the value 'output_file' only if the file name contain the
    # string '.txt' in it
    output_file: str = Field(pattern=r"^[^/\\]+\.txt$")

    @model_validator(mode="after")
    def file_exist(self) -> "Valid_Config":
        """Ensure the output file exists, creating it if necessary.

        Looks for the file relative to the configuration directory first,
        then falls back to the project root.

        Returns:
            The updated model instance.
        """
        file = Path(__file__).parent / self.output_file
        if not file.exists():
            file = Path(__file__).parent.parent / self.output_file
        file.touch(exist_ok=True)
        return self

    # put the 'perfect' value to 'True' by default
    perfect: bool = Field(default=True)
    seed: int = Field(default=random.randint(0, 99999))


if __name__ == "__main__":
    try:
        config = Valid_Config()
        print("Config loaded successfully:")
        print(f"  width       = {config.width}")
        print(f"  height      = {config.height}")
        print(f"  entry       = {config.entry}")
        print(f"  exit        = {config.exit}")
        print(f"  output_file = {config.output_file}")
        print(f"  perfect     = {config.perfect}")
        print(f"  seed        = {config.seed}")
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
