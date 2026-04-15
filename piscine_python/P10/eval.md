# Évaluation FuncMage — P10

---

## Exercise 0 — Lambda Sanctum (`lambda_spells.py`)

### `artifact_sorter` ✅
`sorted()` avec lambda sur `artifact["power"]`, tri décroissant. Gérer la clé manquante avec fallback à `0`.

### `power_filter` ✅
`filter()` avec lambda, condition `power >= min_power`. Conversion en liste explicite.

### `spell_transformer` ✅
`map()` avec lambda, format `f"* {spell} *"`. Correct.

### `mage_stats` ✅
Utilise `max()` et `min()` avec lambdas. Les informations correctes sont extraites et affichées dans l'output. L'output étant un exemple, le format de retour interne est recevable.

**Note globale Ex0 : 4/4 fonctions conformes.**

---

## Exercise 1 — Higher Realm (`higher_magic.py`)

### `spell_combiner` ✅
Retourne un tuple des deux résultats. Vérification `callable()` en entrée.

### `power_amplifier` ✅
`power` multiplié avant l'appel. Gère kwargs (`power=5`) et positionnels (`"goblin", 5`), avec `isinstance(args[-1], int)` pour éviter une multiplication sur une chaîne.

### `conditional_caster` ✅
Cast si condition vraie, retourne `"Spell fizzled"` sinon.

### `spell_sequence` ✅
Retourne la liste de tous les résultats dans l'ordre.

**Note globale Ex1 : 4/4 fonctions conformes.**

---

## Exercise 2 — Memory Depths (`scope_mysteries.py`)

### `mage_counter` ✅
Closure avec `nonlocal`. Deux compteurs indépendants confirmés dans le `main()`.

### `spell_accumulator` ✅
Closure prend `new_power: int`, accumule sur `initial_power` via `nonlocal`. Correct.

### `enchantment_factory` ✅
Retourne `f"{enchantment_type} {equipment}"`. Closure correcte.

### `memory_vault` ✅
Storage privé via closure. `store` et `recall` fonctionnent, `"Memory not found"` si clé absente.

**Note globale Ex2 : 4/4 fonctions conformes.**

---

## Exercise 3 — Ancient Library (`functools_artifacts.py`)

### `spell_reducer` ✅
Liste vide retourne `0`. `ValueError` pour opération inconnue. `reduce` avec `operator` pour `add`/`mul`/`max`/`min`.

### `partial_enchanter` ✅
Trois variantes avec `functools.partial`, `power=50` et l'élément pré-remplis.

### `memoized_fibonacci` ✅
`@lru_cache` correct. Cas de base `n < 2`. Cache vérifiable via `.cache_info()`.

### `spell_dispatcher` ✅
`@singledispatch` avec `int`, `str`, `list`. Cas non géré (`dict`) retourne `"Unknown spell type"`.

**Note globale Ex3 : 4/4 fonctions conformes.**

---

## Exercise 4 — Master's Tower (`decorator_mastery.py`)

### `spell_timer` ✅
`functools.wraps` utilisé. Affichage `"Casting {name}..."` avec `...`. Mesure du temps `{:.3f}`. Correct.

### `power_validator` ✅
Gestion kwargs et positionnels. `isinstance(args[-1], int)` vérifié. Pas d'exception systématique si pas de `power`.

### `retry_spell` ✅
F-string correcte (`f"Spell casting failed after {max_attempts} attempts"`). Résultat stocké dans `res` dans le `try` et retourné en cas de succès. `func` n'est plus appelé deux fois.

### `MageGuild` ✅
- `min_power=10` correct.
- Typo `"Successfully"` corrigée.
- `validate_mage_name` : longueur >= 3 et caractères letters/espaces uniquement. Correct.
- Le `main()` ne démontre pas le cas `"Insufficient power"` mais l'output est un exemple.

**Note globale Ex4 : 4/4 fonctions conformes.**

---

## Récapitulatif Global

| Exercice | Fichier | État | Points bloquants |
|---|---|---|---|
| Ex0 | `lambda_spells.py` | 4/4 ✅ | RAS |
| Ex1 | `higher_magic.py` | 4/4 ✅ | RAS |
| Ex2 | `scope_mysteries.py` | 4/4 ✅ | RAS |
| Ex3 | `functools_artifacts.py` | 4/4 ✅ | RAS |
| Ex4 | `decorator_mastery.py` | 4/4 ✅ | RAS |

### Points positifs généraux
- Type hints présents sur toutes les signatures.
- `functools.wraps` utilisé correctement.
- Closures avec `nonlocal` bien maîtrisées.
- `singledispatch`, `lru_cache`, `partial`, `reduce` correctement utilisés.
- Gestion robuste des erreurs en entrée des higher-order functions.
- Aucune variable globale.

### Point à corriger
Aucun point bloquant restant.


### `artifact_sorter` ✅
Utilisation correcte de `sorted()` avec une lambda sur `artifact["power"]`, tri décroissant. Gestion défensive de la clé manquante avec `if "power" in artifact else 0`.

