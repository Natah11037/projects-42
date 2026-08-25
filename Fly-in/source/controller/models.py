import math


class Zone:
    def __init__(self, name: str, x: int, y: int, zone: str,
                 max_drones: int, color: str):
        self.name = name
        self.x = x
        self.y = y
        self.zone = zone
        self.max_drones = max_drones
        self.color = color
        self.nb_drones = 0

    def __repr__(self):
        return f"{self.name}"

    def __lt__(self, other):
        return self.name < other.name

    def get_cost(self):
        if self.zone == "restricted":
            return 2
        elif self.zone == "blocked":
            return math.inf
        else:
            return 1


class Connection:
    def __init__(self, zone1: Zone, zone2: Zone, max_link_capacity: int):
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity
        self.nb_drones = 0

    def __str__(self) -> str:
        return self.zone1.name + "-" + self.zone2.name


class Drone:
    def __init__(self, name: str, current_zone: Zone,
                 path: list[Zone] | None = None):
        self.name = name
        self.current_zone = current_zone
        self.path: list[Zone] = path if path is not None else []
        self.in_transit = False
        self.path_index = 0
        self.status: str = "start"
