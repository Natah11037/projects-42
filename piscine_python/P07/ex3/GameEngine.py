from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from .GameStrategy import GameStrategy
from .CardFactory import CardFactory


class GameEngine:
    def __init__(self):
        self.turn = 0
        self.total_dmg = 0
        self.card_created = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.turn = self.turn + 1
        cards_name = []
        card = self.factory.create_themed_deck(2)
        for value in card.values():
            self.card_created = self.card_created + 1
            cards_name.append(value.name)
        dmg = sum(
            cards.attack
            for cards in card.values()
            if isinstance(cards, (CreatureCard, EliteCard)))
        self.total_dmg = self.total_dmg + dmg
        return {
            "cards_played": cards_name,
            "mana_used": sum(cards.cost for cards in card.values()),
            "targets_attacked": "every creature on battlefield",
            "damage_dealt": dmg
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.__class__.__name__,
            "total_damage": self.total_dmg,
            "cards_created": self.card_created
        }
