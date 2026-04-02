from .TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.cards = []
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"ID: {card.name.lower()}_001"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.match_played += 1
        return {
            "first": card1_id,
            "type": "VS",
            "second": card2_id
        }

    def get_leaderboard(self) -> list:
        sort_top = sorted(self.cards, key=lambda card: card.rate, reverse=True)
        return sort_top

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "matches_played": self.match_played,
            "avg_rating": (
                sum(card.rate for card in self.cards) / len(self.cards)
                ),
            "platform_status": "active"
        }
