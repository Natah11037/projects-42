#!/usr/bin/env python3

def check_temperatures(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number ❌\n")
    else:
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants 🥶(min 0°C)")
        elif temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants 🥵(max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!🌺\n")


def test_temperature_input() -> None:
    print("=☀️ = Garden Temperature Checker =❄️ =\n")
    for _ in range(5):
        try:
            temperature: str = input("Enter a temperature: ")
            check_temperatures(temperature)
        except ValueError as error:
            print(f"Error: {error}\n")

    print("All tests completed - program didn't crash!✨")


if __name__ == "__main__":
    test_temperature_input()
