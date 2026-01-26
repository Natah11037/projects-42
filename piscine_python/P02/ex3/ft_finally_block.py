#!usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if not plant:
            raise ValueError(f"Error: Cannot water {plant} - invalid plant!")
        else:
            print(f"Watering {plant}")


def test_watering_system() -> None:
    good_list = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    wrong_list = [
        "tomato",
        None,
        "lettuce",
        "carrots"
    ]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        water_plants(good_list)
    except ValueError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")
    print("Testing with error...")
    try:
        water_plants(wrong_list)
    except ValueError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
