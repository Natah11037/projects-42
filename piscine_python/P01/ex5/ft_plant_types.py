#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        return (f"{self.name} ({self.__height}cm, {self.__age} days)")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return (f"{self.name} is blooming beautifully!")

    def get_info(self):
        return (f"{self.name} (Flower): {self.height}cm, {self.age} days,"
                f" {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.diam = trunk_diameter

    def produce_shade(self):
        return (f"{self.name} provides {self.height / self.diam * 7.8}"
                f" square meters of shade")

    def get_info(self):
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days,"
                f" {self.diam}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutritional = nutritional_value

    def get_info(self):
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} "
                f"days, {self.season} harvest")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    iris = Flower("Iris", 50, 321, "purple")
    oak = Tree("Oak", 500, 1825, 50)
    palm = Tree("Palm Tree", 400, 700, 210)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 326, 411, "winter", "vitamin A")
    print("=== Garden Plant Types ===")
    print("")
    print(rose.get_info())
    print(rose.bloom())
    print("")
    print(oak.get_info())
    print(oak.produce_shade())
    print("")
    print(tomato.get_info())
    print(f"{tomato.name} is rich in {tomato.nutritional}")