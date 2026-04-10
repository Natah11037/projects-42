from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = 0

    def accumulator():
        nonlocal power
        power += initial_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def memory_vault() -> dict[str, Callable]:
    pass


def main():
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    for _ in range(4):
        print(f"counter_a call: {counter_a()}")
    counter_b = mage_counter()
    for _ in range(2):
        print(f"counter_a call: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = spell_accumulator(20)
    for _ in range(4):
        print(f"Actual power: {base()}")


if __name__ == "__main__":
    main()
