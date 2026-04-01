from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, atk: int):
        super().__init__(name, cost, rarity)
        self.atk = atk
        self.win = 0
        self.loose = 0
        self.rate = 0

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] = game_state["mana"] - self.cost
        else:
            return {
                "cost": self.cost,
                "actual_mana": game_state["mana"],
                "is_playable": self.is_playable(game_state["mana"]),
            }
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = (
            f"Card, {self.name}," f" summoned to battlefield"
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": (f"Card, {self.name}," f" summoned to battlefield"),
        }

    def attack(self, target) -> dict:
        if isinstance(target, TournamentCard):
            if self.atk > target.atk:
                self.update_wins(self.win)
                target.update_losses(target.loose)
                return {
                    "winner": f"{self.name.lower()}_001",
                    "loser": f"{target.name.lower()}_001",
                    "winner_rating": self.rate,
                    "loser_rating": target.rate,
                }
            elif self.atk < target.atk:
                target.update_wins(target.win)
                self.update_losses(self.loose)
                return {
                    "winner": f"{target.name.lower()}_001",
                    "loser": f"{self.name.lower()}_001",
                    "winner_rating": target.rate,
                    "loser_rating": self.rate,
                }
            else:
                return {
                    "winner": "Egality",
                    "loser": "Egality",
                    "winner_rating": "Egality",
                    "loser_rating": "Egality",
                }
        else:
            return {"match": "didnt happened because no good card were put"}

    def defend(self, incoming_damage: int) -> dict:
        if self.atk > incoming_damage:
            self.update_wins(self.win)
            return {
                "winner": f"{self.name.lower()}_001",
                "loser": "anonymous",
                "winner_rating": self.rate,
                "loser_rating": "anonymous",
            }
        elif self.atk < incoming_damage:
            self.update_losses(self.loose)
            return {
                "winner": "anonymous",
                "loser": f"{self.name.lower()}_001",
                "winner_rating": "anonymous",
                "loser_rating": self.rate,
            }
        else:
            return {
                "winner": "Egality",
                "loser": "Egality",
                "winner_rating": "Egality",
                "loser_rating": "Egality",
            }

    def calculate_rating(self) -> int:
        self.rate = round(100 + self.atk - self.cost)
        return self.rate

    def update_wins(self, wins: int) -> None:
        self.rate = self.rate + 16
        self.win = wins + 1

    def update_losses(self, losses: int) -> None:
        self.rate = self.rate - 16
        self.loose = losses + 1

    def get_rank_info(self) -> dict:
        pass

    def get_tournament_stats(self) -> dict:
        parents = [cls.__name__ for cls in self.__class__.__bases__]
        if self.rate == 0:
            self.calculate_rating()
        return {
            "name": self.name,
            "interfaces": parents,
            "rating": self.rate,
            "record": f"{self.win}-{self.loose}",
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.atk}
