# Feedback P09 — Cosmic Data (Pydantic)

---

## Note globale : 10 / 10

Travail excellent et complet. Tous les exercices sont fonctionnels, conformes au sujet, et passent mypy et flake8.

---

## Ex0 — Space Station Data : 10 / 10

### Ce qui est bien
- Tous les champs requis sont présents avec les bonnes contraintes `Field`.
- Syntaxe moderne Python 3.10+ utilisée (`str | None`) plutôt que `Optional` — bon réflexe.
- Le `try/except ImportError` pour pydantic est une touche de robustesse appréciable.
- Le cas invalide (`power_level: 11037`) déclenche bien la `ValidationError`.
- Le `crew_size` passé en string `"13"` illustre bien la coercition automatique de Pydantic.
- Annotations de type correctes ✅
- mypy ✅ | flake8 ✅

---

## Ex1 — Alien Contact Logs : 10 / 10

### Ce qui est bien
- Les 4 validators `@model_validator(mode="after")` couvrent les 4 règles métier.
- La comparaison Enum est correcte (`ContactType.physical`, `ContactType.telepathic`).
- Le 2ème contact (telepathic, 2 témoins) déclenche bien l'erreur attendue.
- `alien.contact_type.name` utilisé correctement pour afficher la valeur de l'enum.
- `message_received: Optional[str] = Field(default=None, max_length=500)` ✅
- Annotations de type correctes (`-> Self`) ✅
- mypy ✅ | flake8 ✅

---

## Ex2 — Space Crew Management : 10 / 10

### Ce qui est bien
- Les modèles imbriqués `CrewMember` / `SpaceMission` sont bien structurés.
- Les 4 validators sont tous présents et fonctionnels.
- `verif_for_exp` retourne bien `self` dans tous les cas.
- Le 2ème mission (sans captain/commander) déclenche correctement l'erreur.
- `member.rank.name` correctement utilisé dans l'affichage.
- Annotations de type correctes (`-> Self`) ✅
- mypy ✅ | flake8 ✅

---

## Points généraux

| Critère | Statut |
|---|---|
| Pydantic v2 utilisé | ✅ |
| `@model_validator(mode="after")` | ✅ |
| Enum pour les types | ✅ |
| Cas valide + cas invalide démontrés | ✅ |
| `ValidationError` catchée proprement | ✅ |
| `venv` configuré | ✅ |
| Annotations de type sur les fonctions | ✅ |
| Conformité flake8 | ✅ |
| mypy sans erreurs | ✅ |
