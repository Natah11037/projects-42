# Feedback - DataDeck P07 (ex0 → ex4)

---

# Exercise 0 : Card Foundation

## Vue d'ensemble

Toutes les corrections ont ete apportees. Le code s'execute proprement, flake8 passe sans erreur, et les concepts sont correctement implementes.

---

## Structure du projet

- Arborescence conforme (`ex0/__init__.py`, `Card.py`, `CreatureCard.py`, `main.py`) : OK
- Execution depuis la racine avec `python3 -m ex0.main` : OK
- Import absolu dans `main.py` (`from ex0.CreatureCard import CreatureCard`) : OK

---

## Card.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `ABC` | OK | Correct |
| Constructeur avec type hints | OK | Signature conforme |
| `@abstractmethod` sur `play` | OK | Implemente correctement |
| `get_card_info()` avec retour `dict` | OK | |
| `is_playable()` avec retour `bool` | OK | |
| Bloc `__main__` supprime | OK | Corrige |

> **Point cosmetique** : `is_playable` utilise encore une variable intermediaire `playable` inutile. Simplifiable en `return available_mana >= self.cost`, mais pas bloquant.

---

## CreatureCard.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `Card` | OK | Correct |
| Constructeur complet avec type hints | OK | |
| Validation `attack > 0` et `health > 0` | OK | Corrige (etait `>= 0`) |
| `raise AttributeError` si valeur invalide | OK | Gestion d'erreur propre |
| Implementation de `play` | OK | Retourne un `dict` dans tous les cas |
| Return type de `play` coherent | OK | Corrige |
| `get_card_info()` etendu | OK | Ajoute bien `type`, `attack`, `health` |
| `attack_target()` - `damage_dealt` | OK | Bug du set `{self.attack}` corrige -> `self.attack` |
| Import `Any` du module `typing` | OK | Utilisation correcte |
| Flake8 | OK | Aucune erreur |

---

## main.py

| Point | Statut | Commentaire |
|---|---|---|
| Demo fonctionnelle | OK | Le script s'execute sans erreur |
| Gestion `try/except AttributeError` | OK | Coherent avec la validation du constructeur |
| Tests mana suffisant / insuffisant | OK | Les deux cas sont illustres |
| Libertes sur l'output | OK | Valeurs differentes de l'exemple du sujet mais logique identique |

---

## Output obtenu

```
=== DataDeck Card Foundation ===

Testing Abstract Base Class Design:

CreatureCard Info:
{'name': 'Rebecca', 'cost': 75, 'rarity': 'iconic', 'type': 'Creature', 'attack': 7, 'health': 5}

Playing Rebecca with 100 mana available:
Playable: True
Play result: {'player': 'Natah', 'mana': 25, 'card_played': 'Rebecca', 'mana_used': 75, 'effect': 'Creature, Rebecca, summoned to battlefield'}

Rebecca attacks cyberpsycho:
{'attacker': 'Rebecca', 'target': 'cyberpsycho', 'damage_dealt': 7, 'combat_resolved': True}

Testing insufficient mana (25 available):
Playable: False

Abstract pattern successfully demonstrated!
```

---

## Note ex0

| Critere | Points |
|---|---|
| Structure projet / imports | 2/2 |
| Card.py (ABC, methodes, types) | 4/4 |
| CreatureCard.py (heritage, methodes, validation) | 5/5 |
| main.py (demo fonctionnelle, gestion erreurs) | 2/2 |
| Qualite du code (flake8, types, style) | 3/3 |
| Libertes output coherentes | bonus |
| **Total** | **16/16** |

---

# Exercise 1 : Deck Builder

## Vue d'ensemble

Le code tourne sans crash, flake8 passe sans erreur. Toutes les classes sont correctement implementees.

---

## Structure du projet

- Arborescence conforme (`ex1/__init__.py`, `SpellCard.py`, `ArtifactCard.py`, `Deck.py`, `main.py`) : OK
- Execution depuis la racine avec `python3 -m ex1.main` : OK
- Import absolu depuis ex0 (`from ex0.Card import Card`) : OK
- Flake8 : OK

---

## SpellCard.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `Card` | OK | |
| Constructeur avec `effect_type` | OK | |
| `play()` implementee | OK | Retourne un dict dans tous les cas |
| `resolve_effect(targets)` implementee | OK | Logique custom par type d'effet |
| Gestion mana insuffisant | OK | Retourne un dict d'erreur |
| `game_state.get("enemy_deck", [])` | OK | `.get()` avec valeur par defaut `[]` |
| Import `from ex0.CreatureCard import CreatureCard` | OK | Import explicite |

