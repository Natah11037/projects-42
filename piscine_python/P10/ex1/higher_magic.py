from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"fireball threw at {target} and dealt {power} damages"


def fire(power: int) -> int:
    return power


def heavy(target: str, power: int) -> str:
    return f"Heavy add a magical weight of {power} pounds to {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1):
        raise TypeError("spell1 object need to be a callable")
    if not callable(spell2):
        raise TypeError("spell2 object need to be a callable")

    def combine(*args):
        return (spell1(*args), spell2(*args))
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell object need to be a callable")
    if not isinstance(multiplier, int):
        raise TypeError("multiplier object need to be an integer")

    def amplifie(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplifie


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition):
        raise TypeError("condition object need to be a callable")
    if not callable(spell):
        raise TypeError("spell object need to be a callable")

    def cast_if(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return cast_if


def spell_sequence(spells: list[Callable]) -> Callable:
    if not isinstance(spells, list) or not all(callable(s) for s in spells):
        raise TypeError("spells object need to be a list of Callable")

    def cast(*args, **kwargs):
        all_spells = []
        for spell in spells:
            all_spells.append(spell(*args, **kwargs))
        return all_spells
    return cast


def more_than_4(target: str, power: int) -> bool:
    return power > 4


def main():

    power = 5
    target = "goblin"
    try:
        combined_spell = spell_combiner(fireball, heavy)
    except TypeError as e:
        print(f"\n{e}\n")
        exit(1)
    result_combined = combined_spell(target, power)

    print("\nTesting spell combiner...")
    len_res = len(result_combined)
    print("Combined spell result: ", end="")
    for res in result_combined:
        if len_res > 1:
            print(f"{res}, ", end="")
        else:
            print(res)
        len_res += -1

    try:
        amplified_spell = power_amplifier(fire, 3)
    except TypeError as e:
        print(f"\n{e}\n")
        exit(1)
    new_power = amplified_spell(power)
    result_amplifier = fireball(target, new_power)

    print("\nTesting power amplifier...")
    print(f"{result_amplifier} instead of {fireball('goblin', 5)}")

    try:
        conditionned_spell = conditional_caster(more_than_4, fireball)
    except TypeError as e:
        print(f"\n{e}\n")
        exit(1)
    result_conditional = conditionned_spell(target, power)

    print("\nTesting conditional caster...")
    print(result_conditional)

    try:
        sequence_of_spells = spell_sequence([fireball, heal, heavy])
    except TypeError as e:
        print(f"\n{e}\n")
        exit(1)
    result_sequenced = sequence_of_spells(target, power)

    print("\nTesting spell sequence...")
    len_sequence = len(result_sequenced)
    for spell in result_sequenced:
        if len_sequence > 1:
            print(f"{spell}, ", end="")
        else:
            print(spell)
        len_sequence += -1


if __name__ == "__main__":
    main()
