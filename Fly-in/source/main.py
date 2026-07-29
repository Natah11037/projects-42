from .controller.graph import Graph
from .parsing.parser import Parser
from .controller.pathfinder import pathfinder


if __name__ == "__main__":
    parsed = Parser("./assets/maps/easy/01_linear_path.txt")
    parsed.parse()
    graph = Graph(parsed.data)
    print(pathfinder(graph))
