from .graph import Graph
from .models import (
    Connection,
    Drone,
    DroneViewState,
    SimulationViewState,
    Zone,
)
from .pathfinder import Pathfinder


class Simulation:
    def __init__(
        self, graph: Graph, nb_drones: int, pathfinder: Pathfinder
    ) -> None:
        self.drones: list[Drone] = []
        self.zones: list[object] = []
        self.connections: list[Connection] = []
        self.graph = graph
        self.nb_drones = nb_drones
        self.pathfinder = pathfinder
        self.turn = 0

    def load_drones(self) -> None:
        self.drones = [
            Drone(
                name=f"D{i}",
                current_zone=self.graph.zones[self.graph.start_hub.name],
                path=self.pathfinder.find_path(),
            )
            for i in range(1, self.nb_drones + 1)
        ]
        for drone in self.drones:
            drone.current_zone.nb_drones += 1

    def moving_drones(self) -> list[str]:
        movements = []
        restricted_con_status = []
        for drone in self.drones:
            if drone.current_zone == self.graph.end_hub:
                continue
            next_zone = drone.path[drone.path_index + 1]
            if next_zone.max_drones == next_zone.nb_drones:
                og_type = next_zone.zone
                next_zone.zone = "blocked"
                path = self.pathfinder.find_path(drone.current_zone)
                if path:
                    drone.path = path
                    drone.path_index = 0
                next_zone.zone = og_type
                next_zone = drone.path[drone.path_index + 1]
            if next_zone.zone == "restricted":
                if drone.in_transit is True:
                    connection = drone.current_zone
                    drone.in_transit = False
                    restricted_con_status.append(connection)
                    drone.current_zone = next_zone
                    drone.current_zone.nb_drones += 1
                    drone.path_index += 1
                    movements.append(f"{drone.name}-{next_zone.name}")
                else:
                    connection = self.graph.get_connection(
                        drone.current_zone, next_zone
                    )

                    if (
                        connection.nb_drones == connection.max_link_capacity
                        or next_zone.nb_drones == next_zone.max_drones or self.check_restricted_hub_connection(next_zone) == next_zone.max_drones
                    ):
                        # Rerouting
                        og_type = next_zone.zone
                        next_zone.zone = "blocked"
                        path = self.pathfinder.find_path(drone.current_zone)
                        if path:
                            drone.path = path
                            drone.path_index = 0
                        next_zone.zone = og_type
                        next_zone = drone.path[drone.path_index + 1]
                        if next_zone.zone == "restricted":
                            connection = self.graph.get_connection(
                                drone.current_zone, next_zone
                            )
                            connection.nb_drones += 1
                            drone.in_transit = True
                            drone.current_zone.nb_drones -= 1
                            drone.current_zone = connection
                            connection = drone.current_zone
                            movements.append(f"{drone.name}-{connection}")
                        else:
                            drone.current_zone = next_zone
                            drone.path_index += 1
                            movements.append(f"{drone.name}-{next_zone.name}")
                    else:
                        connection.nb_drones += 1
                        drone.in_transit = True
                        drone.current_zone.nb_drones -= 1
                        drone.current_zone = connection
                        movements.append(f"{drone.name}-{connection}")
            else:
                next_zone.nb_drones += 1
                drone.current_zone.nb_drones -= 1
                drone.current_zone = next_zone
                drone.path_index += 1
                movements.append(f"{drone.name}-{next_zone.name}")
        for connection in restricted_con_status:
            connection.nb_drones -= 1
        return movements

    def get_view_state(self) -> SimulationViewState:
        drones = []
        for drone in self.drones:
            if isinstance(drone.current_zone, Connection):
                zone_name = None
                connection_zone_names = (
                    drone.current_zone.zone1.name,
                    drone.current_zone.zone2.name,
                )
            else:
                zone_name = drone.current_zone.name
                connection_zone_names = None

            drones.append(
                DroneViewState(
                    name=drone.name,
                    zone_name=zone_name,
                    connection_zone_names=connection_zone_names,
                    path=tuple(zone.name for zone in drone.path),
                )
            )

        return SimulationViewState(self.turn, tuple(drones))

    def advance_turn(self) -> SimulationViewState:
        if self.drones and all(
            drone.current_zone == self.graph.end_hub for drone in self.drones
        ):
            return self.get_view_state()

        self.moving_drones()
        self.turn += 1
        return self.get_view_state()

    def check_restricted_hub_connection(self, zone):
        counter = zone.nb_drones
        connection_list = []
        for connection in self.graph.connections:
            if (connection.zone1 == zone or connection.zone2 == zone):
                connection_list.append(connection)
        for connection in connection_list:
            zone = connection.zone1 if connection.zone1 == zone else connection.zone2
            for drone in self.drones:
                if drone.current_zone == connection and drone.path[drone.path_index + 1] == zone:
                    counter += 1
        return counter