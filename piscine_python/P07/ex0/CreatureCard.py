from .Card import Card
from typing import Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super.__init__(name, cost, rarity)
        if attack >= 0 and health >= 0:
            self.attack = attack
            self.health = health

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] = game_state["mana"] - self.cost
        else:
            return (f"{self.name} is not playable because you"
                    f" don't have the required quantity of mana")
        try:
            game_state["Card_played"].append(self.get_card_info())
        except KeyError:
            game_state["Card_played"] = [self.get_card_info()]
        return (game_state)
    
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.append(self.attack, self.health)
        return {info}

    def attack_target(self, target: Any) -> dict:
        attack = {"attacker": self.name, "target": target, "damage_dealt": 10, "combat_resolved": True}
