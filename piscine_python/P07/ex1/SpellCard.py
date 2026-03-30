from ex0 import CreatureCard
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] = game_state["mana"] - self.cost
        else:
            return {"cost": self.cost, "actual_mana": game_state["mana"],
                    "is_playable": self.is_playable(game_state["mana"])}
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.resolve_effect(game_state.get(
            "enemy_deck", None))["effect"]
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect(game_state['enemy_deck'])["effect"]
        }

    def resolve_effect(self, targets: list) -> dict:
        if all(isinstance(target, CreatureCard) for target in targets):
            if "heal" in self.effect_type:
                return {
                    "effect": f"{self.effect_type} every allies"
                }
            elif "damage" in self.effect_type:
                return {
                    "effect": f"deal {self.cost} to {[target.name for target in targets]}"
                }
            elif "debuff" in self.effect_type:
                return {
                    "effect": f"apply {self.effect_type} to "
                    f"{[target.name for target in targets]}"
                }
            elif "buff" in self.effect_type:
                return {
                    "effect": f"giving {self.effect_type} to every allies"
                }
            else:
                return {
                    "effect": None
                }
