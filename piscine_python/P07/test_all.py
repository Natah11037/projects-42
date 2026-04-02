import unittest
from abc import ABC

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard
from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex4.Rankable import Rankable
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


# ─── EX0 ─────────────────────────────────────────────────────────────────────── # noqa E501


class TestCard(unittest.TestCase):
    def test_card_is_abstract(self):
        self.assertTrue(issubclass(Card, ABC))
        with self.assertRaises(TypeError):
            Card("test", 10, "common")

    def test_card_has_abstract_play(self):
        self.assertIn("play", Card.__abstractmethods__)


class TestCreatureCard(unittest.TestCase):
    def setUp(self):
        self.card = CreatureCard("Rebecca", 75, "iconic", 7, 5)

    def test_creation(self):
        self.assertEqual(self.card.name, "Rebecca")
        self.assertEqual(self.card.cost, 75)
        self.assertEqual(self.card.rarity, "iconic")
        self.assertEqual(self.card.attack, 7)
        self.assertEqual(self.card.health, 5)

    def test_invalid_attack_raises(self):
        with self.assertRaises(AttributeError):
            CreatureCard("Bad", 10, "common", 0, 5)
        with self.assertRaises(AttributeError):
            CreatureCard("Bad", 10, "common", -1, 5)

    def test_invalid_health_raises(self):
        with self.assertRaises(AttributeError):
            CreatureCard("Bad", 10, "common", 5, 0)
        with self.assertRaises(AttributeError):
            CreatureCard("Bad", 10, "common", 5, -1)

    def test_is_playable_true(self):
        self.assertTrue(self.card.is_playable(100))
        self.assertTrue(self.card.is_playable(75))

    def test_is_playable_false(self):
        self.assertFalse(self.card.is_playable(74))
        self.assertFalse(self.card.is_playable(0))

    def test_is_playable_returns_bool(self):
        self.assertIsInstance(self.card.is_playable(100), bool)

    def test_play_with_enough_mana(self):
        result = self.card.play({"mana": 100})
        self.assertIsInstance(result, dict)
        self.assertEqual(result["card_played"], "Rebecca")
        self.assertEqual(result["mana_used"], 75)

    def test_play_without_enough_mana(self):
        result = self.card.play({"mana": 10})
        self.assertIsInstance(result, dict)
        self.assertNotIn("card_played", result)

    def test_get_card_info(self):
        info = self.card.get_card_info()
        self.assertIn("name", info)
        self.assertIn("cost", info)
        self.assertIn("rarity", info)
        self.assertIn("type", info)
        self.assertIn("attack", info)
        self.assertIn("health", info)
        self.assertEqual(info["type"], "Creature")

    def test_attack_target(self):
        result = self.card.attack_target("enemy")
        self.assertEqual(result["attacker"], "Rebecca")
        self.assertEqual(result["target"], "enemy")
        self.assertEqual(result["damage_dealt"], 7)
        self.assertTrue(result["combat_resolved"])

    def test_attack_target_damage_is_int(self):
        result = self.card.attack_target("enemy")
        self.assertIsInstance(result["damage_dealt"], int)

    def test_inherits_card(self):
        self.assertIsInstance(self.card, Card)


# ─── EX1 ─────────────────────────────────────────────────────────────────────── # noqa E501


class TestSpellCard(unittest.TestCase):
    def setUp(self):
        self.spell = SpellCard("Lightning", 15, "common", "damage")

    def test_creation(self):
        self.assertEqual(self.spell.name, "Lightning")
        self.assertEqual(self.spell.effect_type, "damage")

    def test_play_with_mana(self):
        result = self.spell.play({"mana": 50})
        self.assertIsInstance(result, dict)
        self.assertEqual(result["card_played"], "Lightning")

    def test_play_without_mana(self):
        result = self.spell.play({"mana": 5})
        self.assertIsInstance(result, dict)
        self.assertNotIn("card_played", result)

    def test_resolve_effect_no_targets(self):
        result = self.spell.resolve_effect([])
        self.assertEqual(result["effect"], "no creature targets")

    def test_resolve_effect_with_creature(self):
        target = CreatureCard("Goblin", 10, "common", 2, 5)
        result = self.spell.resolve_effect([target])
        self.assertIn("effect", result)
        self.assertNotEqual(result["effect"], "no creature targets")

    def test_resolve_effect_heal(self):
        heal = SpellCard("Heal", 30, "rare", "heal")
        target = CreatureCard("Goblin", 10, "common", 2, 5)
        result = heal.resolve_effect([target])
        self.assertIn("heal", result["effect"])

    def test_inherits_card(self):
        self.assertIsInstance(self.spell, Card)


