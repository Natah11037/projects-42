from wcwidth import wcswidth
import re
import random
import time
from tqdm import tqdm
import termios
import tty
import sys
from mazegen.maze_generator import MazeGenerator
from mazegen.configuration.parser import Valid_Config


GREEN = "\033[92m"
RESET = "\033[0m"


def random_binary() -> str:
    return f"{GREEN}{random.randint(0, 1)}{RESET}"


binary_emoji = f"{GREEN}01{RESET}"
ansi_escape = re.compile(r'\x1b\[[0-9;]*m')


def check_char_width(char: str) -> str:
    width = 2
    clean_char = ansi_escape.sub('', char)
    char_width = wcswidth(clean_char)
    if char_width <= 0:
        return char
    if char_width < width:
        return char + " " * (width - char_width)
    return char


def select_wall_char() -> str:
    """Return a randomly chosen wall emoji from a fixed palette."""
    walls = [
        "🌳",
        "🌲",
        "🌴",
        "🎄",
        "🌵",
        "🌻",
        "🌾",
        "🌺",
        "🌷",
        "🌹",
    ]
    return random.choice(walls)


def render_maze(
    grid: list[list[dict[str, bool | int]]],
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    path: list[tuple[int, int]] | str | None = None,
    wall_char: str = "🌳",
    path_char: str = "🐾",
    sign: list[tuple[int, int]] | set[tuple[int, int]] | None = None,
) -> list[str]:
    """Render the maze as a list of display-ready strings.

    Each cell is drawn as a 3-part block (top wall, middle content, bottom
    wall). Emojis are padded to a consistent 2-column width via wcwidth.

    Args:
        grid: Maze grid indexed as grid[x][y] (column, row).
        entry: Entry cell position as (column, row), shown as 🐕.
        exit_pos: Exit cell position as (column, row), shown as 🦴.
        path: Sequence of (x, y) positions to highlight as 🐾, or a falsy
            value to skip path rendering.
        wall_char: Emoji used to draw walls.
        path_char: Emoji used to draw path cells.
        sign: Set or list of (x, y) positions belonging to the '42' pattern;
            rendered as solid walls.

    Returns:
        List of strings, one per rendered row (top wall + content rows).
    """
    lines = []
    width = len(grid)        # grid[x] → number of columns
    height = len(grid[0])   # grid[x][y] → number of rows
    for y in range(height):  # iterating over rows for display
        top_line = ""
        middle_line = ""
        bottom_line = ""
        for x in range(width):  # x = column
            top_line += check_char_width(wall_char)
            if grid[x][y]["north"]:
                top_line += check_char_width(wall_char)
            else:
                top_line += check_char_width(" ")
            if grid[x][y]["west"]:
                middle_line += check_char_width(wall_char)
            else:
                middle_line += check_char_width(" ")
            if (x, y) == entry:
                middle_line += check_char_width("🐕")
            elif (x, y) == exit_pos:
                middle_line += check_char_width("🦴")
            elif path and (x, y) in path:
                middle_line += check_char_width(path_char)
            elif sign and (x, y) in sign:
                middle_line += check_char_width(wall_char)
            else:
                middle_line += check_char_width(" ")
            bottom_line += check_char_width(wall_char)
            if grid[x][y]["south"]:
                bottom_line += check_char_width(wall_char)
            else:
                bottom_line += check_char_width(" ")
        top_line += check_char_width(wall_char)
        middle_line += check_char_width(wall_char)
        bottom_line += check_char_width(wall_char)
        lines.append(top_line)
        lines.append(middle_line)
        if y == height - 1:
            lines.append(bottom_line)
    return lines


def display(
    maze: MazeGenerator,
    config: Valid_Config,
    wall_char: str,
    path: list[tuple[int, int]] | str,
) -> None:
    """Print the maze and its config summary to stdout.

    Args:
        maze: The generated maze object.
        config: Validated configuration (width, height, entry, exit, …).
        wall_char: Emoji used to render walls.
        path: Solution path to highlight, or an empty string to hide it.
    """
    lines = render_maze(maze.grid, maze.entry, maze.exit,
                        path=path, wall_char=wall_char, sign=maze.sign)
    for line in lines:
        print(line)
    print("\nConfig loaded successfully:")
    print(f"  width       = {config.width}")
    print(f"  height      = {config.height}")
    print(f"  entry       = {config.entry}")
    print(f"  exit        = {config.exit}")
    print(f"  output_file = {config.output_file}")
    print(f"  perfect     = {config.perfect}")
    print(f"  seed        = {config.seed}\n")
    if config.width <= 10 or config.height <= 8:
        print("Maze size is too small to contain the 42 pattern.\n")
    print("\nPress 'd' to switch maze color\n"
          "Press 'f' to show/hide the path\n"
          "Press 'o' to regenerate a random maze\n"
          "Press 'i' to regenerate the same maze\n"
          "Press 'e' to exit")


