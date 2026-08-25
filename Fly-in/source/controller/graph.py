from .models import Zone, Connection


class Graph():
    def __init__(self, data: dict):
        self.data = data
        self.zones = {
            hub["name"]: Zone(**{
                key: value for key, value in hub.items() if key != "index"})
            for hub in data["hub"] + [data["start_hub"], data["end_hub"]]
        }
        self.start_hub = self.zones[data["start_hub"]["name"]]
        self.end_hub = self.zones[data["end_hub"]["name"]]
        self.connections: list[Connection] = []
        for conn_data in data.get("connections", []):
            parts = conn_data["connection"].split("-")
            zone1 = self.zones[parts[0]]
            zone2 = self.zones[parts[1]]
            max_link_capacity = conn_data["metadata"].get(
                "max_link_capacity", 1)
            self.connections.append(Connection(
                zone1, zone2, max_link_capacity))

    def get_neighbors(self, zone: Zone):
        neighbors = []
        for connection in self.connections:
            if connection.zone1.name == zone.name:
                if connection.zone2.zone != "blocked":
                    neighbors.append(connection.zone2)
            elif connection.zone2.name == zone.name:
                if connection.zone2.zone != "blocked":
                    neighbors.append(connection.zone1)
        return neighbors

    def get_connection(self, zone1: Zone, zone2: Zone) -> Connection:
        for connection in self.connections:
            if ((connection.zone1 == zone1
               and connection.zone2 == zone2)
                or (connection.zone2 == zone1
               and connection.zone1 == zone2)):
                return connection

    def set_zones_to_inf(self):
        return {zone.name: [float("inf"), []] for zone in self.zones.values()}