class TestArtifactCard(unittest.TestCase):
    def setUp(self):
        self.artifact = ArtifactCard("Lava Field", 50, "epic", 3, "burns")

    def test_creation(self):
        self.assertEqual(self.artifact.name, "Lava Field")
        self.assertEqual(self.artifact.durability, 3)

    def test_invalid_durability_raises(self):
        with self.assertRaises(AttributeError):
            ArtifactCard("Bad", 10, "common", 0, "effect")
        with self.assertRaises(AttributeError):
            ArtifactCard("Bad", 10, "common", -1, "effect")

    def test_play_with_mana(self):
        result = self.artifact.play({"mana": 100})
        self.assertIsInstance(result, dict)
        self.assertEqual(result["card_played"], "Lava Field")

    def test_play_without_mana(self):
        result = self.artifact.play({"mana": 10})
        self.assertNotIn("card_played", result)

    def test_activate_ability_decrements_durability(self):
        initial = self.artifact.durability
        self.artifact.activate_ability()
        self.assertEqual(self.artifact.durability, initial - 1)

    def test_activate_ability_at_zero(self):
        self.artifact.durability = 0
        result = self.artifact.activate_ability()
        self.assertIsNone(result.get("active_effect"))

    def test_inherits_card(self):
        self.assertIsInstance(self.artifact, Card)


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.card1 = CreatureCard("Goblin", 10, "common", 2, 5)
        self.card2 = SpellCard("Fire", 15, "common", "damage")
        self.card3 = ArtifactCard("Shield", 20, "rare", 2, "blocks")

    def test_add_card(self):
        self.deck.add_card(self.card1)
        self.assertIn(self.card1, self.deck.list_card)

    def test_remove_card_existing(self):
        self.deck.add_card(self.card1)
        result = self.deck.remove_card("Goblin")
        self.assertTrue(result)
        self.assertNotIn(self.card1, self.deck.list_card)

    def test_remove_card_nonexistent(self):
        self.deck.add_card(self.card1)
        result = self.deck.remove_card("Ghost")
        self.assertFalse(result)

    def test_draw_card(self):
        self.deck.add_card(self.card1)
        self.deck.add_card(self.card2)
        drawn = self.deck.draw_card()
        self.assertIsInstance(drawn, Card)
        self.assertEqual(len(self.deck.list_card), 1)

    def test_shuffle_does_not_crash(self):
        self.deck.add_card(self.card1)
        self.deck.add_card(self.card2)
        self.deck.shuffle()
        self.assertEqual(len(self.deck.list_card), 2)

    def test_shuffle_empty_deck(self):
        self.deck.list_card = []
        self.deck.shuffle()  # should not raise

    def test_get_deck_stats_keys(self):
        self.deck.add_card(self.card1)
        self.deck.add_card(self.card2)
        self.deck.add_card(self.card3)
        stats = self.deck.get_deck_stats()
        self.assertIn("total_cards", stats)
        self.assertIn("creatures", stats)
        self.assertIn("spells", stats)
        self.assertIn("artifacts", stats)
        self.assertIn("avg_cost", stats)

    def test_get_deck_stats_counts(self):
        self.deck.add_card(self.card1)
        self.deck.add_card(self.card2)
        self.deck.add_card(self.card3)
        stats = self.deck.get_deck_stats()
        self.assertEqual(stats["total_cards"], 3)
        self.assertEqual(stats["creatures"], 1)
        self.assertEqual(stats["spells"], 1)
        self.assertEqual(stats["artifacts"], 1)

    def test_avg_cost(self):
        self.deck.add_card(self.card1)
        self.deck.add_card(self.card2)
        stats = self.deck.get_deck_stats()
        self.assertAlmostEqual(stats["avg_cost"], 12.5)


# ─── EX2 ─────────────────────────────────────────────────────────────────────── # noqa E501


