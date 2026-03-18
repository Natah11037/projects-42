def absolute_import():
    from alchemy.transmutation.basic import stone_to_gem, lead_to_gold
    return (f"lead_to_gold(): {lead_to_gold()}\n"
            f"stone_to_gem(): {stone_to_gem()}")


def relative_imports():
    from alchemy.transmutation import elixir_of_life, philosophers_stone
    return (f"philosophers_stone(): {philosophers_stone()}\n"
            f"elixir_of_life(): {elixir_of_life()}")


def package_access():
    from alchemy.transmutation import lead_to_gold, philosophers_stone
    return (f"alchemy.transmutation.lead_to_gold(): {lead_to_gold()}\n"
            f"alchemy.transmutation.philosophers_stone(): "
            f"{philosophers_stone()}")


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(absolute_import())

    print("\nTesting Relative Imports (from advanced.py):")
    print(relative_imports())

    print("\nTesting Package Access:")
    print(package_access())

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
