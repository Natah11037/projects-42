from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    try:
        rebecca = CreatureCard("Rebecca", 75, "iconic", 7, 5)

        print(f"CreatureCard Info:\n{rebecca.get_card_info()}\n")

        game_state = {"player": "Natah", "mana": 100}

        print(f"Playing {rebecca.name} with"
              f" {game_state['mana']} mana available:")
        print(f"Playable: {rebecca.is_playable(game_state['mana'])}")
        print(f"Play result: {rebecca.play(game_state)}\n")

        cyberpsycho = "cyberpsycho"
        print(f"{rebecca.name} attacks {cyberpsycho}:")
        print(rebecca.attack_target(cyberpsycho))

        print(f"\nTesting insufficient mana ({game_state['mana']} available):")
        print(f"Playable: {rebecca.is_playable(game_state['mana'])}\n")
    except AttributeError as e:
        print(e)

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