class TestEliteCard(unittest.TestCase):
    def setUp(self):
        self.roadhog = EliteCard("Roadhog", 50, "legendary", 750, 94, 40, 10)
        self.doomfist = EliteCard("Doomfist", 50, "legendary", 525, 36, 30, 10)

    def test_multiple_inheritance(self):
        self.assertIsInstance(self.roadhog, Card)
        self.assertIsInstance(self.roadhog, Combatable)
        self.assertIsInstance(self.roadhog, Magical)

    def test_play_with_mana(self):
        result = self.roadhog.play({"player": "Test", "mana": 100})
        self.assertEqual(result["card_played"], "Roadhog")

    def test_play_without_mana(self):
        result = self.roadhog.play({"player": "Test", "mana": 10})
        self.assertNotIn("card_played", result)

    def test_attack_with_target(self):
        result = self.roadhog.attack(self.doomfist)
        self.assertEqual(result["attacker"], "Roadhog")
        self.assertEqual(result["target"], "Doomfist")
        self.assertEqual(result["damage"], 94)

    def test_attack_without_target(self):
        result = self.roadhog.attack(None)
        self.assertIsNone(result["target"])
        self.assertEqual(result["damage"], 0)

    def test_defend(self):
        result = self.roadhog.defend(36)
        self.assertIn("damage_taken", result)
        self.assertIn("damage_blocked", result)
        self.assertIn("still_alive", result)

    def test_defend_blocked_capped_at_defense(self):
        result = self.roadhog.defend(100)
        self.assertEqual(result["damage_blocked"], 40)

    def test_cast_spell_enough_mana(self):
        result = self.roadhog.cast_spell("hook", [self.doomfist])
        self.assertEqual(result["caster"], "Roadhog")
        self.assertIn("Doomfist", result["targets"])

    def test_cast_spell_non_card_targets_filtered(self):
        result = self.roadhog.cast_spell("hook", ["not_a_card", self.doomfist])
        self.assertNotIn("not_a_card", result["targets"])

    def test_channel_mana_int(self):
        before = self.roadhog.mana
        result = self.roadhog.channel_mana(4)
        self.assertEqual(result["channeled"], 4)
        self.assertEqual(self.roadhog.mana, before + 4)

    def test_channel_mana_non_int(self):
        before = self.roadhog.mana
        result = self.roadhog.channel_mana("four")
        self.assertEqual(result["channeled"], 0)
        self.assertEqual(self.roadhog.mana, before)

    def test_get_combat_stats(self):
        stats = self.roadhog.get_combat_stats()
        self.assertIn("health", stats)
        self.assertIn("damage", stats)
        self.assertIn("defense", stats)

    def test_get_magic_stats(self):
        stats = self.roadhog.get_magic_stats()
        self.assertIn("mana", stats)

    def test_combatable_is_abstract(self):
        self.assertIsInstance(Combatable, type)
        with self.assertRaises(TypeError):
            Combatable()

    def test_magical_is_abstract(self):
        with self.assertRaises(TypeError):
            Magical()


# ─── EX3 ─────────────────────────────────────────────────────────────────────── # noqa E501


class TestAggressiveStrategy(unittest.TestCase):
    def setUp(self):
        self.strat = AggressiveStrategy()

    def test_get_strategy_name(self):
        self.assertEqual(self.strat.get_strategy_name(), "Aggressive Strategy")

    def test_execute_turn_returns_dict(self):
        hand = [
            CreatureCard("A", 3, "common", 1, 1),
            CreatureCard("B", 8, "common", 2, 2),
        ]
        result = self.strat.execute_turn(hand, [])
        self.assertIn("hand", result)
        self.assertIn("battlefield", result)

    def test_execute_turn_plays_affordable_cards(self):
        self.strat.mana = 10
        hand = [
            CreatureCard("Cheap", 3, "common", 1, 1),
            CreatureCard("Costly", 8, "common", 2, 2),
        ]
        result = self.strat.execute_turn(hand, [])
        names = [c.name for c in result["battlefield"]]
        self.assertIn("Cheap", names)

    def test_execute_turn_empty_hand_no_crash(self):
        self.strat.mana = 10
        result = self.strat.execute_turn([], [])
        self.assertEqual(result["hand"], [])
        self.assertEqual(result["battlefield"], [])

    def test_prioritize_targets_removes_creatures(self):
        c = CreatureCard("G", 10, "common", 2, 5)
        e = EliteCard("E", 50, "legendary", 500, 90, 40, 10)
        other = "non_card"
        result = self.strat.prioritize_targets([c, e, other])
        self.assertNotIn(c, result)
        self.assertNotIn(e, result)
        self.assertIn(other, result)

    def test_prioritize_targets_does_not_mutate_original(self):
        c = CreatureCard("G", 10, "common", 2, 5)
        original = [c, "other"]
        self.strat.prioritize_targets(original)
        self.assertEqual(len(original), 2)

    def test_inherits_game_strategy(self):
        self.assertIsInstance(self.strat, GameStrategy)


