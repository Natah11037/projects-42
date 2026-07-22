class Zone():
    def __init__(self, name: str, x: int, y: int, zone: str,
                 max_drones: int, color: str):
        self.name = name
        self.x = x
        self.y = y
        self.zone = zone
        self.max_drones = max_drones
        self.color = color

    def __repr__(self):
        return f"{self.name}"


class Connection():
    def __init__(self, zone1: Zone, zone2: Zone, max_link_capacity: int):
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity
