from .models import Zone, Connection


class Graph():
    def __init__(self, data: dict):
        self.data = data
        all_hubs = data["hub"] + [data["start_hub"], data["end_hub"]]
        self.zones = {
            hub["name"]: Zone(**{
                key: value for key, value in hub.items() if key != "index"})
            for hub in all_hubs
        }
        self.connections = []
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
                neighbors.append(connection.zone2)
            elif connection.zone2.name == zone.name:
                neighbors.append(connection.zone1)
        return neighbors
