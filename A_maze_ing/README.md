*This project has been created as part of the 42 curriculum by eel-arou, nweber--.*

## Description

A-Maze-ing is a maze generator written in Python. It reads a configuration file, generates a maze (optionally perfect — with a single path between entry and exit), displays it in the terminal using emoji characters, and writes the result to an output file in hexadecimal format.

The generated maze always embeds a visible **"42" pattern** formed by fully closed cells, and supports interactive controls: regenerate, show/hide the shortest path, and change wall colours.

## Instructions

### Requirements

- Python 3.10 or later
- [uv](https://github.com/astral-sh/uv) (recommended package manager)

### Installation

```bash
make install
```

### Run

```bash
make run
```

Or manually:

```bash
python3 a_maze_ing.py configuration/config.txt
```

### Other Makefile rules

```bash
make debug       # Run with Python debugger (pdb)
make clean       # Remove __pycache__, .mypy_cache
make lint        # Run flake8 and mypy
make lint-strict # Run flake8 and mypy --strict
```

### Interactive controls

| Key | Action |
|-----|--------|
| `o` | Re-generate a new maze |
| `f` | Show / hide the shortest path |
| `d` | Change wall colour |
| `e` | Exit |
| `Ctrl+C` | Exit (with surprise) |

## Configuration file

The configuration file uses the `KEY=VALUE` format. Lines starting with `#` are comments and are ignored. Keys are case-insensitive.

| Key | Description | Example |
|-----|-------------|---------|
| `WIDTH` | Number of columns (≥ 4) | `WIDTH=20` |
| `HEIGHT` | Number of rows (≥ 4) | `HEIGHT=15` |
| `ENTRY` | Entry cell coordinates `x,y` | `ENTRY=0,0` |
| `EXIT` | Exit cell coordinates `x,y` | `EXIT=19,14` |
| `OUTPUT_FILE` | Output filename (must end in `.txt`) | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Perfect maze (single path) | `PERFECT=True` |
| `SEED` *(optional)* | Seed for reproducibility | `SEED=42` |

Example config file (`configuration/config.txt`):

```
# A-Maze-ing configuration
WIDTH=16
HEIGHT=16
ENTRY=1,1
EXIT=13,14
OUTPUT_FILE=maze.txt
PERFECT=TRUE
```

## Output file format

The output file contains one hexadecimal digit per cell. Each digit encodes which walls are closed using a 4-bit mask:

| Bit | Direction |
|-----|-----------|
| 0 (LSB) | North |
| 1 | East |
| 2 | South |
| 3 | West |

`1` = wall closed, `0` = wall open. Cells are stored row by row, one row per line.

After an empty line, three lines follow:
- Entry coordinates
- Exit coordinates
- Shortest path from entry to exit using `N`, `E`, `S`, `W`

## Maze generation algorithm

We chose the **Depth-First Search (DFS) recursive backtracker** algorithm.

### How it works

Starting from the entry cell, the algorithm visits unvisited neighbours at random. Each time it moves to a neighbour, it removes the wall between them. When it reaches a dead end, it backtracks until it finds a cell with unvisited neighbours. This continues until every cell has been visited.

### Why DFS

- Produces **perfect mazes** by construction (a spanning tree of the grid), which directly satisfies the `PERFECT=True` requirement.
- Naturally generates long, winding corridors — the classic "maze feel".
- Simple to implement and understand.
- Deterministic given a seed, making mazes reproducible.

For `PERFECT=False`, additional walls are removed after DFS to create loops (multiple paths between cells).

## Reusable module

The `MazeGenerator` class is implemented in `mazegen.py` as a standalone module, installable as a pip package (`mazegen-*.whl`).

### Installation

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

### Basic usage

```python
from mazegen import MazeGenerator

maze = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)
maze.init_grid()
maze.generate()

# Access the grid
grid = maze.grid          # grid[x][y] — dict with keys: north, south, east, west (bool)
sign = maze.sign          # list of (x, y) tuples forming the "42" pattern
```

### Custom parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `width` | `int` | Number of columns |
| `height` | `int` | Number of rows |
| `entry` | `tuple[int, int]` | Entry cell `(x, y)` |
| `exit` | `tuple[int, int]` | Exit cell `(x, y)` |
| `perfect` | `bool` | Perfect maze if `True` |
| `seed` | `int` | Seed for reproducibility |

### Accessing the solution

```python
from solver import bfs, path_to_directions

path = bfs(maze.grid, maze.entry, maze.exit)
# path → list of (x, y) tuples

directions = path_to_directions(path)
# directions → list of "N", "E", "S", "W"
```

### Building the package

```bash
cd mazegen_src
python3 -m venv mon_venv
mon_venv/bin/pip install build
mon_venv/bin/python -m build
# generates mazegen-*.whl in mazegen_src/dist/
```

## Resources

### References

- [Maze generation algorithms — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Depth-first search — Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
- [Pydantic documentation](https://docs.pydantic.dev/)
- [pydantic-settings documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [wcwidth — terminal character width](https://pypi.org/project/wcwidth/)


## Team and project management

### Team members

| **eel-arou** | Core maze generation (`mazegen.py`), BFS solver (`solver.py`), main program (`a_maze_ing.py`), "42" sign placement, Ctrl+C easter egg, `write_output` function (hex output file), Makefile rules completion (`debug`, `clean`, `lint`, `lint-strict`), type hints across all files, `mazegen` pip package (`mazegen_src/`, `.whl`), merge management |

| **nweber--** | Configuration parser (`configuration/parser.py`) with pydantic validation, terminal raw mode (`key_reader.py`), display & animations (`display.py`) including binary rain effect and tqdm progress bar, `PERFECT=False` implementation (wall removal with 3×3 rule), hex output file format, `sys.argv` for config file path, docstrings across all files, colour change & regeneration |

### Planning

We started by splitting the project into two independent parts: the generation core (eel-arou) and everything around it — display, config, output (nweber--). This worked well in parallel, then we merged and integrated both sides.

The planning evolved when we realised the output file format and the reusable package required more work than expected, and that the 3×3 open area rule needed a dedicated verification method in the generator.

### What worked well

- The DFS algorithm was straightforward to implement and the result was immediately visible.
- Using `pydantic-settings` for config parsing saved a lot of boilerplate validation code.
- Splitting the project cleanly between generation and display kept merge conflicts minimal at first.

### What could be improved

- We underestimated the time needed for the output file format and the reusable package setup.
- Starting with type hints and docstrings from the beginning would have saved refactoring time later.
- Better coordination on branches would have avoided some merge conflicts.

### Tools used

- **VS Code** — code editor
- **GitHub** — version control and collaboration
- **uv** — Python package and virtual environment management
