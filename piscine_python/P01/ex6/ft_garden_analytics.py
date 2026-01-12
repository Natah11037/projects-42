#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int):
        self.name = name.capitalize()
        self.height = height
        self.count_growth = 0

    def get_info(self):
        return (f"{self.name}: {self.height}cm")

    def grow(self):
        self.height = self.height + 1
        self.count_growth += 1


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

    def growth_all(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")
        print("")

    def garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print("")

    def height_validation(self):
        for plant in self.plants:
            if plant.height > 0:
                return ("Height validation test: True")
            else:
                return ("Height validation test: False")

    class GardenStats:
        @staticmethod
        def count_plant(plants):
            return (len(plants))

        @staticmethod
        def total_grow(plants):
            total_growth = 0
            for plant in plants:
                total_growth = total_growth + plant.count_growth
            return (total_growth)

        @staticmethod
        def count_plant_type(plants):
            regular = 0
            flowering = 0
            prize_flowers = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize_flowers += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1
            return (f"Plants types: {regular} regular, {flowering} flowering,"
                    f" {prize_flowers} prize flowers")

        def count_score(plants):
            total_score = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_score += plant.score
            return (total_score)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    oak = Plant("Oak", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice = GardenManager("Alice")
    print(alice.add_plant(oak))
    print(alice.add_plant(rose))
    print(alice.add_plant(sunflower))
    print("")
    alice.growth_all()
    alice.garden_report()
    print(f"Plants added: {alice.GardenStats.count_plant(alice.plants)},"
          f" Total growth: {alice.GardenStats.total_grow(alice.plants)}cm")
    print(alice.GardenStats.count_plant_type(alice.plants))
    print(alice.height_validation())
    print(alice.GardenStats.count_score(alice.plants))