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
            Drone(
                name=f"Drone {i}",
                current_zone=self.graph.zones[self.graph.start_hub.name],
                path=self.pathfinder.find_path(),
            )
            for i in range(1, self.nb_drones + 1)
        ]

    def moving_drones(self):
        restricted_con_status = []
        for drone in self.drones:
            if drone.current_zone == self.graph.end_hub:
                continue
            next_zone = drone.path[drone.path_index + 1]
            if next_zone.max_drones == next_zone.nb_drones:
                continue
            if next_zone.zone == "restricted":
                if drone.in_transit is True:
                    connection = drone.current_zone
                    drone.in_transit = False
                    restricted_con_status.append(connection)
                    drone.current_zone = next_zone
                    drone.current_zone.nb_drones += 1
                    drone.path_index += 1
                    self.cost += 1
                else:
                    connection = self.graph.get_connection(
                        drone.current_zone, next_zone
                    )
                    if (
                        connection.nb_drones == connection.max_link_capacity
                        or next_zone.nb_drones >= next_zone.max_drones
                    ):
                        # Rerouting
                        og_type = next_zone.zone
                        next_zone.zone = "blocked"
                        path = self.pathfinder.find_path(drone.current_zone)
                        if path:
                            drone.path = path
                            drone.path_index = 1
                        next_zone.zone = og_type
                        next_zone = drone.path[drone.path_index]
                        if next_zone.zone == "restricted":
                            connection = self.graph.get_connection(
                                drone.current_zone, next_zone
                            )
                            connection.nb_drones += 1
                            drone.in_transit = True
                            drone.current_zone.nb_drones -= 1
                            drone.current_zone = connection
                            connection = drone.current_zone
                        else:
                            drone.current_zone = next_zone
                    else:
                        connection.nb_drones += 1
                        drone.in_transit = True
                        drone.current_zone.nb_drones -= 1
                        drone.current_zone = connection
                        connection = drone.current_zone
            else:
                next_zone.nb_drones += 1
                drone.current_zone.nb_drones -= 1
                drone.current_zone = next_zone
                drone.path_index += 1
        for connection in restricted_con_status:
            connection.nb_drones -= 1
