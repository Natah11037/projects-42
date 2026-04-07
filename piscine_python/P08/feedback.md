# Feedback P08 — The Matrix

**Date :** 7 avril 2026  
**Notation globale : 27.5 / 30**

---

## Résumé général

| Exercice | Score | Statut |
|---|---|---|
| Ex0 – construct.py | 9.5 / 10 | Excellent, quasi-parfait |
| Ex1 – loading.py | 9 / 10 | Très bon |
| Ex2 – oracle.py | 9 / 10 | Très bon |
| **TOTAL** | **27.5 / 30** | |

---

## Ex0 — Entering the Matrix (`construct.py`) — 9.5 / 10

### ✅ Points positifs
- Détection du venv correcte via `sys.prefix != sys.base_prefix`.
- Nom du venv récupéré proprement avec `os.path.basename(sys.prefix)`.
- `Environment Path:` affiché dans la branche "inside venv". ✅
- `site.getsitepackages()[0]` avec `\n` — format correct. ✅
- Ligne Windows `matrix_env\Scripts\activate` présente. ✅
- Modules autorisés uniquement (`sys`, `os`, `site`).
- Flake8 : **0 erreur**. Mypy : **0 erreur**.

### ⚠️ Point mineur
La condition est évaluée deux fois consécutivement (d'abord pour définir `venv_name`, ensuite pour l'affichage). Pas une erreur, mais un simple `if/else` unique aurait été plus lisible. Aucun impact fonctionnel.

---

## Ex1 — Loading Programs (`loading.py`, `requirements.txt`, `pyproject.toml`) — 9 / 10

### ✅ Points positifs
- Utilisation de `importlib` pour les imports dynamiques : élégant et conforme.
- Données générées avec `numpy` (`rng.normal`, `np.arange`, `np.sin`) — pas de listes codées en dur. ✅
- Gestion des dépendances manquantes avec messages pour `pip` ET `poetry`.
- `requirements.txt` et `pyproject.toml` présents et cohérents.
- Docstring corrigée (une seule docstring multiligne propre). ✅
- `check_dependencies()` correctement défini et appelé. ✅
- Flake8 : **0 erreur**.

### ⚠️ Point mineur
La variable `pd` est importée via `importlib` mais utilisée sans annotation de type explicite — mypy ne peut pas inférer les types des modules chargés dynamiquement. Aucune erreur remontée car le sujet l'autorise explicitement pour les import errors. Aucun impact fonctionnel.

---

## Ex2 — Accessing the Mainframe (`oracle.py`, `.env.example`, `.gitignore`) — 9 / 10

### ✅ Points positifs
- `python-dotenv` utilisé correctement via `load_dotenv()`.
- Les 5 variables de configuration requises sont toutes gérées.
- Différenciation `development` / `production` visible dans la sortie. ✅
- Gestion d'erreur sur l'import de `dotenv` avec message utile.
- `.env.example` présent avec les 5 variables. ✅
- `.gitignore` dans `ex2/` contient `.env` — bonne pratique. ✅
- `def main() -> None:` — annotation de type présente. ✅
- Flake8 : **0 erreur**. Mypy : **0 erreur**.

### ⚠️ Point mineur
Le bloc `try/except ImportError` est placé au niveau module (hors de toute fonction). C'est fonctionnel, mais une convention plus courante serait de l'isoler dans un bloc `if __name__ == "__main__"` ou dans `main()` pour garder le module importable sans side-effect. Pas une erreur.

---

## Conseils pour la peer-review

- Savoir expliquer **pourquoi** `sys.prefix != sys.base_prefix` détecte un venv.
- Savoir expliquer la différence entre `pip` et `poetry` (lockfile, résolution des dépendances, environnements intégrés).
- Savoir expliquer **pourquoi** ne jamais commiter un `.env` (secrets, credentials, portabilité).
- Savoir expliquer la différence `development` vs `production` dans ton oracle.
