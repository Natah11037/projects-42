from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")

    generator_card = FantasyCardFactory()
    strat = AggressiveStrategy()
    game = GameEngine()
    print("Configuring Fantasy Card Game...")
    print(f"Factory: {generator_card.__class__.__name__}")
    print(f"Strategy: {strat.get_strategy_name()}")
    print(f"Available types: {generator_card.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    hand = generator_card.create_themed_deck(3)
    result = ", ".join(f"{card.name} ({card.cost})" for card in hand.values())
    print(f"Hand: [{result}]\n")

    print("Turn execution:")
    print(f"Strategy: {strat.get_strategy_name()}")
    game.configure_engine(generator_card, strat)
    print(f"Actions: {game.simulate_turn()}\n")

    print("Game Report:")
    print(game.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility"
          " achieved!\n")


if __name__ == "__main__":
    main()