class TestFantasyCardFactory(unittest.TestCase):
    def setUp(self):
        self.factory = FantasyCardFactory()

    def test_create_creature_by_name(self):
        card = self.factory.create_creature("goblin")
        self.assertIsInstance(card, CreatureCard)

    def test_create_creature_random(self):
        card = self.factory.create_creature()
        self.assertIsInstance(card, CreatureCard)

    def test_create_spell_by_name(self):
        card = self.factory.create_spell("lightning")
        self.assertIsInstance(card, SpellCard)

    def test_create_spell_random(self):
        card = self.factory.create_spell()
        self.assertIsInstance(card, SpellCard)

    def test_create_artifact_by_name(self):
        card = self.factory.create_artifact("lava field")
        self.assertIsInstance(card, ArtifactCard)

    def test_create_artifact_random(self):
        card = self.factory.create_artifact()
        self.assertIsInstance(card, ArtifactCard)

    def test_create_themed_deck_returns_dict(self):
        deck = self.factory.create_themed_deck(3)
        self.assertIsInstance(deck, dict)
        self.assertEqual(len(deck), 3)

    def test_create_themed_deck_values_are_cards(self):
        deck = self.factory.create_themed_deck(3)
        for card in deck.values():
            self.assertIsInstance(card, Card)

    def test_get_supported_types(self):
        types = self.factory.get_supported_types()
        self.assertIsInstance(types, dict)
        self.assertIn("Creature", types)
        self.assertIn("Spell", types)
        self.assertIn("Artifact", types)

    def test_inherits_card_factory(self):
        self.assertIsInstance(self.factory, CardFactory)


class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()
        self.engine.configure_engine(
            FantasyCardFactory(), AggressiveStrategy()
        )

    def test_configure_engine(self):
        self.assertIsInstance(self.engine.factory, CardFactory)
        self.assertIsInstance(self.engine.strategy, GameStrategy)

    def test_simulate_turn_returns_dict(self):
        result = self.engine.simulate_turn()
        self.assertIsInstance(result, dict)
        self.assertIn("cards_played", result)
        self.assertIn("mana_used", result)
        self.assertIn("damage_dealt", result)

    def test_simulate_turn_increments_counter(self):
        self.engine.simulate_turn()
        self.assertEqual(self.engine.turn, 1)
        self.engine.simulate_turn()
        self.assertEqual(self.engine.turn, 2)

    def test_simulate_turn_tracks_cards_created(self):
        before = self.engine.card_created
        self.engine.simulate_turn()
        self.assertGreater(self.engine.card_created, before)

    def test_get_engine_status_keys(self):
        self.engine.simulate_turn()
        status = self.engine.get_engine_status()
        self.assertIn("turns_simulated", status)
        self.assertIn("strategy_used", status)
        self.assertIn("total_damage", status)
        self.assertIn("cards_created", status)

    def test_damage_dealt_is_int(self):
        result = self.engine.simulate_turn()
        self.assertIsInstance(result["damage_dealt"], int)


# ─── EX4 ─────────────────────────────────────────────────────────────────────── # noqa E501


