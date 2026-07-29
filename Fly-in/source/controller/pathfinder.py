from .graph import Graph
import heapq


def pathfinder(graph: Graph):
    queue = []
    visited = set()
    start = graph.zones[graph.data["start_hub"]["name"]]
    end = graph.data["end_hub"]["name"]
    queue.append((0, start))
    visited.add(start)
    paths = graph.set_zones_to_inf()
    heapq.heapify(queue)
    while queue:
        current_distance, current_zone = heapq.heappop(queue)
        if current_zone == graph.zones[end]:
            return (f"{paths[end][1] + [end]}\n\nTotal cost: {paths[end][0]}")

        for neighbor in graph.get_neighbors(current_zone):
            distance = current_distance + neighbor.get_cost()
            if distance < paths[neighbor.name][0]:
                paths[neighbor.name][0] = distance
                paths[neighbor.name][1] = paths[current_zone.name][
                    1] + [current_zone.name]
                heapq.heappush(queue, (distance, neighbor))
    return (f"{paths[end][1] + [end]}\n\nTotal cost: {paths[end][0]}")
