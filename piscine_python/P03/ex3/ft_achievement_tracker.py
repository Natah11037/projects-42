#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    cihan_achievements = {
        "Defeated_by_a_splinter",
        "42_student",
        "less_logtime",
    }
    kevin_achievements = {
        "42_student",
        "Tutor",
        "ChatGPT_enjoyer",
        "Stopped_smoking",
    }
    gautier_achievements = {"42_student", "code_slayer", "COD_Demon"}
    print(f"Player Cihan achievements: {cihan_achievements}")
    print(f"Player Kevin achievements: {kevin_achievements}")
    print(f"Player Gautier achievements: {gautier_achievements}")
    print("\n=== Achievement Analytics ===")
    ouaboula = cihan_achievements.union(
        kevin_achievements, gautier_achievements
    )
    print(f"All unique achievements: {ouaboula}")
    print(f"Total unique achievements: {len(ouaboula)}\n")
    common_all = cihan_achievements.intersection(
        kevin_achievements, gautier_achievements
    )
    print(f"Common to all players: {common_all}")
    cihan_unique = cihan_achievements.difference(
        kevin_achievements, gautier_achievements
    )
    kevin_unique = kevin_achievements.difference(
        cihan_achievements, gautier_achievements
    )
    gautier_unique = gautier_achievements.difference(
        cihan_achievements, kevin_achievements
    )
    rare_achievements = cihan_unique.union(kevin_unique, gautier_unique)
    print(f"Rare achievement (1 Player): {rare_achievements}\n")
    cihan_vs_kevin = cihan_achievements.intersection(kevin_achievements)
    print(f"Cihan vs Kevin common: {cihan_vs_kevin}")
    cihan_unique = cihan_achievements.difference(
        kevin_achievements, gautier_achievements
    )
    print(f"Cihan unique: {cihan_unique}")
    kevin_unique = kevin_achievements.difference(
        cihan_achievements, gautier_achievements
    )
    print(f"Kevin unique: {kevin_unique}")
