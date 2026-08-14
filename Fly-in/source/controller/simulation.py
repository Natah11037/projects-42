from .graph import Graph
from .models import Zone, Connection, Drone
from .pathfinder import Pathfinder


class Simulation:
    def __init__(self, graph: Graph, nb_drones: int, pathfinder: Pathfinder):
        self.drones = []
        self.zones = []
        self.connections = []
        self.cost = 0
        self.graph = graph
        self.nb_drones = nb_drones
        self.pathfinder = pathfinder

    def load_drones(self):
        self.drones = [
            Drone(name=f"Drone {i}", current_zone=self.graph.zones[
                self.graph.start_hub.name], path=self.pathfinder.find_path())
            for i in range(1, self.nb_drones + 1)
            ]

    def mooving_drones(self):
        for drone in self.drones:
            if drone.current_zone.name != self.graph.end_hub:
                if drone.in_transit is True:
                    drone.in_transit = False
                    self.cost += 1
                    continue
                drone.path_index += 1
                next_zone = drone.path[drone.path_index]
                if next_zone.max_drones == next_zone.nb_drones:
                    continue
                if next_zone.name != "blocked":
                    if next_zone.name == "restricted":
                        drone.in_transit = True
                    next_zone.nb_drones += 1
                    drone.current_zone.nb_drones -= 1
                    drone.current_zone = next_zone
                    self.cost += 1
