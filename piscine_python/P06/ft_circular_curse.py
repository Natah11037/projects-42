def ingredient_validation(ingredient: str):
    from alchemy.grimoire.validator import validate_ingredients
    return (f'validate_ingredients("{ingredient}"):'
            f' {validate_ingredients(ingredient)}')


def spell_recording(spell_name: str, ingredient: str):
    from alchemy.grimoire.spellbook import record_spell
    return (f'record_spell("{spell_name}", "{ingredient}"):'
            f' {record_spell(spell_name, ingredient)}')


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    test_1 = "fire air"
    test_2 = "dragon scales"
    print(ingredient_validation(test_1))
    print(ingredient_validation(test_2))

    print("\nTesting spell recording with validation:")
    test_3_1 = "Fireball"
    test_3_2 = "fire air"
    print(spell_recording(test_3_1, test_3_2))
    test_4_1 = "Dark Magic"
    test_4_2 = "shadow"
    print(spell_recording(test_4_1, test_4_2))

    print("\nTesting late import technique:")
    test_5_1 = "Lightning"
    test_5_2 = "air"
    print(spell_recording(test_5_1, test_5_2))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
