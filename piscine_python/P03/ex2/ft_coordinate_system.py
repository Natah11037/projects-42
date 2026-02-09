#!/usr/bin/env python3

import math
import sys


def parsing(user_co: str) -> tuple[int, ...] | None:
    working_co: list[int] = []
    splited_co: list[str] = user_co.split(",")
    if len(splited_co) != 3:
        print(f"Parsing invalid coordinates: {user_co}")
        print("Error parsing coordinates: expected exactly # values  (x,y,z)")
        return None
    try:
        for co in splited_co:
            co = int(co)
            working_co.append(co)
    except ValueError as e:
        print(f"Parsing invalid coordinates: {user_co}")
        print(f"Error parsing coordinate: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return (None)
    print(f'Parsing coordinates: "{user_co}"')
    return tuple(working_co)


def distance_between(first_co: tuple, second_co: tuple):
    x1, y1, z1 = first_co
    x2, y2, z2 = second_co

    return (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def coordinates(positions: tuple, positions2: tuple):
    print(f"Position created: {positions}")
    print(f"Distance between {positions2} and {positions}:"
          f" {distance_between(positions, positions2):.2f}")


if __name__ == "__main__":
    try:
        position = sys.argv[1]
    except IndexError:
        print('Please consider putting an arguments (example: "3,4,5")')
        sys.exit(1)
    print("=== Game Coordinate System ===\n")
    try:
        position2 = sys.argv[2]
        pos2 = parsing(position2)
    except IndexError:
        print("No 2nd arguments, set by default at 0 0 0")
        pos2 = (0, 0, 0)
    finally:
        print(f"Parsed position: {pos2}\n")
    pos = parsing(position)
    if not pos:
        sys.exit(1)
    print(f"Parsed position: {pos}\n")
    coordinates(pos, pos2)
