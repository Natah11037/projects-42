#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name:
        print("Testing empty plant name...")
        raise ValueError("Error: Plant name cannot be empty!\n")
    if not 0 < water_level < 11:
        print("Testing bad water level...")
        raise ValueError(f"Error: Water level {water_level} is too high "
                         f"(max 10)\n")
    if sunlight_hours < 2:
        print("Testing bad sunlight hours...")
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low "
                         f"(min 2)\n")
    elif sunlight_hours > 12:
        print("Testing bad sunlight hours...")
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too much "
                         f"(max 12)\n")
    if plant_name and 0 < water_level < 11 and 12 > sunlight_hours > 1:
        print(f"Plant '{plant_name}' is healthy!\n")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 9, 3)
    except ValueError as error:
        print(error)
    try:
        check_plant_health(None, 9, 3)
    except ValueError as error:
        print(error)
    try:
        check_plant_health("carrot", 15, 9)
    except ValueError as error:
        print(error)
    try:
        check_plant_health("lettuce", 9, 0)
    except ValueError as error:
        print(error)
    print("All error raising tests completed!")
