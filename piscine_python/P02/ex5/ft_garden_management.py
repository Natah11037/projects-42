#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.count_growth = 0
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(
        self, name: str, water_in_tank: int, plants: list[Plant] = None
    ):
        self.name = name
        if plants is None:
            plants = []
        self.plants = plants
        self.water_in_tank = water_in_tank

    def water_plants(self, plants: list[Plant]) -> None:
        print("Opening watering system")
        for plant in plants:
            if not plant:
                raise ValueError(
                    f"Error: Cannot water {plant} - invalid plant!"
                )
            else:
                print(f"Watering {plant.name} - success")

    def add_plant(self, plant: Plant):
        if not plant:
            raise PlantError(
                "Error adding plant: Plant cannot be empty!\n"
            )
        elif not plant.name:
            raise PlantError(
                "Error adding plant: Plant name cannot be empty!\n"
            )
        else:
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")

    def check_plant_health(self, plants: list[Plant]) -> None:
        for plant in plants:
            if not 0 < plant.water_level < 11:
                raise ValueError(
                    f"Error checking {plant.name}: Water level "
                    f"{plant.water_level} is too high (max 10)\n"
                )
            if plant.sunlight_hours < 2:
                raise ValueError(
                    f"Error checking {plant.name}: Sunlight hours "
                    f"{plant.sunlight_hours} is too low (min 2)\n"
                )
            if (
                plant.name
                and 0 < plant.water_level < 11
                and plant.sunlight_hours > 1
            ):
                print(
                    f"{plant.name}: healthy (water: "
                    f"{plant.water_level}, sun: {plant.sunlight_hours})"
                )


def test_garden_management():
    print("=== Garden Management System Demo ===\n")
    lettuce = Plant("lettuce", 15, 8)
    tomato = Plant("tomato", 5, 8)
    cihan = Plant("", 4, 4)
    natah = GardenManager("Natah", 13)

    print("Adding plants to garden...")
    try:
        natah.add_plant(tomato)
    except PlantError as e:
        print(e)
    try:
        natah.add_plant(lettuce)
    except PlantError as e:
        print(e)
    try:
        natah.add_plant(cihan)
    except PlantError as e:
        print(e)
    try:
        natah.add_plant(None)
    except PlantError as e:
        print(e)
    print("Watering plants...")
    try:
        natah.water_plants(natah.plants)
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)\n")
    print("Checking plant health...")
    try:
        natah.check_plant_health(natah.plants)
    except ValueError as e:
        print(e)
    print("Testing error recovery...")
    try:
        if natah.water_in_tank < 20:
            raise GardenError(
                "Caught WaterError: Not enough water in"
                " tank\nSystem recovered and continuing..."
            )
        elif natah.water_in_tank > 100:
            raise GardenError(
                "Caught WaterError: Too much water in"
                " tank\nSystem recovered and continuing..."
            )
        else:
            print("Didn't caught any errors\nSystem working fine")
    except GardenError as e:
        print(e)
    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
