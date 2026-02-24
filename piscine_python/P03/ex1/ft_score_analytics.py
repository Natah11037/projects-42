#!/usr/bin/env python3

import sys


def score_analytics() -> str:
    scores: list[str] = sys.argv[1:]
    if not scores:
        return ("No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> ...")
    else:
        scores_int: list[int] = []
        for score in scores:
            try:
                scores_int.append(int(score))
            except ValueError:
                return (f"{score} is not a valid input, please consider "
                        "retrying")
        average: float = sum(scores_int) / len(scores_int)
        return (f"Scores processed: {scores_int}\n"
                f"Total players: {len(scores_int)}\n"
                f"Total score: {sum(scores_int)}\n"
                f"Average score: {average}\n"
                f"High score: {max(scores_int)}\n"
                f"Low score: {min(scores_int)}\n"
                f"Score range: {max(scores_int) - min(scores_int)}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    print(score_analytics())
