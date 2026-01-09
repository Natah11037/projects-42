#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.__height = height
        self.__plant_age = age

    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {self.__height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {self.__age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_info(self):
        return (f"{self.name} ({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    plant = Plant("Rose", 50, 240)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-5)
    print("")
    print(f"Current plant: {plant.get_info()}")