---

## ArtifactCard.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `Card` | OK | |
| Constructeur avec `durability` et `effect` | OK | |
| Validation `durability > 0` | OK | `AttributeError` leve si invalide |
| `play()` implementee | OK | Retourne un dict complet |
| `activate_ability()` implementee | OK | Decremente la durabilite a chaque activation |

---

## Deck.py

| Point | Statut | Commentaire |
|---|---|---|
| `__init__` present | OK | Corrige |
| `add_card()` fonctionnel | OK | |
| `remove_card()` | OK | Corrige : `card.name == card_name` + `list.remove(card)` |
| `shuffle()` | OK | |
| `draw_card()` | OK | |
| `get_deck_stats()` cles conformes | OK | `total_cards`, `creatures`, `spells`, `artifacts`, `avg_cost` |
| `avg_cost` | OK | Corrige : `sum(...) / len(self.list_card)` |

---

## main.py

| Point | Statut | Commentaire |
|---|---|---|
| Demo fonctionnelle | OK | Le script s'execute sans erreur |
| Deck de 20 cartes avec les 3 types | OK | |
| `enemy_deck` initialise avant les `play()` | OK | |
| Polymorphisme illustre | OK | Les 3 types de cartes sont joues |

---

## Output obtenu

```
=== DataDeck Deck Builder ===

Building deck with different card types...
Deck stats: {'total_cards': 20, 'creatures': 5, 'spells': 10, 'artifacts': 5, 'avg_cost': 32.75}

...

Time to Play:

{'card_played': 'Stone Curse', 'mana_used': 35, 'effect': 'no creature targets'}
{'card_played': 'Lava Field', 'mana_used': 50, 'durability': 2, 'active effect': 'Lava flood the field, every target who get hit take x1,5 more damage'}
{'card_played': 'Venom Field', 'mana_used': 30, 'durability': 5, 'active effect': 'inflict damage to every card each turn'}

Polymorphism in action: Same interface, different card behaviors!
```

---

## Note ex1

| Critere | Points |
|---|---|
| Structure projet / imports | 2/2 |
| SpellCard.py (heritage, methodes) | 4/4 |
| ArtifactCard.py (heritage, methodes, validation) | 4/4 |
| Deck.py (methodes, logique) | 5/5 |
| main.py (demo fonctionnelle, polymorphisme) | 2/2 |
| Qualite du code (flake8, types, style) | 3/3 |
| **Total** | **20/20** |

---

# Exercise 2 : Ability System

## Vue d'ensemble

Le code tourne sans crash, flake8 passe sans erreur. Heritage multiple correct, toutes les methodes abstraites sont implementees.

---

## Structure du projet

- Arborescence conforme (`ex2/__init__.py`, `Combatable.py`, `Magical.py`, `EliteCard.py`, `main.py`) : OK
- Execution depuis la racine avec `python3 -m ex2.main` : OK
- Import depuis ex0 et imports relatifs corrects : OK
- Flake8 : OK

---

## Combatable.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `ABC` | OK | |
| `@abstractmethod` sur les 3 methodes | OK | `attack`, `defend`, `get_combat_stats` |
| Signatures conformes au sujet | OK | |

---

## Magical.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `ABC` | OK | |
| `@abstractmethod` sur les 3 methodes | OK | `cast_spell`, `channel_mana`, `get_magic_stats` |
| Signatures conformes au sujet | OK | |

---

## EliteCard.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage multiple `Card, Magical, Combatable` | OK | |
| Constructeur avec attributs pertinents | OK | `health`, `damage`, `defense`, `mana` |
| `play()` implementee | OK | Retourne un dict dans tous les cas, espace corrige |
| `attack()` implementee | OK | Gere le cas `target=None` |
| `defend()` implementee | OK | Logique de blocage correcte |
| `cast_spell()` implementee | OK | Gere le mana insuffisant |
| Filtre `isinstance(target, (EliteCard, CreatureCard))` | OK | Accepte les deux types |
| Cle `"targets"` (pluriel) dans les deux branches | OK | Corrige |
| `channel_mana()` implementee | OK | Gere le cas non-`int` |
| `get_combat_stats()` implementee | OK | Retourne `health`, `damage`, `defense` |
| `get_magic_stats()` implementee | OK | Retourne `mana` |

---

## main.py

