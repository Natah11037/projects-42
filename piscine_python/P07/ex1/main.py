from ex0 import CreatureCard
from ex1 import ArtifactCard

from .SpellCard import SpellCard
from .Deck import Deck

import click


def main():
    all_card = Deck()
    my_deck = Deck()
    enemy_deck = Deck()
    game_state = {
        "player": "Natah",
        "mana": 100
    }

    # SpellCard
    cards = [
        SpellCard("Lightning", 15, "common", "damage"),
        SpellCard("Heal", 30, "rare", "heal"),
        SpellCard("Speed Boost", 25, "uncommon", "buff"),
        SpellCard("Stone Curse", 35, "epic", "debuff"),
        SpellCard("Burn", 15, "common", "damage"),
        SpellCard("Freeze", 30, "rare", "debuff"),
        SpellCard("Strength Boost", 25, "uncommon", "buff"),
        SpellCard("Poison", 25, "rare", "debuff"),
        SpellCard("Flowering", 40, "rare", "heal"),
        SpellCard("Explosion", 30, "uncommon", "damage"),
        # ArtifactCard
        ArtifactCard(
            "Water Field",
            40,
            "rare",
            3,
            "submerge the field" "with water which heal all allies each turn",
        ),
        ArtifactCard(
            "Lava Field",
            50,
            "epic",
            3,
            "Lava flood the field,"
            " every target who get hit take x1,5 more damage",
        ),
        ArtifactCard(
            "Cloudy Field",
            35,
            "uncommon",
            4,
            "Every "
            "card goes in the sky, every target have 20% to miss"
            " their attack",
        ),
        ArtifactCard(
            "Venom Field",
            30,
            "rare",
            6,
            "inflict damage to " "every card each turn",
        ),
        ArtifactCard(
            "Night City",
            75,
            "legendary",
            1,
            "Welcome "
            "in Night City, The City of Dreams. in this field your strongest"
            " card became a cyberpsychos and enrage. double damage,"
            " double life and attack in first for one turn",
        ),
        # CreatureCard
        CreatureCard(
            "King Sloth",
            45,
            "rare",
            3,
            16,
        ),
        CreatureCard("Goblin", 10, "common", 2, 5),
        CreatureCard("Cute Kitty", 25, "epic", 8, 8),
        CreatureCard("Slime", 15, "uncommon", 1, 6),
        CreatureCard("Flying Robotic Shark", 60, "legendary", 10, 15),
    ]

    for card in cards:
        all_card.add_card(card)

    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    print(f"Deck stats: {all_card.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    for _ in range(3):
        all_card.shuffle()
        card = all_card.draw_card()
        print(f"Drew: {card.name} ({card.__class__.__name__}) for enemy\n")
        enemy_deck.add_card(card)
        all_card.shuffle()
        card = all_card.draw_card()
        print(f"Drew: {card.name} ({card.__class__.__name__}) for me\n")
        my_deck.add_card(card)

    game_state["my_deck"] = my_deck.list_card
    game_state["enemy_deck"] = enemy_deck.list_card

    print("RESULT:\n")

    print("My Deck:\n")
    for card in game_state["my_deck"]:
        print(f"- {card.name}")

    print("\nEnemy Deck:\n")
    for card in game_state["enemy_deck"]:
        print(f"- {card.name}")

    print("\nTime to Play:\n")

    for card in game_state["my_deck"]:
        print(card.play(game_state))


if __name__ == "__main__":
    main()
