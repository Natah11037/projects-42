from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    supported = {"add": add, "multiply": mul, "max": max, "min": min}
    if operation in supported:
        r = reduce(supported.get(operation), spells)
        return r
    raise ValueError(f"Error: {operation} variable is not a supported "
                     "operation")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"adding {element} enchant to {target} resulting a power of {power}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Flaming"),
        "ice": partial(base_enchantment, 50, "Frozen"),
        "lightning": partial(base_enchantment, 50, "Shocking")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell):
        return "Unknown spell type"

    @cast_spell.register
    def _(spell: int):
        return f"{spell} damage"

    @cast_spell.register
    def _(spell: str):
        return spell

    @cast_spell.register
    def _(spell: list):
        res = []
        for s in spell:
            res.append(cast_spell(s))
        return res

    return cast_spell


def main():
    print("\nTesting spell reducer...")
    nbr = [17, 81, 21, 12]
    try:
        print(f"Sum: {spell_reducer(nbr, 'add')}")
        print(f"Product: {spell_reducer(nbr, 'multiply')}")
        print(f"Max: {spell_reducer(nbr, 'max')}")
        print(f"Min: {spell_reducer(nbr, 'min')}")
    except ValueError as e:
        print(e)
    except TypeError:
        print("Error: please consider putting the two argument: "
              "spells, operation")

    print("\nTesting partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(enchant["fire"]("Sword"))
    print(enchant["ice"]("Shield"))
    print(enchant["lightning"]("Spear"))

    print("\nTesting memoized fibonacci...")
    i = 8
    print(f"Fib({i}): {memoized_fibonacci(i)}")
    print(f"Info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f"Damage spell: {dispatch(42)}")
    print(f"Enchantment: {dispatch('fireball')}")
    print(f"Multi-cast: {len(dispatch([50, 'poison', 1]))} spells")
    print(f"{dispatch({'name': 'Natah'})}")


if __name__ == "__main__":
    main()
