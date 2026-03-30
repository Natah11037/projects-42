from .Card import Card
from typing import Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        if attack > 0 and health > 0:
            self.attack = attack
            self.health = health
        else:
            raise AttributeError("attack or health is unitialized"
                                 " at a wrong value (need to be > 0)\n")

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] = game_state["mana"] - self.cost
        else:
            return {"cost": self.cost, "actual_mana": game_state["mana"],
                    "is_playable": self.is_playable(game_state["mana"])}
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = (f"Creature, {self.name},"
                                f" summoned to battlefield")
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": (f"Creature, {self.name},"
                       f" summoned to battlefield")
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def attack_target(self, target: Any) -> dict:
        return {"attacker": self.name, "target": target,
                "damage_dealt": self.attack, "combat_resolved": True}
