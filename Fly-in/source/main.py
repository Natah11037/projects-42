from .controller.graph import Graph
from .parsing.parser import Parser


if __name__ == "__main__":
    parsed = Parser("./assets/maps/easy/01_linear_path.txt")
    parsed.parse()
    graph = Graph(parsed.data)
    print(graph.get_neighbors(graph.zones["waypoint1"]))
