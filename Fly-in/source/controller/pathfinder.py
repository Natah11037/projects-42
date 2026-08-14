import heapq
from .graph import Graph
from .models import Zone


class Pathfinder:
    def __init__(self, graph: Graph):
        self.graph = graph

    def find_path(self) -> list[Zone]:
        start: Zone = self.graph.zones[self.graph.data["start_hub"]["name"]]
        end: str = self.graph.data["end_hub"]["name"]
        queue: list[tuple[int, Zone]] = [(0, start)]
        paths: dict[str, list] = self.graph.set_zones_to_inf()
        paths[start.name] = [0, []]
        heapq.heapify(queue)
        while queue:
            current_distance, current_zone = heapq.heappop(queue)
            if current_zone == self.graph.zones[end]:
                return paths[end][1] + [current_zone]
            if current_distance > paths[current_zone.name][0]:
                continue
            for neighbor in self.graph.get_neighbors(current_zone):
                distance = current_distance + neighbor.get_cost()
                if distance < paths[neighbor.name][0]:
                    paths[neighbor.name][0] = distance
                    paths[neighbor.name][1] = (
                        paths[current_zone.name][1] + [current_zone]
                    )
                    heapq.heappush(queue, (distance, neighbor))
        return []
