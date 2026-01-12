#!/usr/bin/env python3

class Plant:
    """Create a plant with a name, a height, and an age"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize the plant with its basic information"""
        self.name = name.capitalize()
        self.height = height
        self.plant_age = age

    def grow(self):
        """Increase the plant height by 1 cm"""
        self.height = self.height + 1

    def age(self):
        """Increase the plant age by 1 day"""
        self.plant_age = self.plant_age + 1

    def get_info(self):
        """Print the plant name, height, and age"""
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    hibiscus = Plant("Hibiscus", 80, 748)
    rhododendron = Plant("Rhododendron", 350, 1465)
    iris = Plant("Iris", 50, 456)
    plants = [hibiscus, rhododendron, iris]
    total_growth = 0
    print("=== Day 1 ===")
    for p in plants:
        p.get_info()
    for _ in range(6):
        total_growth += 1
        for p in plants:
            p.age()
            p.grow()
    print("=== Day 7 ===")
    for p in plants:
        p.get_info()
    print(f"Growth this week: +{total_growth}cm")
