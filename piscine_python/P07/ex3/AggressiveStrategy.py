from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        self.mana = 10

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        hand.sort(key=lambda card: card.cost)
        while self.mana - hand[0].cost > 0:
            battlefield.append(hand[0])
            self.mana = self.mana - hand[0].cost
            hand.remove(hand[0])
        return {
            "hand": hand,
            "battlefield": battlefield
        }

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        for card in available_targets:
            if isinstance(card, (CreatureCard, EliteCard)):
                available_targets.remove(card)
        return (available_targets)
