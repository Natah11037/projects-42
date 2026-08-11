import heapq
from .graph import Graph
from .models import Zone


def pathfinder(graph: Graph) -> list[str]:
    """
    Find the shortest path from start to end using Dijkstra's algorithm.

    Args:
        graph: The zone graph with start and end hubs.

    Returns:
        A list of zone names representing the optimal path (inclusive of
        start and end), or an empty list if the end is unreachable.
    """
    start: Zone = graph.zones[graph.start_hub]
    end_name: str = graph.end_hub

    queue: list[tuple[int, Zone]] = [(0, start)]
    paths: dict[str, list] = graph.set_zones_to_inf()
    paths[start.name] = [0, []]

    while queue:
        current_distance, current_zone = heapq.heappop(queue)

        if current_zone.name == end_name:
            return paths[end_name][1] + [end_name]

        if current_distance > paths[current_zone.name][0]:
            continue  # Stale heap entry, skip

        for neighbor in graph.get_neighbors(current_zone):
            distance = current_distance + neighbor.get_cost()
            if distance < paths[neighbor.name][0]:
                paths[neighbor.name][0] = distance
                paths[neighbor.name][1] = (
                    paths[current_zone.name][1] + [current_zone.name]
                )
                heapq.heappush(queue, (distance, neighbor))

    return []
