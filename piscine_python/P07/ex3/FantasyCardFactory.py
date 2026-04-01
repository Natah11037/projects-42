import random

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    creature_dict = {
        "king sloth": (
            "King Sloth",
            45,
            "rare",
            3,
            16,
        ),
        "goblin": ("Goblin", 10, "common", 2, 5),
        "cute kitty": ("Cute Kitty", 25, "epic", 8, 8),
        "slime": ("Slime", 15, "uncommon", 1, 6),
        "flying robotic shark": ("Flying Robotic Shark", 60, "legendary", 10,
                                 15),
    }
    spell_dict = {
        "lightning": ("Lightning", 15, "common", "damage"),
        "heal": ("Heal", 30, "rare", "heal"),
        "speed boost": ("Speed Boost", 25, "uncommon", "buff"),
        "stone curse": ("Stone Curse", 35, "epic", "debuff"),
        "burn": ("Burn", 15, "common", "damage"),
        "freeze": ("Freeze", 30, "rare", "debuff"),
        "strength boost": ("Strength Boost", 25, "uncommon", "buff"),
        "poison": ("Poison", 25, "rare", "damage"),
        "flowering": ("Flowering", 40, "rare", "heal"),
        "explosion": ("Explosion", 30, "uncommon", "damage"),
    }

    artifact_dict = {
        "water field": (
            "Water Field",
            40,
            "rare",
            3,
            "submerge the field with water which heal " "all allies each turn",
        ),
        "lava field": (
            "Lava Field",
            50,
            "epic",
            3,
            "Lava flood the field,"
            " every target who get hit take x1,5 more damage",
        ),
        "cloudy field": (
            "Cloudy Field",
            35,
            "uncommon",
            4,
            "card goes in the sky,"
            " every target have 20% to miss their attack",
        ),
        "venom field": (
            "Venom Field",
            30,
            "rare",
            6,
            "inflict damage to every card each turn",
        ),
        "night city": (
            "Night City",
            75,
            "legendary",
            1,
            "Welcome in Night City, The City of Dreams."
            " in this field your strongest card became a"
            " cyberpsychos and enrage. double damage,"
            " double life and attack in first for one turn",
        ),
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 10)
            rarity = random.choice(
                [
                    "common",
                    "uncommon",
                    "rare",
                    "epic",
                    "legendary",
                    "heroic",
                    "iconic",
                    "mythical",
                ]
            )
            attack = random.randint(1, 10)
            health = random.randint(1, 10)
            return CreatureCard(name, cost, rarity, attack, health)
        elif isinstance(name_or_power, int):
            name = random.choice(
                [
                    "goblin",
                    "bowser",
                    "xX_Toad_le_bg_Xx",
                    "nathan weber le talentueux",
                    "l'echarde dans le pied a cihan",
                    "la trott de gautier",
                    "copilot le retour",
                    "fee a la fraise des bois",
                    "Mr.Propre",
                    "bulbizarre",
                    "bout de carton mouille",
                    "Professeur.Layton",
                    "Hatsune Miku",
                    "power ranger magenta",
                    "Lionnel Messi",
                    "Julien Song",
                    "P05",
                    "exam rank 02",
                    "aquaman"
                ]
            )
            cost = random.randint(1, 10)
            rarity = random.choice(
                [
                    "common",
                    "uncommon",
                    "rare",
                    "epic",
                    "legendary",
                    "heroic",
                    "iconic",
                    "mythical",
                ]
            )
            attack = name_or_power
            health = random.randint(1, 10)
            return CreatureCard(name, cost, rarity, attack, health)
        else:
            name, cost, rarity, attack, health = random.choice(
                list(self.creature_dict.values())
            )
            return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 10)
            rarity = random.choice(
                [
                    "common",
                    "uncommon",
                    "rare",
                    "epic",
                    "legendary",
                    "heroic",
                    "iconic",
                    "mythical",
                ]
            )
            effect_type = random.choice(["damage", "buff", "debuff", "heal"])
            return SpellCard(name, cost, rarity, effect_type)
        elif isinstance(name_or_power, int):
            name = random.choice(
                [
                    "speed",
                    "poison",
                    "burn",
                    "freeze",
                    "stone curse",
                    "seisme",
                    "malediction",
                    "minimoyzed",
                    "gigantized",
                    "heal",
                    "dead",
                    "slow",
                    "stun",
                    "paralyze",
                    "levitating",
                    "explosion nucleaire de la mort ki "
                    "tue vraiment tres fort attention "
                    "danger je rigole pas le sort est ouf "
                    "de malade a lancer avec precaution un "
                    "peu comme manger avec precaution des "
                    "chocobons",
                    "suicide",
                ]
            )
            cost = random.randint(1, 10)
            rarity = random.choice(
                [
                    "common",
                    "uncommon",
                    "rare",
                    "epic",
                    "legendary",
                    "heroic",
                    "iconic",
                    "mythical",
                ]
            )
            effect_type = random.choice(["damage", "buff", "debuff", "heal"])
            return SpellCard(name, cost, rarity, effect_type)
        else:
            name, cost, rarity, effect_type = random.choice(
                list(self.spell_dict.values())
            )
            return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 10)
            rarity = random.choice(
                [
                    "common",
                    "uncommon",
                    "rare",
                    "epic",
                    "legendary",
                    "heroic",
                    "iconic",
                    "mythical",
                ]
            )
            durability = random.randint(1, 5)
            effect = random.choice(
                [
                    "die instantly",
                    "become an entity of the void",
                    "explode",
                    "suffer for the rest of your miserable life",
                    "fall on the ground",
                    "get strength",
                    "become Harder, Better, Faster, Stronger",
                    "get hug by all the creatures card",
                    "eat a delicious meal",
                    "improve dancing skills",
                ]
            )
            return ArtifactCard(name, cost, rarity, durability, effect)
        elif isinstance(name_or_power, int):
            name = random.choice(
                [
                    "water_necklace",
                    "ring of power",
                    "pretty hat",
                    "magical machine gun",
                    "nothing, what a lucky guy",
                    "lolipop with magic powder",
                    "strength uniform",
                    "hacking pen",
                    "explosive boots",
                    "deadly gauntlets",
                    "Lostvayne",
                ]
            )
            cost = random.randint(1, 10)
            rarity = random.choice(
                [
                    "common",
                    "uncommon",
                    "rare",
                    "epic",
                    "legendary",
                    "heroic",
                    "iconic",
                    "mythical"
                ]
            )
            durability = random.randint(1, 5)
            effect = random.choice(
                [
                    "die instantly",
                    "become an entity of the void",
                    "explode",
                    "suffer for the rest of your miserable life",
                    "fall on the ground",
                    "get strength",
                    "become Harder, Better, Faster, Stronger",
                    "get hug by all the creatures card",
                    "eat a delicious meal",
                    "improve dancing skills"
                ]
            )
            return ArtifactCard(name, cost, rarity, durability, effect)
        else:
            name, cost, rarity, durability, effect = random.choice(
                list(self.artifact_dict.values())
            )
            return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        if size > 0:
            deck = {}
            for i in range(size):
                argment = random.choice([
                    "Kevin",
                    10,
                    "Monster",
                    8,
                    "Zeus, the almighty god of the god",
                    7,
                    "a brainless goat",
                    11,
                    "Time Keeper",
                    4,
                    None,
                    2,
                    None,
                    None,
                    None,
                    None,
                    5,
                    6
                ])
                deck[f"card_{i}"] = random.choice([self.create_creature(
                    argment),
                                                   self.create_spell(argment),
                                                   self.create_artifact(
                                                       argment)])
            return deck
        else:
            return {
                "deck": "empty because of a wrong size value"
            }

    def get_supported_types(self) -> dict:
        return {
            "Creature": list(self.creature_dict.keys()),
            "Spell": list(self.spell_dict.keys()),
            "Artifact": list(self.artifact_dict.keys())
        }
