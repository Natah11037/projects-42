#!/usr/bin/env python3

class Plant:
    """
    Create a class plant which contain data
    """

    def __init__(self, name: str, height: int, age: int):
        """Initiate the data of the plant

        Args:
            name (str): name of the plant
            height (int): height of the plant
            age (int): age of the plant
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def print_plants(self):
        """Print the data of the plant

        Returns:
            str: data of the plant
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    hibiscus = Plant("Hibiscus", 80, 748)
    rhododendron = Plant("Rhododendron", 350, 1465)
    iris = Plant("Iris", 50, 456)
    print("=== Garden Plant Registry ===")
    hibiscus.print_plants()
    rhododendron.print_plants()
    iris.print_plants()
