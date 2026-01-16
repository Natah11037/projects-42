#!/usr/bin/env python3

class Plant:
    """Create a plant with a name, a height, and an age"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize the plant with its basic information"""
        self.name = name.capitalize()
        self.height = height
        self.plant_age = age

    def get_info(self):
        """Print the plant creation information"""
        print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")


if __name__ == "__main__":
    total_plants = 0
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = [Plant(n, h, a) for n, h, a in plant_data]
    for p in plants:
        p.get_info()
    print("")
    print("Total plants created: ", len(plants))