class TestTournamentCard(unittest.TestCase):
    def setUp(self):
        self.card_a = TournamentCard("Alpha", 5, "rare", 8)
        self.card_b = TournamentCard("Beta", 3, "common", 4)

    def test_multiple_inheritance(self):
        from ex2.Combatable import Combatable
        from ex4.Rankable import Rankable

        self.assertIsInstance(self.card_a, Card)
        self.assertIsInstance(self.card_a, Combatable)
        self.assertIsInstance(self.card_a, Rankable)

    def test_play_with_mana(self):
        result = self.card_a.play({"mana": 100})
        self.assertEqual(result["card_played"], "Alpha")

    def test_play_without_mana(self):
        result = self.card_a.play({"mana": 1})
        self.assertNotIn("card_played", result)

    def test_attack_winner(self):
        result = self.card_a.attack(self.card_b)
        self.assertIn("winner", result)
        self.assertIn("alpha", result["winner"])

    def test_attack_loser(self):
        result = self.card_b.attack(self.card_a)
        self.assertIn("loser", result)
        self.assertIn("beta", result["loser"])

    def test_attack_equality(self):
        c = TournamentCard("C", 5, "common", 8)
        result = self.card_a.attack(c)
        self.assertEqual(result["winner"], "Egality")

    def test_attack_wrong_type(self):
        result = self.card_a.attack("not_a_card")
        self.assertIn("match", result)

    def test_attack_updates_win_rate(self):
        before_rate = self.card_a.rate
        self.card_a.calculate_rating()
        self.card_a.attack(self.card_b)
        self.assertGreater(self.card_a.rate, before_rate)
        self.assertEqual(self.card_a.win, 1)

    def test_attack_updates_loss_rate(self):
        self.card_b.calculate_rating()
        self.card_a.attack(self.card_b)
        self.assertEqual(self.card_b.loose, 1)

    def test_calculate_rating(self):
        rate = self.card_a.calculate_rating()
        self.assertIsInstance(rate, int)
        self.assertEqual(self.card_a.rate, rate)

    def test_update_wins(self):
        self.card_a.rate = 100
        self.card_a.update_wins(0)
        self.assertEqual(self.card_a.rate, 116)
        self.assertEqual(self.card_a.win, 1)

    def test_update_losses(self):
        self.card_a.rate = 100
        self.card_a.update_losses(0)
        self.assertEqual(self.card_a.rate, 84)
        self.assertEqual(self.card_a.loose, 1)

    def test_get_rank_info(self):
        result = self.card_a.get_rank_info()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("win", result)
        self.assertIn("losses", result)
        self.assertIn("ranking", result)

    def test_get_combat_stats(self):
        result = self.card_a.get_combat_stats()
        self.assertIn("attack", result)
        self.assertEqual(result["attack"], 8)

    def test_get_tournament_stats(self):
        result = self.card_a.get_tournament_stats()
        self.assertIn("name", result)
        self.assertIn("interfaces", result)
        self.assertIn("rating", result)
        self.assertIn("record", result)

    def test_rankable_is_abstract(self):
        with self.assertRaises(TypeError):
            Rankable()


class TestTournamentPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = TournamentPlatform()
        self.card_a = TournamentCard("Alpha", 5, "rare", 8)
        self.card_b = TournamentCard("Beta", 3, "common", 4)
        self.card_a.calculate_rating()
        self.card_b.calculate_rating()

    def test_register_card_returns_id(self):
        card_id = self.platform.register_card(self.card_a)
        self.assertIsInstance(card_id, str)
        self.assertIn("alpha", card_id)

    def test_register_card_adds_to_list(self):
        self.platform.register_card(self.card_a)
        self.assertIn(self.card_a, self.platform.cards)

    def test_create_match_returns_dict(self):
        result = self.platform.create_match("alpha_001", "beta_001")
        self.assertIn("first", result)
        self.assertIn("type", result)
        self.assertIn("second", result)

    def test_create_match_increments_counter(self):
        self.platform.create_match("a", "b")
        self.assertEqual(self.platform.match_played, 1)

    def test_get_leaderboard_sorted(self):
        self.platform.register_card(self.card_a)
        self.platform.register_card(self.card_b)
        self.card_a.attack(self.card_b)
        leaderboard = self.platform.get_leaderboard()
        self.assertGreaterEqual(leaderboard[0].rate, leaderboard[1].rate)

    def test_get_leaderboard_returns_list(self):
        self.platform.register_card(self.card_a)
        result = self.platform.get_leaderboard()
        self.assertIsInstance(result, list)

    def test_generate_tournament_report_keys(self):
        self.platform.register_card(self.card_a)
        self.platform.register_card(self.card_b)
        report = self.platform.generate_tournament_report()
        self.assertIn("total_cards", report)
        self.assertIn("matches_played", report)
        self.assertIn("avg_rating", report)
        self.assertIn("platform_status", report)

    def test_generate_tournament_report_platform_status_key(self):
        self.platform.register_card(self.card_a)
        report = self.platform.generate_tournament_report()
        self.assertNotIn("platfrom_status", report)
        self.assertEqual(report["platform_status"], "active")

    def test_generate_report_avg_rating(self):
        self.platform.register_card(self.card_a)
        self.platform.register_card(self.card_b)
        report = self.platform.generate_tournament_report()
        expected = (self.card_a.rate + self.card_b.rate) / 2
        self.assertAlmostEqual(report["avg_rating"], expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
