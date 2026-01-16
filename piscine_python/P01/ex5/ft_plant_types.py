#!/usr/bin/env python3

class Plant:
    """Create a plant with a name, a height, and an age"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize the plant with its basic information"""
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        """Return the plant name, height, and age"""
        return f"{self.name} ({self.height}cm, {self.age} days)"


class Flower(Plant):
    """Create a flower with a color in addition to plant information"""

    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize the flower with its basic information and color"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Return a message showing the flower is blooming"""
        return f"{self.name} is blooming beautifully!"

    def get_info(self):
        """Return the flower name, height, age, and color"""
        return (f"{self.name} (Flower): {self.height}cm, {self.age} days, "
                f"{self.color} color")


class Tree(Plant):
    """Create a tree with a trunk diameter in addition to plant information"""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initialize the tree with its basic information and trunk diameter"""
        super().__init__(name, height, age)
        self.diam = trunk_diameter

    def produce_shade(self):
        """Return the amount of shade produced by the tree"""
        return (f"{self.name} provides {self.height / self.diam * 7.8}"
                f" square meters of shade")

    def get_info(self):
        """Return the tree name, height, age, and trunk diameter"""
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.diam}cm diameter")


class Vegetable(Plant):
    """Create a vegetable with a harvest season and a nutritional
       value in addition to plant information"""

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
