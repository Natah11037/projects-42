#!/usr/bin/env python3


def list_comprehension(players_info: dict) -> list:
    list_high_scores = [
        name for name, data in players_info.items() if data["score"] > 2000
    ]
    print(f"High scorers (>2000): {list_high_scores}")
    list_doubled = [data["score"] * 2 for data in players_info.values()]
    print(f"Scores doubled: {list_doubled}")
    list_active = [
        name for name, data in players_info.items() if data["score"] > 2500
    ]
    print(f"Active players: {list_active}")


def dict_comprehension(players_info: dict) -> dict:
    dict_scores = {player: data["score"] for player, data in
                   players_info.items()}
    print(f"Player scores: {dict_scores}")
    dict_scores_status = {
        "high": len([data for data in players_info.values()
                     if data["score"] > 2500]),
        "medium": len([data for data in players_info.values()
                      if data["score"] <= 2500 and data["score"] > 1500]),
        "low": sum(1 for data in players_info.values()
                   if data["score"] <= 1500)
    }
    print(f"Score categories: {dict_scores_status}")
    dict_achievements = {player: len(data["achievements"]) for player, data
                         in players_info.items()}
    print(f"Achievement counts: {dict_achievements}")


def set_comprehension(players_info: dict) -> set:
    set_players = {name for name in players_info.keys()}
    print(f"Unique players: {set_players}")
    set_achievements = {
        achievement
        for name, data in players_info.items()
        for achievement in data["achievements"]
        }
    print(f"Unique achievements: {set_achievements}")


def analysis(players_info: dict) -> set:
    total_players = len(players_info)
    print(f"Total players: {total_players}")
    total_achievements = len({
        achievement
        for name, data in players_info.items()
        for achievement in data["achievements"]
        })
    print(f"Total unique achievements: {total_achievements}")
    average_score = {data["score"] for data in
                     players_info.values()}
    total = 0
    divide = 0
    for score in average_score:
        total += score
        divide += 1
    total = total / divide
    print(f"Average score: {total}")
    top_performer = max(players_info, key=lambda player:
                        players_info[player]["score"])
    print(f"Top performer: {top_performer}"
          f" ({players_info[top_performer]['score']} points,"
          f" {len(players_info[top_performer]['achievements'])} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players = {
        "Cihan": {
            "score": 2559,
            "achievements": ["always late", "less logtime", "42_student"]
            },
        "Gautier": {
            "score": 1956,
            "achievements": ["42_student", "code_slayer", "COD_Demon"]
            },
        "Kevin": {
            "score": 254,
            "achievements": ["42_student", "Tutor", "ChatGPT_enjoyer",
                             "Stopped_smoking"]
            },
        "Nathan": {
            "score": 4139,
            "achievements": ["Exam_failer", "want_to_eat", "6 or 7"]
            },
        }
    list_comprehension(players)
    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(players)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players)
    print("\n=== Combined Analysis ===")
    analysis(players)
