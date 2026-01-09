#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int):
        self.name = name.capitalize()
        self.height = height
        self.total_growth = 0

    def get_info(self):
        return (f"{self.name}: {self.__height}cm")

    def grow(self):
        self.height = self.height + 1
        self.total_growth += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, score: int):
        super().__init__(name, height, color)
        self.score = score

    def get_info(self):
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming), "
                f"Prize points: {self.score}")


class GardenManager:
    def __init__(self, name: str, plants: list[Plant] = None):
        self.name = name.capitalize()
        if plants is None:
            plants = []
        self.plants = plants
    
    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        return (f"Added {plant.name} to {self.name}'s garden")

    def grow(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print("")

    class GardenStats