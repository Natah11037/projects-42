def ft_seed_inventory(seed_type: str, quant: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quant} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quant} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quant} square meters")
    else:
        print("Unknown unit type")
