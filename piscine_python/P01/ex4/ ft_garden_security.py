#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.__height = height
        self.__plant_age = age

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("The height must be a positive value")

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("The age must be a positive value")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")


if __name__ == "__main__":
    plant = Plant("Sunflower", 50, 147)