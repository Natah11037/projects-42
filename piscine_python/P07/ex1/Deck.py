from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.Card import Card
import random


class Deck():
    def __init__(self):
        pass

    def add_card(self, card: Card) -> None:
        try:
            self.list_card
        except AttributeError:
            self.list_card = []
        if isinstance(card, Card):
            self.list_card.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.list_card:
            if card.name == card_name:
                self.list_card.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        if not self.list_card:
            return
        random.shuffle(self.list_card)

    def draw_card(self) -> Card:
        card = self.list_card.pop()
        return (card)

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.list_card),
            "creatures": sum(1 for card in self.list_card
                             if isinstance(card, CreatureCard)),
            "spells": sum(1 for card in self.list_card
                          if isinstance(card, SpellCard)),
            "artifacts": sum(1 for card in self.list_card
                             if isinstance(card, ArtifactCard)),
            "avg_cost": sum(card.cost for card in self.list_card) / len(
                self.list_card)
        }
