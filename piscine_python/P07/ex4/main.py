from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
import random


def main():
    print("\n=== DataDeck Tournament Platform ===\n")
    management = TournamentPlatform()
    card_1 = TournamentCard(
        random.choice(
            [
                "goblin",
                "bowser",
                "xX_Toad_le_bg_Xx",
                "nathan weber le talentueux",
                "l'echarde dans le pied a cihan",
                "la trott de gautier",
                "copilot le retour",
                "fee a la fraise des bois",
                "Mr.Propre",
                "bulbizarre",
                "bout de carton mouille",
                "Professeur.Layton",
                "Hatsune Miku",
                "power ranger magenta",
                "Lionnel Messi",
                "Julien Song",
                "P05",
                "exam rank 02",
                "aquaman",
                "King Sloth",
                "Zeus, the almighty god of the god",
                "Time Keeper",
            ]
        ),
        random.randint(1, 10),
        random.choice(
            [
                "common",
                "uncommon",
                "rare",
                "epic",
                "legendary",
                "heroic",
                "iconic",
                "mythical",
            ]
        ),
        random.randint(1, 10),
    )

    card_2 = TournamentCard(
        random.choice(
            [
                "goblin",
                "bowser",
                "xX_Toad_le_bg_Xx",
                "nathan weber le talentueux",
                "l'echarde dans le pied a cihan",
                "la trott de gautier",
                "copilot le retour",
                "fee a la fraise des bois",
                "Mr.Propre",
                "bulbizarre",
                "bout de carton mouille",
                "Professeur.Layton",
                "Hatsune Miku",
                "power ranger magenta",
                "Lionnel Messi",
                "Julien Song",
                "P05",
                "exam rank 02",
                "aquaman",
                "King Sloth",
                "Zeus, the almighty god of the god",
                "Time Keeper",
            ]
        ),
        random.randint(1, 10),
        random.choice(
            [
                "common",
                "uncommon",
                "rare",
                "epic",
                "legendary",
                "heroic",
                "iconic",
                "mythical",
            ]
        ),
        random.randint(1, 10),
    )

    print("Registering Tournament Cards...\n")

    print(
        f"{card_1.name.capitalize()} " f"({management.register_card(card_1)}):"
    )
    stat_for_1 = card_1.get_tournament_stats()
    print(f"- Interfaces: {stat_for_1['interfaces']}")
    print(f"- Rating: {stat_for_1['rating']}")
    print(f"- Record: {stat_for_1['record']}\n")

    print(
        f"{card_2.name.capitalize()} " f"({management.register_card(card_2)}):"
    )
    stat_for_2 = card_2.get_tournament_stats()
    print(f"- Interfaces: {stat_for_2['interfaces']}")
    print(f"- Rating: {stat_for_2['rating']}")
    print(f"- Record: {stat_for_2['record']}\n")

    print("Creating tournament match...")
    match_annoucements = management.create_match(
        card1_id=f"{card_1.name.lower()}_001",
        card2_id=f"{card_2.name.lower()}_001",
    )
    print("\n", match_annoucements["first"], end=" | ")
    print(match_annoucements["type"], end=" | ")
    print(match_annoucements["second"], "\n")

    print(f"Match result: {card_1.attack(card_2)}\n")

    print("Tournament Leaderboard:")
    top = management.get_leaderboard()
    for i, card in enumerate(top, start=1):
        print(f"{i}. {card.name} - Rating: {card.rate} "
              f"({card.win}-{card.loose})")

    print("\nPlatform Report:")
    print(management.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!\n")


if __name__ == "__main__":
    main()