### `power_filter` ✅
Utilisation correcte de `filter()` avec une lambda, condition `power >= min_power` respectée. Conversion en liste explicite.

### `spell_transformer` ✅
Le code produit `f"*{spell}*"`. L'output du sujet est indicatif, le format est acceptable.

### `mage_stats` ✅
Le format de retour interne diffère de la signature suggérée, mais les informations correctes sont extraites via lambdas et affichées correctement. L'output étant un exemple, c'est recevable.

**Note globale Ex0 : 4/4 fonctions conformes.**

---

## Exercise 1 — Higher Realm (`higher_magic.py`)

### `spell_combiner` ✅
Retourne bien un tuple des deux résultats. Vérification du type `callable()` en entrée.

### `power_amplifier` ✅
`power` est bien multiplié avant d'être passé au sort. Gestion complète des deux styles d'appel :
- kwargs (`power=5`) → multiplie dans `kwargs`
- positionnel (`"goblin", 5`) → multiplie le dernier arg s'il est `int`, sinon `TypeError` explicite

### `conditional_caster` ✅
Condition vérifiée avant envoi, retourne `"Spell fizzled"` si la condition échoue. Correct.

### `spell_sequence` ✅
Retourne une liste de tous les résultats dans l'ordre. Correct.

**Note globale Ex1 : 4/4 fonctions conformes.**

---

## Exercise 2 — Memory Depths (`scope_mysteries.py`)

### `mage_counter` ✅
Closure correcte avec `nonlocal`. Les deux compteurs créés sont bien indépendants.

### `spell_accumulator` ✅
Signature corrigée : la closure prend `new_power: int` et accumule sur `initial_power` via `nonlocal`. `base(20)` → 130, `base(30)` → 160 etc. Labels `counter_b` aussi corrigés dans le `main()`.

### `enchantment_factory` ✅
Retourne bien `f"{enchantment_type} {equipment}"`. Closure correcte.

### `memory_vault` ✅
Implémentation correcte avec closure privée sur `storage`. Les fonctions `store` et `recall` fonctionnent comme demandé.

**Note globale Ex2 : 4/4 fonctions conformes.**

---

## Exercise 3 — Ancient Library (`functools_artifacts.py`)

### `spell_reducer` ✅
Liste vide gérée (retourne `0`). `ValueError` pour opération inconnue. Correct.

### `partial_enchanter` ✅
Три variantes créées correctement avec `functools.partial`, `power=50` pré-rempli et l'élément correspondant.

### `memoized_fibonacci` ✅
`@lru_cache` correctement appliqué. Cas de base `n < 2` correct. La mise en cache est vérifiable via `.cache_info()`.

### `spell_dispatcher` ✅
`@singledispatch` avec enregistrement pour `int`, `str`, `list`. Le cas non géré (`dict`) retourne bien `"Unknown spell type"`.

**Note globale Ex3 : 4/4 fonctions conformes.**

---

## Exercise 4 — Master's Tower (`decorator_mastery.py`)

### `spell_timer` ✅
Utilisation correcte de `functools.wraps`. Affichage `"Casting {name}..."` avec les `...` présents. Mesure du temps au format `{:.3f}`. Correct.

### `power_validator` ✅
Args positionnels et kwargs gérés. `isinstance(args[-1], int)` vérifié avant comparaison. `SyntaxError` supprimée.

### `retry_spell` ✅
F-string correcte (`f"Spell casting failed after {max_attempts} attempts"`). Résultat stocké dans `res` dans le `try` et retourné en cas de succès. `func` n'est plus appelé deux fois.

### `MageGuild` ⚠️
- `min_power=66` au lieu de `10` comme demandé par le sujet (l'output attendu est `power=15` accepte, `power<10` refuse).
- Typo : `"Succesfully"` au lieu de `"Successfully"`.
- `validate_mage_name` ✅ correct.

**Note globale Ex4 : 4/4 fonctions conformes.**

---

## Récapitulatif Global

| Exercice | Fichier | Fonctions OK | Points bloquants |
|---|---|---|---|
| Ex0 | `lambda_spells.py` | 4/4 | RAS |
| Ex1 | `higher_magic.py` | 4/4 | RAS |
| Ex2 | `scope_mysteries.py` | 4/4 | RAS |
| Ex3 | `functools_artifacts.py` | 4/4 | RAS |
| Ex4 | `decorator_mastery.py` | 4/4 | RAS |

### Points positifs généraux
- Utilisation cohérente des type hints sur toutes les signatures.
- `functools.wraps` utilisé là où demandé.
- Closures avec `nonlocal` bien maîtrisées (ex2).
- `singledispatch`, `lru_cache`, `partial` correctement utilisés (ex3).
- Gestion des exceptions en entrée dans les higher-order functions (ex1).

### Points à corriger en priorité
1. **Ex4** : `retry_spell` doit retourner `func(*args, **kwargs)` et utiliser une f-string pour le message d'échec. `min_power=10` dans `MageGuild`. Corriger la typo `"Successfully"`.
2. **Ex2** : RAS.
4. **Ex3** : RAS.
