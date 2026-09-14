*This project has been created as part of the 42 curriculum by nweber--.*

# Fly-in

## Description

Fly-in is a Python simulation that routes several drones through a network of
connected zones. The project parses map files, builds a graph, finds routes,
simulates drone movements turn by turn, and displays the result in the
terminal and with Pygame.

The simulation supports zone capacities, connection capacities, restricted
zones, blocked zones, priorities, and simultaneous drone movements.

## Instructions

### Requirements

- Python 3.13 or later
- `uv`
- A graphical environment for the Pygame visualizer

Install the dependencies and create the virtual environment:

```bash
make install
```

Run the default map:

```bash
make run
```

Run another map with the `MAP` variable:

```bash
make run MAP=assets/maps/easy/02_simple_fork.txt
make run MAP=assets/maps/medium/03_priority_puzzle.txt
make run MAP=assets/maps/hard/03_ultimate_challenge.txt
```

The simulation first prints movements in the terminal and then opens the
Pygame visualizer. Press `Space` to advance one turn and `Escape` to quit.

Useful commands:

```bash
make debug MAP=assets/maps/easy/01_linear_path.txt
make lint
make lint-strict
make clean
```

## Algorithm and implementation

The parser reads the number of drones, hubs, metadata, and bidirectional
connections. It validates names, coordinates, capacities, duplicate entries,
and reachability from the start hub to the end hub.

The graph is implemented with the project's own `Zone` and `Connection`
classes; no external graph library is used. `Pathfinder` uses Dijkstra's
algorithm. The cost of entering a normal or priority zone is one turn, while
entering a restricted zone costs two turns. Blocked zones are excluded from
valid routes.

`Simulation` advances the drones turn by turn. Before each movement it checks
zone and connection capacities. Restricted-zone movements use the connection
as a temporary transit state. When a route is blocked, the simulation can
temporarily exclude the blocked zone and calculate another route.

The implementation is object-oriented and uses type hints. Flake8 and Mypy
are used to check the source code.

## Visual representation

The terminal output shows each movement using the format `D1-zone` and makes
the turn-by-turn schedule easy to follow. The Pygame visualizer displays the
map, hubs, connections, zone colors, and drone positions. A drone crossing a
restricted connection is displayed in transit. The visualizer can be stepped
one turn at a time with the keyboard.

## Map format

The first useful line defines the number of drones:

```text
nb_drones: 5
```

Start and end hubs, regular hubs, and bidirectional connections are then
declared as follows:

```text
start_hub: start 0 0 [color=green max_drones=5]
end_hub: goal 10 10 [color=yellow max_drones=5]
hub: corridor 4 3 [zone=priority color=blue max_drones=2]
connection: start-corridor
connection: corridor-goal [max_link_capacity=2]
```

Supported zone types are `normal`, `restricted`, `priority`, and `blocked`.
Comments beginning with `#` and blank lines are ignored.

## Project structure

```text
.
├── Makefile
├── pyproject.toml
├── README.md
├── subject.md
├── assets/
└── source/
    ├── main.py
    ├── controller/
    ├── parsing/
    └── view/
```

## Resources

- Python documentation: https://docs.python.org/3/
- Dijkstra's algorithm: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- Pygame documentation: https://www.pygame.org/docs/
- Mypy documentation: https://mypy.readthedocs.io/
- Flake8 documentation: https://flake8.pycqa.org/

AI tools were used as a development aid for repetitive tasks, documentation
wording, and review of parser, pathfinding, simulation, and typing issues.
All generated suggestions were checked, adapted to the project, and tested by
the authors.

## Validation

Run the standard checks before submitting:

```bash
make lint
```

The project also provides `make lint-strict` for stricter Mypy checks.