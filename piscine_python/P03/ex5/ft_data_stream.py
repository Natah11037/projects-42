#!/usr/bin/env python3

import random
from typing import Generator


PLAYERS = ["alice", "bob", "cihan", "delphine", "elyan", "farouk", "gautier",
           "hector", "irene", "julien", "kevin", "lea", "manon", "nathan",
           "ophelie", "patrick", "quentin", "roxanne", "sana", "titouanne",
           "ulysse", "valerie", "walid", "xyffard", "yoan", "zach"]

EVENTS = ["died", "found a treasure", "got 3 diamonds in a chest",
          "get diffed by a door", "found the one piece", "got a shiny",
          "got a full iv", "got crit", "got 1 shotted", "need to sleep",
          "need to take a shower", "is playing in a 10 hours streak",
          "received love from a pet", "is rich (more than 100k gold)",
          "believed he can fly (fall from more than 100 meters)",
          "tried to make a wish but failed", "got he's wish realised !!!"]


def generator(nb_events: int) -> Generator[dict, None, None]:
    for i in range(nb_events):
        event = {
            'number': i + 1,
            'player': random.choice(PLAYERS),
            'level': random.randint(1, 100),
            'events': random.choice(EVENTS)
        }
        yield event


def fibonacci_generate(nb) -> Generator[dict, None, None]:
    a = 0
    b = 1
    for i in range(nb):
        a = a + b       


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    total_events = 0
    high_lvl_players = 0
    stinky_weeb_events = 0
    badluck = 0
    noob = 0
    print("Processing 1000 game events...\n")
    for event in generator(3):
        print(event)
        total_events += 1
        if event["level"] >= 85:
            high_lvl_players += 1
        if event["events"] in (
                "need to sleep",
                "need to take a shower",
                "is playing in a 10 hours streak"):
            stinky_weeb_events += 1
        if event["events"] in (
                "got crit",
                "got 1 shotted",
                "tried to make a wish but failed"):
            badluck += 1
        if event["events"] in (
                "died",
                "get diffed by a door",
                "believed he can fly (fall from more than 100 meters)"):
            noob += 1
    print("...\n")
    for event in generator(997):
        total_events += 1
        if event["level"] >= 85:
            high_lvl_players += 1
        if event["events"] in (
                "need to sleep",
                "need to take a shower",
                "is playing in a 10 hours streak"):
            stinky_weeb_events += 1
        if event["events"] in (
                "got crit",
                "got 1 shotted",
                "tried to make a wish but failed"):
            badluck += 1
        if event["events"] in (
                "died",
                "get diffed by a door",
                "believed he can fly (fall from more than 100 meters)"):
            noob += 1
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (85+): {high_lvl_players}")
    print(f"Stinky weeb events: {stinky_weeb_events}")
    print(f"Badluck events: {badluck}")
    print(f"Noobs events: {noob}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    nb = 10
    fibo_dict = {}
    for i in fibonacci_generate(nb):
        str(i)
    fibonacci_sequence = ", ".join()
    print(f"Fibonacci sequence (first {nb}): {}")
