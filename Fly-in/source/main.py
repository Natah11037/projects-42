from source.controller.simulation import Simulation

from .controller.graph import Graph
from .parsing.parser import Parser
from .controller.pathfinder import Pathfinder
import os

if __name__ == "__main__":
    parsed = Parser(os.getenv("MAP"))
    parsed.parse()
    graph = Graph(parsed.data)
    pathfinder = Pathfinder(graph)
    print(pathfinder.find_path())
    simulator = Simulation(graph, graph.data['nb_drones'], pathfinder)
    simulator.load_drones()
    for drone in simulator.drones:
        print(f"ID {drone.name}:", drone.current_zone)
    counter = 0
    for i in range(len(simulator.drones[0].path) - 1):
        counter += 1
        print(f"Turn {counter}:")
        simulator.mooving_drones()
        for drone in simulator.drones:
            print(f"ID {drone.name}:", drone.current_zone)
