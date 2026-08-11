from graph import Graph
from models import Zone, Connection, Drone


class Simulation:
    def __init__(self):
        self.drones = []
        self.zones = []
        self.connections = []
        self.cost = 0
        self.graph = Graph()

    def load_drones(self, nb_drones: int):
        self.drones = [
            Drone(name=f"Drone {i}", current_zone=self.graph.start_hub)
            for i in range(nb_drones)
            ]

    def mooving_drones(self):
        for drone in self.drones:
            if drone.current_zone != self.graph.end_hub:
                if drone.in_transit is True:
                    drone.in_transit = False
                    self.cost += 1
                    continue
                next_zone = drone.path[drone.path_index + 1]
                if next_zone.zone != "blocked":
                    if next_zone.zone == "restricted":
                        drone.in_transit = True
                    drone.current_zone = next_zone
                    self.cost += 1
