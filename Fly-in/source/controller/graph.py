from .models import Zone, Connection
from ..parsing.parser import Parser


class Graph():
    def __init__(self, data: dict):
        self.data = data
