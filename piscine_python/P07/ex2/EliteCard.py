from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
from ex0.CreatureCard import CreatureCard


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, damage: int, defense: int, mana: int):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.defense = defense
        self.mana = mana

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
        game_state["effect"] = (f"{game_state['player']} "
                                f"is playing {self.name}")
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": (f"{game_state['player']} is playing {self.name}")
        }

    def attack(self, target) -> dict:
        if target:
            return {
                "attacker": self.name,
                "target": target.name,
                "damage": self.damage,
                "combat_type": "shotgun"
            }
        else:
            return {
                "attacker": self.name,
                "target": None,
                "damage": 0,
                "combat_type": "emoting"
            }

    def defend(self, incoming_damage: int) -> dict:
        if self.defense >= incoming_damage:
            blocked = incoming_damage
        else:
            blocked = self.defense

        if self.health > incoming_damage - self.defense:
            alive = True
        else:
            alive = False

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": blocked,
            "still_alive": alive
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        targets = [
            target for target in targets if
            isinstance(target, (EliteCard, CreatureCard))
        ]
        if len(targets) <= self.mana:
            self.mana = self.mana - len(targets)
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [target.name for target in targets],
                "mana_used": len(targets)
            }
        else:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [target.name for target in targets],
                "mana_used": "Not the required ammount of mana",
                "state of the spell": "aborth"
            }

    def channel_mana(self, amount: int) -> dict:
        if isinstance(amount, int):
            self.mana = self.mana + amount
            return {
                "channeled": amount,
                "total_mana": self.mana
            }
        else:
            return {
                "channeled": 0,
                "total_mana": self.mana
            }

    def get_combat_stats(self) -> dict:
        return {
            "health": self.health,
            "damage": self.damage,
            "defense": self.defense
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
