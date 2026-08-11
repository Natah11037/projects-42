from .controller.graph import Graph
from .parsing.parser import Parser
from .controller.pathfinder import pathfinder


if __name__ == "__main__":
    parsed = Parser("./assets/maps/challenger/01_the_impossible_dream.txt")
    parsed.parse()
    graph = Graph(parsed.data)
    print(pathfinder(graph))
