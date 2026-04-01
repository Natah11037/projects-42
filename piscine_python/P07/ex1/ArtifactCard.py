from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if durability > 0:
            self.durability = durability
        else:
            raise AttributeError("Not a good value for durability"
                                 " (need to be > 0)")
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] = game_state["mana"] - self.cost
        else:
            return {"cost": self.cost, "actual_mana": game_state["mana"],
                    "is_playable": self.is_playable(game_state["mana"])}
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["durability"] = self.durability
        activate = self.activate_ability().get(
                "active_effect", None)
        game_state["active effect"] = activate
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "durability": self.durability,
            "active effect": activate
        }

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability = self.durability - 1
        elif self.durability == 0:
            return {
                "active_effect": None
            }
        return {
            "active_effect": self.effect
        }
