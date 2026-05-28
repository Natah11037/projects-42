try:
    from mazegen.configuration import Valid_Config
except FileNotFoundError as e:
    print(e)
    exit(1)
from pydantic import ValidationError
from mazegen.maze_generator import MazeGenerator
from mazegen.display import select_wall_char, display, display_regenerate
from mazegen.solver import bfs, path_to_directions
from mazegen.key_reader import read_key
import random
from mazegen.emoji_maker import cute_anime_girl_smiling, looking_eyes
import time
import sys


def venv_detector() -> bool:
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment! \n"
              "The machines can see everything you install.\n")

        print("To enter the construct, run: \n"
              "python -m venv .venv \n"
              "source .venv/bin/activate # On Unix\n"
              ".venv\\Scripts\\activate # On Windows\n")

        print("Then run this program again.\n")
        return False
    return True


def write_output(
    maze: MazeGenerator,
    config: Valid_Config,
    path: list[tuple[int, int]],
) -> None:
    """Write the maze solution to the output file specified in config.

    The file contains the hex-encoded grid rows, a blank separator line,
    the entry and exit coordinates, and the direction string.

    Args:
        maze: The generated maze object.
        config: Validated configuration supplying output_file, entry, exit.
        path: Ordered list of (x, y) positions from entry to exit.
    """
    lines = []
    for y in range(maze.height):
        row = "".join(format(maze.grid[x][y]["value"], 'X') for x in range(
            maze.width))
        lines.append(row)
    try:
        with open(config.output_file, "w") as file:
            file.write(f"{'\n'.join(line for line in lines)}\n"
                       f"\n{",".join(map(str, config.entry))}\n"
                       f"{",".join(map(str, config.exit))}\n"
                       f"{"".join(
                           direction for direction in path_to_directions(
                               path))}\n")
    except PermissionError:
        raise PermissionError("Unable to write output file. Please check "
              "permissions and try again.\n")


def program_running(
    maze: MazeGenerator,
    config: Valid_Config,
    wall_char: str,
) -> None:
    """Run the interactive event loop until the user chooses to exit.

    Key bindings:
        'd': cycle wall emoji.
        'f': toggle solution path visibility.
        'o': regenerate the maze with a new random seed.
        'i': regenerate the maze with the same seed.
        'e': open the exit confirmation sub-menu.

    Args:
        maze: The generated maze object (mutated on regeneration).
        config: Validated configuration.
        wall_char: Initial wall emoji.
    """
    running = True
    running2 = True
    show = False
    path = bfs(maze.grid, maze.entry, maze.exit)
    write_output(maze, config, path)
    while running:
        running2 = True
        key = read_key()
        if key == 'd':
            print("\033c")
            wall_char = select_wall_char()
            display(maze, config, wall_char, path if show else "")
            time.sleep(0.3)
        elif key == 'e':
            print("\033c")
            looking_eyes()
            print("\n\nPress 'e' to continue exiting (don't do it)\n"
                  "Press 'f' if you want to come back to the maze")
            while running2:
                key = read_key()
                if key == 'e':
                    running = False
                    running2 = False
                elif key == 'f':
                    running2 = False
            if running:
                print("\033c")
                display(maze, config, wall_char, path)
            time.sleep(0.3)

        elif key == 'f':
            show = not show
            print("\033c")
            display(maze, config, wall_char, path if show else "")
            time.sleep(0.3)
        elif key == 'o':
            print("\033c")
            maze.seed = random.randint(0, 9999)
            maze.grid = []
            maze.init_grid()
            maze.generate()
            display_regenerate(maze, config, wall_char, "")
            path = bfs(maze.grid, maze.entry, maze.exit)
            write_output(maze, config, path)
            show = False
            time.sleep(0.3)
        elif key == 'i':
            print("\033c")
            display_regenerate(maze, config, wall_char, "")
            path = bfs(maze.grid, maze.entry, maze.exit)
            write_output(maze, config, path)
            show = False
            time.sleep(0.3)


def main() -> None:
    """Entry point: load config, generate the maze, and start the
    event loop."""
    if venv_detector() is False:
        return
    else:
        try:
            print("\033c")
            config = Valid_Config()
            maze = MazeGenerator(
                config.width,
                config.height,
                config.entry,  # type: ignore[arg-type]
                config.exit,   # type: ignore[arg-type]
                config.perfect,
                config.seed
            )
            print("\033[?25l")
            maze.init_grid()
            maze.generate()

            wall_char = "🌳"
            path = ""
            display_regenerate(maze, config, wall_char, path)
            program_running(maze, config, wall_char)

        except ValidationError as e:
            for err in e.errors():
                print(err["msg"])
        except ValueError as e:
            print("\033c", end="")
            print(e)
        except KeyboardInterrupt:
            print("\033c", end="")
            cute_anime_girl_smiling()
        except PermissionError as e:
            print("\033c", end="")
            print(f"Permission error: {e}")
        else:
            print("\033c")
            cute_anime_girl_smiling()
        finally:
            print("\033[?25h", end="")


if __name__ == "__main__":
    main()
