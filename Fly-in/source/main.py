from source.controller.simulation import Simulation

from source.view.visualizer import Visualizer
from .controller.graph import Graph
from .parsing.parser import Parser
from .controller.pathfinder import Pathfinder
import os


def print_simulation(simulator, graph):
    while (
        len(
            set(
                [drone.current_zone for drone in simulator.drones]
                + [graph.end_hub]
                )
            )
            != 1
            ):
        print(" ".join(simulator.moving_drones()))


if __name__ == "__main__":
    parsed = Parser(os.getenv("MAP"))
    parsed.parse()
    graph = Graph(parsed.data)
    pathfinder = Pathfinder(graph)
    path = pathfinder.find_path()
    simulator = Simulation(graph, graph.data["nb_drones"], pathfinder)
    simulator.load_drones()
    print_simulation(simulator, graph)

    graph = Graph(parsed.data)
    pathfinder = Pathfinder(graph)
    simulator = Simulation(graph, graph.data["nb_drones"], pathfinder)
    simulator.load_drones()

    game = Visualizer(
        graph,
        simulator.get_view_state(),
        simulator.advance_turn,
        os.getenv("MAP"),
    )
    game.run()