| Point | Statut | Commentaire |
|---|---|---|
| Demo fonctionnelle | OK | S'execute sans erreur |
| Affichage des methodes par interface | OK | Utilisation de `dir()` sur chaque classe |
| Combat phase illustree | OK | `attack()` et `defend()` demontrees |
| Magic phase illustree | OK | `cast_spell()` et `channel_mana()` demontrees |
| Theme Overwatch (Roadhog / Doomfist) | OK | Liberte creative coherente |

---

## Output obtenu

```
=== DataDeck Ability System ===

EliteCard capabilities:
['get_card_info', 'is_playable', 'play']
['attack', 'defend', 'get_combat_stats']
['cast_spell', 'channel_mana', 'get_magic_stats'] 

Playing Arcane Warrior (Elite Card):

Combat phase:
Attack result: {'attacker': 'Roadhog', 'target': 'Doomfist', 'damage': 94, 'combat_type': 'shotgun'}
Defense result: {'defender': 'Roadhog', 'damage_taken': 36, 'damage_blocked': 36, 'still_alive': True}

Magic phase:
Spell cast: {'caster': 'Roadhog', 'spell': 'chain hook', 'targets': ['Doomfist', 'Roadhog'], 'mana_used': 2}
Mana channel: {'channeled': 4, 'total_mana': 12}

Multiple interface implementation successful!
```

---

## Note ex2

| Critere | Points |
|---|---|
| Structure projet / imports | 2/2 |
| Combatable.py (ABC, methodes abstraites) | 3/3 |
| Magical.py (ABC, methodes abstraites) | 3/3 |
| EliteCard.py (heritage multiple, implementations) | 8/8 |
| main.py (demo fonctionnelle, interfaces illustrees) | 2/2 |
| Qualite du code (flake8, types, style) | 2/2 |
| **Total** | **20/20** |

---

# Exercise 3 : Game Engine

## Vue d'ensemble

Le code tourne sans crash. Les deux design patterns (Abstract Factory + Strategy) sont correctement implementes. Quelques methodes non implementees (`get_strategy_name`, `prioritize_targets`) retournent `None` implicitement mais ne bloquent pas l'execution.

---

## Structure du projet

- Arborescence conforme (`ex3/__init__.py`, `GameStrategy.py`, `CardFactory.py`, `AggressiveStrategy.py`, `FantasyCardFactory.py`, `GameEngine.py`, `main.py`) : OK
- Execution depuis la racine avec `python3 -m ex3.main` : OK
- Imports absolus depuis ex0/ex1/ex2 : OK

---

## GameStrategy.py / CardFactory.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `ABC` | OK | |
| Toutes les methodes en `@abstractmethod` | OK | |
| Signatures conformes au sujet | OK | |

---

## AggressiveStrategy.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `GameStrategy` | OK | |
| `execute_turn()` : tri par `cost` puis boucle | OK | Joue les cartes les moins cheres en premier |
| Retourne `hand` et `battlefield` | OK | |
| `get_strategy_name()` | Non implemente | Retourne `None` (pas bloquant ici) |
| `prioritize_targets()` | Non implemente | Retourne `None` (pas bloquant ici) |

---

## FantasyCardFactory.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `CardFactory` | OK | |
| Dictionnaires de cartes (creature, spell, artifact) | OK | Noms creatifs |
| `create_creature()`, `create_spell()`, `create_artifact()` | OK | Selection aleatoire ou par nom |
| `create_themed_deck(size)` | OK | Genere un mix aleatoire |
| `get_supported_types()` | OK | Retourne les cles de chaque dict |

---

## GameEngine.py

| Point | Statut | Commentaire |
|---|---|---|
| `configure_engine()` stocke `factory` et `strategy` | OK | |
| `simulate_turn()` cree un deck et calcule les stats | OK | |
| `damage_dealt` avec `isinstance(cards, ...)` | OK | Bug corrige (etait `card.values()`) |
| `get_engine_status()` | OK | Retourne rapport complet |
| Compteurs `self.turn`, `self.total_dmg`, `self.card_created` | OK | Tracked correctement |

> **Point cosmetique** : Dans `simulate_turn`, la variable `dmg` est recalculee inutilement a chaque iteration du for - le `sum()` porte sur tout le deck a chaque fois. Pas de bug mais la boucle for ne sert qu'a construire `cards_name`.

---

## main.py

| Point | Statut | Commentaire |
|---|---|---|
| Demo fonctionnelle | OK | S'execute sans erreur |
| Affichage de la hand avec `join` | OK | Format `[Nom (cout), ...]` |
| `configure_engine()` + `simulate_turn()` + `get_engine_status()` | OK | Chaine complete demontree |