def display_regenerate(
    maze: MazeGenerator,
    config: Valid_Config,
    wall_char: str,
    path: list[tuple[int, int]] | str,
) -> None:
    """Animate the maze reveal with a binary-rain effect, then show the maze.

    Displays a tqdm progress bar while filling the terminal with random 0/1
    values, then progressively replaces them with the final maze rendering.
    Terminal raw-mode settings are restored in a finally block.

    Args:
        maze: The generated maze object.
        config: Validated configuration (width, height, entry, exit, …).
        wall_char: Emoji used to render walls in the final frame.
        path: Solution path to highlight, or an empty string to hide it.
    """
    lines = render_maze(maze.grid, maze.entry, maze.exit,
                        path=path, wall_char=binary_emoji, sign=maze.sign)
    bar_size = maze.width * 4 + 1
    if maze.width * maze.height <= 500:
        speed1 = 0.00050
    elif maze.width * maze.height > 500 and maze.width * maze.height <= 2500:
        speed1 = 0.00050
    else:
        speed1 = 0.0000050
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)
    list_coord = [
        (x, y) for x in range(maze.height * 2 + 2) for y in range(
            maze.width * 4 + 3)]
    total = len(list_coord) + sum(
        len(ansi_escape.sub('', line)) for line in lines)
    bar_row = maze.height * 2 + 4
    try:
        print("\033c")
        sys.stdout.write(f"\033[{bar_row};1H")
        sys.stdout.flush()
        pbar = tqdm(total=total, desc="Loading Human visualisation",
                    ncols=bar_size,
                    bar_format="{desc}: |{bar}| {percentage:.1f}%")
        random.shuffle(list_coord)
        for x, y in list_coord:
            sys.stdout.write(f"\033[{x};{y}H")
            sys.stdout.flush()
            sys.stdout.write(random_binary())
            sys.stdout.flush()
            sys.stdout.write(f"\033[{bar_row};1H")
            sys.stdout.flush()
            pbar.update(1)
            time.sleep(speed1)
        for y, line in enumerate(lines):
            sys.stdout.write(f"\033[{y + 1};1H")
            sys.stdout.flush()
            sys.stdout.write(line)
            sys.stdout.flush()
            visible_len = len(ansi_escape.sub('', line))
            sys.stdout.write(f"\033[{bar_row};1H")
            sys.stdout.flush()
            for _ in range(visible_len):
                pbar.update(1)
            time.sleep(0.050)
        pbar.close()
        sys.stdout.write(f"\033[{bar_row};1H\033[2K")
        sys.stdout.flush()
        final_lines = render_maze(maze.grid, maze.entry, maze.exit,
                                  path=path, wall_char=wall_char,
                                  sign=maze.sign)
        for y, line in enumerate(final_lines):
            sys.stdout.write(f"\033[{y + 1};1H")
            sys.stdout.flush()
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(0.050)
        cursor_config_loaded = len(final_lines) + 2
        sys.stdout.write(f"\033[{cursor_config_loaded};1H\r\n"
                         f"Config loaded successfully:\r\n")
        sys.stdout.write(f"  width       = {config.width}\r\n")
        sys.stdout.write(f"  height      = {config.height}\r\n")
        sys.stdout.write(f"  entry       = {config.entry}\r\n")
        sys.stdout.write(f"  exit        = {config.exit}\r\n")
        sys.stdout.write(f"  output_file = {config.output_file}\r\n")
        sys.stdout.write(f"  perfect     = {config.perfect}\r\n")
        sys.stdout.write(f"  seed        = {maze.seed}\r\n\r\n")
        if config.width <= 10 or config.height <= 8:
            sys.stdout.write("Maze size is too small to contain "
                             "the 42 pattern.\n")
        sys.stdout.flush()
        sys.stdout.write("\r\nPress 'd' to switch maze color\r\n"
                         "Press 'f' to show/hide the path\r\n"
                         "Press 'o' to regenerate a random maze\r\n"
                         "Press 'i' to regenerate the same maze\r\n"
                         "Press 'e' to exit\r\n")
        sys.stdout.flush()
    finally:
        termios.tcflush(fd, termios.TCIFLUSH)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
