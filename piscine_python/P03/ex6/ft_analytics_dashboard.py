#!/usr/bin/env python3


def list_comprehension(players_info: dict) -> list:
    list_high_scores = [
        name for name, score in players_info.items() if score > 2000
    ]
    print(f"High scorers (>2000): {list_high_scores}")
    list_doubled = [score * 2 for score in players_info.values()]
    print(f"Scores doubled: {list_doubled}")
    list_active = [
        name for name, score in players_info.items() if score > 2500
    ]
    print(f"Active players: {list_active}")


def dict_comprehension(players_info: dict) -> dict:
    dict_scores = {player: score for player, score in players_info.items()}
    print(f"Player scores: {dict_scores}")
    dict_scores_status = {
        "high": len([score for score in players_info.values()
                    if score > 2500]),
        "medium": len([score for score in players_info.values()
                      if score <= 2500 and score > 1500]),
        "low": sum(1 for score in players_info.values() if score <= 1500)
    }
    print(f"Score categories: {dict_scores_status}")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players = {
        "Cihan": 2607,
        "Gautier": 1956,
        "Kevin": 254,
        "Nathan": 4139
        }
    list_comprehension(players)
    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(players)
