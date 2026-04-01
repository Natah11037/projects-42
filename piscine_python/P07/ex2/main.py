from .EliteCard import EliteCard
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


def main():
    print("=== DataDeck Ability System ===\n")

    game_state = {
        "player": "Natah",
        "mana": 100
    }
    doomfist = EliteCard("Doomfist", 50, "legendary", 525, 36, 30, 10)
    roadhog = EliteCard("Roadhog", 50, "legendary", 750, 94, 40, 10)
    enemy_double_tank = [doomfist, roadhog]

    print("EliteCard capabilities:")
    print([method for method in dir(Card) if not method.startswith("__")
           and method != '_abc_impl'])
    print([method for method in dir(Combatable) if not method.startswith("__")
           and method != '_abc_impl'])
    print([method for method in dir(Magical) if not method.startswith("__")
           and method != '_abc_impl'], "\n")

    print("Playing Arcane Warrior (Elite Card):\n")

    roadhog.play(game_state)

    print("Combat phase:")
    print(f"Attack result: {roadhog.attack(doomfist)}")
    print(f"Defense result: {roadhog.defend(doomfist.damage)}")

    print("\nMagic phase:")
    print(f"Spell cast: {roadhog.cast_spell('chain hook', enemy_double_tank)}")
    amount_for_channeled = 4
    print(f"Mana channel: {roadhog.channel_mana(amount_for_channeled)}")
    game_state["mana"] = game_state["mana"] - amount_for_channeled

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
