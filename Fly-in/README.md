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

Run a specific map by setting the `MAP` environment variable:

```bash
make run MAP=assets/maps/easy/01_linear_path.txt
make run MAP=assets/maps/easy/02_simple_fork.txt
make run MAP=assets/maps/medium/03_priority_puzzle.txt
make run MAP=assets/maps/hard/03_ultimate_challenge.txt
```

The workflow is the following:

1. The parser reads a map file and builds the graph.
2. The pathfinder computes a route for each drone.
3. The simulation advances turn by turn.
4. The terminal prints each movement in real time.
5. The Pygame visualizer then shows the same simulation step by step.

Example of terminal output for a simple path:

```text
D1-start
D1-start-waypoint1
D1-waypoint1-waypoint2
D1-waypoint2-goal
```

A more complete run can show several movements in a turn sequence, for
example:

```text
Turn 1: D1-start-waypoint1 D2-start-waypoint1
Turn 2: D1-waypoint1-waypoint2 D2-waypoint1-waypoint2
Turn 3: D1-waypoint2-goal
```

In the visualizer, the simulation is paused on each turn. Press `Space` to
advance one turn and `Escape` to quit.

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
the turn-by-turn schedule easy to follow. Each move is written as a textual
transition such as `D1-waypoint1`, `D1-waypoint1-waypoint2`, or
`D1-zone-name` depending on the state of the drone. This makes it easy to
check which drone leaves a zone, enters a restricted transit segment, or
reaches the end hub.

The Pygame visualizer displays the complete map, the hubs, the connections,
the zone colors, and the position of each drone. The display is built from the
same graph used for routing, so the layout always matches the map metadata.
A drone crossing a restricted connection is shown in transit between the two
zones. The simulation can be stepped one turn at a time with the keyboard,
which helps review complex routing decisions and capacity constraints.

### Personalized visualization

The visualizer is not limited to a plain graph drawing: it loads a custom
background and animated sprite assets from the `source/view/utilities/`
folder.

- `sonic_map.png` is used as the background image.
- `sonic_ring.gif` is used for animated zones.
- Each drone has its own GIF sprite (`sonic-drone.gif`, `tails-drone.gif`,
  `amy-drone.gif`, `knuckle-drone.gif`, `cream-drone.gif`,
  `metal-sonic-drone.gif`, `shadow-drone.gif`).

Those assets are loaded in `Visualizer.run()`, and the screen is rescaled to
fit the current window size. The zones are positioned automatically from the
coordinates declared in the map, and the drone position is computed from the
same coordinates so the animation stays aligned with the graph.

The visual style is also partly driven by the map data itself:

- zone colors can be defined in the map using `color=...`
- different zone types can be styled through their metadata and route logic
- connection lines are drawn between paired hubs
- the current turn is displayed in the top-left corner of the window

This means the display can be customized both by changing the asset images and
by modifying the map configuration. For a richer visual theme, it is enough to
replace the image files in `source/view/utilities/` and keep the same names, or
to tweak the map color values in the input file.

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