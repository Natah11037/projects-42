class Zone():
    def __init__(self, name: str, x: int, y: int, zone_type: str,
                 max_drones: int, color: str):
        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.max_drones = max_drones
        self.color = color


class Connection():
    def __init__(self, zone1: Zone, zone2: Zone, max_link_capacity: int):
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity
