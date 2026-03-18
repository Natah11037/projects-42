def method_1():
    import alchemy
    return (f"alchemy.elements.create_fire(): "
            f"{alchemy.elements.create_fire()}\n")


def method_2():
    from alchemy.elements import create_water
    return (f"create_water(): {create_water()}")


def method_3():
    from alchemy.potions import healing_potion as heal
    return (f"heal(): {heal()}")


def method_4():
    from alchemy.potions import strength_potion
    from alchemy.elements import create_fire, create_earth
    return (f"create_earth(): {create_earth()}\n"
            f"create_fire(): {create_fire()}\n"
            f"strength_potion(): {strength_potion()}")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(method_1())

    print("Method 2 - Specific function import:")
    print(method_2())

    print("\nMethod 3 - Aliased import:")
    print(method_3())

    print("\nMethod 4 - Multiple imports:")
    print(method_4())

    print("\nAll import transmutation methods mastered!")
