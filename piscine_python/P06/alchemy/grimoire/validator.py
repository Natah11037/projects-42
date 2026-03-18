def validate_ingredients(ingredients: str) -> str:
    ingredient_lst: list[str] = []
    element = ["fire", "water", "earth", "air"]
    ingredient_lst = ingredients.split()
    for i in ingredient_lst:
        if i not in element:
            return "INVALID"
    return f"{ingredients} - VALID"
