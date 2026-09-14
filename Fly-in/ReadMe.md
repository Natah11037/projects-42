# Fly-in

Fly-in is a drone simulation in which drones travel from a starting hub to an end hub through a network of connected zones. The project combines map parsing, pathfinding, turn-based simulation, and Pygame visualization.

## Features

- Read and validate text-based maps.
- Represent the network as a graph.
- Find paths with Dijkstra's algorithm.
- Manage zone and connection capacities.
- Support normal, restricted, priority, and blocked zones.
- Simulate multiple drones in parallel.
- Display movements in the terminal.
- Visualize the simulation with Pygame and Sonic assets.
- Check code style and typing with Flake8 and Mypy.

## Requirements

- Python `>= 3.13`.
- `uv` to install dependencies and manage the virtual environment.
- A working graphical environment to run the Pygame visualizer.

The main dependencies are:

- `pygame` for visualization.
- `Pillow` for loading images and animated GIFs.
- `httpx` for the project's dependencies.

## Installation

From the project root:

```bash
make install
```

This command checks that `uv` is installed, creates or synchronizes the `.venv` environment, and installs the dependencies defined in `pyproject.toml`.

Manual `uv` installation:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Running the Project

Run the default easy map:

```bash
make run
```

Choose a specific map:

```bash
make run MAP=assets/maps/easy/02_simple_fork.txt
make run MAP=assets/maps/medium/03_priority_puzzle.txt
make run MAP=assets/maps/hard/03_ultimate_challenge.txt
make run MAP=assets/maps/challenger/01_the_impossible_dream.txt
```

The program first prints movements in the terminal and then opens the graphical visualization. In the Pygame window:

- `Space` advances one turn.
- `Escape` exits the program.

Run the program with the Python debugger:

```bash
make debug MAP=assets/maps/easy/01_linear_path.txt
```

## Useful Commands

```bash
make install       # Install or synchronize the environment
make run           # Run the simulation
make debug         # Run the simulation with pdb
make lint          # Run Flake8 and Mypy with project rules
make lint-strict   # Run strict Flake8 and Mypy checks
make clean         # Remove Python, Mypy, and Pytest caches
```

## Project Structure

```text
.
├── Makefile
├── pyproject.toml
├── ReadMe.md
├── subject.md
├── assets/
│   └── maps/
│       ├── easy/
│       ├── medium/
│       ├── hard/
│       ├── challenger/
│       └── README.md
└── source/
    ├── main.py
    ├── controller/
    │   ├── graph.py
    │   ├── models.py
    │   ├── pathfinder.py
    │   └── simulation.py
    ├── parsing/
    │   └── parser.py
    └── view/
        ├── visualizer.py
        └── utilities/
            ├── sonic_map.png
            └── *.gif
```

### Main Modules

- `source/main.py`: entry point. It loads the map specified by `MAP`, builds the graph, runs the terminal simulation, and starts the visualizer.
- `source/parsing/parser.py`: reads maps and validates hubs, coordinates, connections, metadata, duplicates, and reachability.
- `source/controller/models.py`: defines `Zone`, `Connection`, `Drone`, and the view state objects.
- `source/controller/graph.py`: converts parser data into `Zone` and `Connection` objects.
- `source/controller/pathfinder.py`: calculates the minimum-cost path between the start and end hubs.
- `source/controller/simulation.py`: moves drones turn by turn while applying zone and connection capacities.
- `source/view/visualizer.py`: displays the graph, hubs, and drones in a Pygame window.

## Map Format

Blank lines and lines beginning with `#` are ignored. The first useful line must define the total number of drones:

```text
nb_drones: 5
```

Exactly one start hub and one end hub must then be defined:

```text
start_hub: start 0 0 [color=green max_drones=5]
end_hub: goal 10 10 [color=yellow max_drones=5]
```

Intermediate hubs use the following format:

```text
hub: corridor 4 3 [zone=priority color=blue max_drones=2]
```

Connections are bidirectional:

```text
connection: start-corridor
connection: corridor-goal [max_link_capacity=2]
```

Hub names must not contain spaces or dashes, because the dash separates the two endpoints of a connection.

## Metadata

### Hubs

| Key | Default value | Description |
| --- | --- | --- |
| `zone` | `normal` | Zone type. Accepted values: `normal`, `restricted`, `priority`, `blocked`. |
| `color` | `white` | Color used by the visualizer. |
| `max_drones` | `1` | Maximum number of drones in the zone. |

A metadata key may appear only once in the same hub. For example, this is invalid:

```text
hub: room 1 1 [color=red color=blue]
```

The start and end hubs are occupancy exceptions in the simulation rules: they can hold all drones. In the current implementation, their capacity is normalized to the total number defined by `nb_drones`.

### Connections

| Key | Default value | Description |
| --- | --- | --- |
| `max_link_capacity` | `1` | Maximum number of drones that can cross the connection at the same time. |

Repeating a key raises an error:

```text
connection: start-goal [max_link_capacity=1 max_link_capacity=2]
```

Capacities must be positive integers, except that a zero capacity is allowed for a connection leading to a blocked zone.

## Zone Types

- `normal`: movement costs `1` turn.
- `restricted`: movement costs `2` turns. The drone occupies the connection while in transit.
- `priority`: movement costs `1` turn. The type is preserved in the model and can be used to improve the pathfinding strategy.
- `blocked`: inaccessible zone that is ignored by pathfinding.

## Simulation Rules

- All drones are created in the start hub.
- Drones are named `D1`, `D2`, and so on.
- Each drone follows a path calculated by the `Pathfinder`.
- A zone cannot exceed its `max_drones` capacity.
- A connection cannot exceed its `max_link_capacity` capacity.
- Drones that reach the end hub remain marked as delivered.
- The simulation advances in discrete turns.
- A blocked drone waits, unless another route can be recalculated when a restricted zone is saturated.
- The program ends when all drones have reached the end hub.

Terminal movements use the following format:

```text
D1-corridor D2-corridor
D1-goal D2-goal
```

When a drone crosses a connection toward a restricted zone, the connection is displayed during transit.

## Available Maps

Maps are grouped by difficulty:

- `easy/`: simple paths and introductory capacity constraints.
- `medium/`: alternate paths, loops, restricted zones, and priorities.
- `hard/`: mazes and significant capacity constraints.
- `challenger/`: stress-test maps designed to push the algorithm to its limits.

The challenger map `01_the_impossible_dream.txt` contains `25` drones and is used as a performance benchmark. The file `assets/maps/README.md` provides more details about each map and gives a reference target of `45` turns for this map.

## Validation and Quality

Run the standard checks:

```bash
make lint
```

Run the strict checks:

```bash
make lint-strict
```

Remove generated files:

```bash
make clean
```

Check the syntax of an individual module:

```bash
.venv/bin/python -m py_compile source/parsing/parser.py
```

## Runtime Architecture

```text
Text map
    │
    ▼
Parser
    │ validated data
    ▼
Graph ───────────────► Pathfinder
    │                       │ path
    └──────────────► Simulation
                            │ state per turn
                            ▼
                    Terminal + Visualizer
```

The project does not use an external graph library. The graph is built with the classes in `controller`, and pathfinding is implemented directly in `pathfinder.py`.

## Known Limitations

- The graphical mode depends on the assets in `source/view/utilities/` and on an environment that can open a Pygame window.
- The current strategy mainly calculates a minimum-cost path per drone; it does not always guarantee globally optimal scheduling for all drones.
- The `priority` type is recognized by the parser, but its cost is currently the same as a `normal` zone.
- The map files are validation and benchmark scenarios; `challenger` maps can be very difficult for the current implementation.
