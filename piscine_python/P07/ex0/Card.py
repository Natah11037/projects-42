from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        playable = False
        if available_mana >= self.cost:
            playable = True
        return (playable)


if __name__ == "__main__":
    rebecca = Card("Rebecca", 80, "Iconic")
    game = {"mana": 100}
    rebecca.play(game)
    print(game)
