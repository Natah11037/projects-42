#!/usr/bin/env python3


import sys


def display_inventory(inventory: dict) -> None:
    print("=== Current Inventory ===")
    all_units: int = sum(inventory.values())
    for loot in inventory:
        if inventory[loot] > 1:
            print(
                f"{loot}: {inventory[loot]} units "
                f"({inventory[loot] * 100 / all_units:.1f}%)"
            )
        elif inventory[loot] == 1:
            print(
                f"{loot}: {inventory[loot]} unit "
                f"({inventory[loot] * 100 / all_units:.1f}%)"
            )


def statistic_inv(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    most_item: str | None = None
    most_quantity: int = 0
    least_item: str | None = None
    least_quantity: float = float("inf")
    for item, quantity in inventory.items():
        if quantity > most_quantity:
            most_item = item
            most_quantity = quantity
        if quantity < least_quantity:
            least_item = item
            least_quantity = quantity
    if most_item is None and least_item is None:
        print("Most abundant: None items in inventory")
        print("Least abundant: None items in inventory")
    else:
        print(f"Most abundant: {most_item} ({most_quantity})")
        print(f"Least abundant: {least_item} ({least_quantity})")
    print("\n=== Item Categories ===")
    moderate: dict = {}
    scarce: dict = {}
    for item, quantity in inventory.items():
        if quantity < 4:
            scarce.update({item: quantity})
        else:
            moderate[item] = quantity
    if moderate:
        print(f"Moderate: {moderate}")
    else:
        print(
            "There is not any item of the rarity 'Moderate' "
            "in your inventory"
        )
    if scarce:
        print(f"Scarce: {scarce}")
    else:
        print(
            "There is not any item of the rarity 'Scarce' " "in your inventory"
        )
    print("\n=== Management Suggestions ===")
    scarce_names: list = list(scarce.keys())
    print(f"Restock needed: {scarce_names}")
    print("\n=== Dictionary Properties Demo ===")
    keys_string: str = ", ".join(inventory.keys())
    print(f"Dictionary keys: {keys_string}")
    values_string: str = ", ".join(str(v) for v in inventory.values())
    print(f"Dictionary values: {values_string}")
    print(f"Sample lookup - 'Kevin_clone' in inventory: {inventory.get(
                                                        "Kevin_clone")}")


if __name__ == "__main__":
    inventory: dict = {}
    for arg in sys.argv[1:]:
        item_args: list[str] = arg.split(":")
        if len(item_args) == 2:
            item_name: str = item_args[0]
            try:
                quantity = int(item_args[1])
                if quantity > 0:
                    inventory[item_name] = quantity
            except ValueError:
                print(
                    f"Error: not an available quantity for '{item_name}'"
                    f" nombre"
                )
    display_inventory(inventory)
    statistic_inv(inventory)
