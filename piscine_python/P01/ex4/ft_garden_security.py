#!/usr/bin/env python3

class Plant:
    """Create a plant with a name, a height, and an age"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize the plant with its basic information"""
        self.name = name.capitalize()
        self.__height = height
        self.__plant_age = age

    def set_height(self, height):
        """Update the plant height if the value is valid"""
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        """Update the plant age if the value is valid"""
        if age > 0:
            self.__plant_age = age
            print(f"Age updated: {self.__plant_age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        """Return the plant age"""
        return self.__plant_age

    def get_height(self):
        """Return the plant height"""
        return self.__height

    def get_info(self):
        """Return the plant name, height, and age"""
        return f"{self.name} ({self.__height}cm, {self.__plant_age} days)"


if __name__ == "__main__":
    plant = Plant("Rose", 50, 240)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(65)
    plant.set_age(97)
    print("")
    plant.set_height(-5)
    print("")
    print(f"Current plant: {plant.get_info()}")
