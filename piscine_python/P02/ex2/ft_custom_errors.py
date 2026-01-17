#!usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, height: int, water: int) -> None:
        self.name = name.title()
        self.height = height
        self.water = water

    def water(self) -> None:
        self.water = 0

    def check(self) -> None:
        if self.water > 3:
            raise PlantError(f"Caught PlantError: The {self.name} "
                             f"plant is wilting!")