#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def print_plants(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    hibiscus = Plant("Hibiscus", 80, 4)
    rhododendron = Plant("Rhododendron", 350, 6)
    iris = Plant("Iris", 50, 2)
    print("=== Garden Plant Registry ===")
    hibiscus.print_plants()
    rhododendron.print_plants()
    iris.print_plants()
