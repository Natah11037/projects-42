#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.plant_age = age

    def grow(self):
        self.height = self.height + 1

    def age(self):
        self.plant_age = self.plant_age + 1
        self.grow()

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    hibiscus = Plant("Hibiscus", 80, 4)
    rhododendron = Plant("Rhododendron", 350, 6)
    iris = Plant("Iris", 50, 2)
    plants = [hibiscus, rhododendron, iris]
    total_growth = 0
    print("=== Day 1 ===")
    for p in plants:
        p.get_info()
    for _ in range(6):
        total_growth += 1
        for p in plants:
            p.age()
    print("=== Day 7 ===")
    for p in plants:
        p.get_info()
    print(f"Growth this week: +{total_growth}cm")
