from httpx import ConnectError

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
        restrictred_con_status = []
        for drone in self.drones:
            if drone.current_zone == self.graph.end_hub:
                continue
            next_zone = drone.path[drone.path_index + 1]
            if next_zone.max_drones == next_zone.nb_drones:
                continue
            if next_zone.zone == "restricted":
                if drone.in_transit is False:
                    connection = self.graph.get_connection(
                        drone.current_zone, next_zone)
                    if connection is None:
                        raise ValueError("OH C'EST PAS POSSIBLE LA")
                    if connection.nb_drones == connection.max_link_capacity:
                        # Rerouting
                        continue
                        # og_type = next_zone.zone
                        # next_zone.zone = "blocked"
                        # path = self.pathfinder.find_path(drone.current_zone)
                        # if path:
                        #     drone.path = path
                        # print(drone.path)
                        # next_zone.zone = og_type
                else:
                    connection = drone.current_zone
                if drone.in_transit is True:
                    drone.in_transit = False
                    restrictred_con_status.append(connection)
                    drone.current_zone = next_zone
                    drone.current_zone.nb_drones += 1
                    drone.path_index += 1
                    self.cost += 1
                else:
                    connection.nb_drones += 1
                    drone.in_transit = True
                    drone.current_zone.nb_drones -= 1
                    drone.current_zone = connection
            else:
                next_zone.nb_drones += 1
                drone.current_zone.nb_drones -= 1
                drone.current_zone = next_zone
                drone.path_index += 1
        for connection in restrictred_con_status:
            connection.nb_drones -= 1
