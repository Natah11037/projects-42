from collections.abc import Callable
import random
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:

    def accumulator(new_power: int):
        nonlocal initial_power
        initial_power += new_power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def putting_enchants(equipment: str):
        return f"{enchantment_type} {equipment}"
    return putting_enchants


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: Any, value: Any):
        storage[key] = value

    def recall(key: Any) -> Any | str:
        return storage.get(key, 'Memory not found')
    return {"store": store, "recall": recall}


def main():
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    for _ in range(4):
        print(f"counter_a call: {counter_a()}")
    counter_b = mage_counter()
    for _ in range(2):
        print(f"counter_b call: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = spell_accumulator(10)
    data = [
        17,
        7,
        4,
        23,
        6
    ]
    for i in range(len(data)):
        print(f"Actual power: {base(data[i])}")

    print("\nTesting enchantment factory...")
    equipments = [
        "sword",
        "spear",
        "shield",
        "armor",
        "boots",
        "hammer",
        "great sword",
        "knife",
        "hemlet",
        "assault rifle"
    ]
    enchants = [
        "Flaming",
        "Frozen",
        "Mysterious",
        "Molten",
        "Stormforged",
        "Shocking",
        "Infernal",
        "Runed",
        "Forbidden",
        "Ethereal"
    ]
    enchant_equipment_1 = enchantment_factory(random.choice(enchants))
    enchant_equipment_2 = enchantment_factory(random.choice(enchants))
    enchanted_1 = enchant_equipment_1(random.choice(equipments))
    enchanted_2 = enchant_equipment_2(random.choice(equipments))
    print(f"{enchanted_1}\n{enchanted_2}")

    print("\nTesting Memory Vault...")
    storage = memory_vault()
    storage["store"]("secret", 42)
    print("Store 'secret' = 42")
    recall_func = storage["recall"]("secret")
    print(f"Recall 'secret': {recall_func}")
    recall_func_2 = storage["recall"]("unknown")
    print(f"Recall 'unknown': {recall_func_2}")


if __name__ == "__main__":
    main()