---

## Note ex3

| Critere | Points |
|---|---|
| Structure projet / imports | 2/2 |
| GameStrategy.py + CardFactory.py (abstractions) | 4/4 |
| AggressiveStrategy.py (logique de jeu) | 4/5 |
| FantasyCardFactory.py (creation cartes, themed deck) | 5/5 |
| GameEngine.py (orchestration) | 4/4 |
| main.py (demo complete) | 2/2 |
| **Total** | **21/22** |

---

# Exercise 4 : Tournament Platform

## Vue d'ensemble

Le code tourne sans crash. L'heritage multiple `Card + Combatable + Rankable` est correctement mis en oeuvre. Le systeme de rating et de leaderboard fonctionne. Quelques petits points cosmetiques.

---

## Structure du projet

- Arborescence conforme (`ex4/__init__.py`, `Rankable.py`, `TournamentCard.py`, `TournamentPlatform.py`, `main.py`) : OK
- Execution depuis la racine avec `python3 -m ex4.main` : OK
- Imports depuis ex0 et ex2 corrects : OK

---

## Rankable.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage de `ABC` | OK | |
| 4 methodes en `@abstractmethod` | OK | |
| Signatures conformes au sujet | OK | |

---

## TournamentCard.py

| Point | Statut | Commentaire |
|---|---|---|
| Heritage multiple `Card, Combatable, Rankable` | OK | |
| `play()` implementee | OK | |
| `attack()` : compare `atk`, met a jour wins/losses | OK | Bug `self.wins` corrige -> `self.win` |
| `defend()` | OK | Logique cohérente |
| `calculate_rating()` | OK | Calcul base sur `atk` et `cost` |
| `update_wins()` : `+16` au rating | OK | |
| `update_losses()` : `-16` au rating | OK | |
| `get_tournament_stats()` avec `__bases__` | OK | Affiche les classes parentes |
| `get_rank_info()` | Non implemente | Retourne `None` |
| `get_combat_stats()` | OK | Retourne `atk` |

---

## TournamentPlatform.py

| Point | Statut | Commentaire |
|---|---|---|
| `register_card()` | OK | Ajoute a la liste et retourne l'ID |
| `create_match()` | OK | Retourne `first / VS / second` |
| `get_leaderboard()` | OK | Tri par `rate` descendant |
| `generate_tournament_report()` | OK | Calcul avg_rating correct |
| Typo `"platfrom_status"` | A corriger | Devrait etre `"platform_status"` |

---

## main.py

| Point | Statut | Commentaire |
|---|---|---|
| Demo fonctionnelle | OK | S'execute sans erreur |
| Cartes generees aleatoirement | OK | Rejouabilite |
| Noms de cartes creatifs | OK | Liberte assumee et coherente |
| Leaderboard avec `enumerate` | OK | Format `1. Nom - Rating: X (W-L)` |
| Rapport final affiche | OK | |

---

## Note ex4

| Critere | Points |
|---|---|
| Structure projet / imports | 2/2 |
| Rankable.py (ABC, methodes abstraites) | 3/3 |
| TournamentCard.py (heritage multiple, logique) | 8/9 |
| TournamentPlatform.py (gestion plateforme) | 4/5 |
| main.py (demo complete) | 2/2 |
| **Total** | **19/21** |

---

# Recapitulatif global

| Exercice | Note | Etat |
|---|---|---|
| ex0 - Card Foundation | 16/16 | Complet |
| ex1 - Deck Builder | 20/20 | Complet |
| ex2 - Ability System | 20/20 | Complet |
| ex3 - Game Engine | 21/22 | Complet |
| ex4 - Tournament Platform | 19/21 | Complet |
| **Total** | **96/99** | |

---

## Points a ameliorer (non bloquants)

- **ex3** `AggressiveStrategy` : implementer `get_strategy_name()` et `prioritize_targets()`
- **ex3** `GameEngine.simulate_turn()` : le calcul de `dmg` dans la boucle for est redondant
- **ex4** `TournamentCard.get_rank_info()` : non implementee (retourne `None`)
- **ex4** `TournamentPlatform` : typo `"platfrom_status"` -> `"platform_status"`

> Exercice solide. L'architecture ABC est bien comprise, les cas d'erreur sont geres proprement, et le code est conforme flake8. Le seul point cosmetique restant (variable `playable` intermediaire dans `is_playable`) n'est absolument pas bloquant.
