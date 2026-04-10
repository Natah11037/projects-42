def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact:
                  artifact["power"] if "power" in artifact else 0,
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage:
                       mage["power"] >= min_power,
                       mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "Most powerful mage": max(mages, key=lambda most: most["power"]),
        "Least powerful mage": min(mages, key=lambda least: least["power"]),
        "average power": sum(mage["power"] for mage in mages) / len(mages)
    }


def main():
    mages = [
        {
            "name": "Henry Potd'Beurre",
            "power": 67,
            "type": "a trulymero trulicina magician"
        },
        {
            "name": "Mauga",
            "power": 666,
            "type": "Win condition"
        },
        {
            "name": "la Trott de Gautier",
            "power": 500,
            "type": "divine beast of speed"
        },
        {
            "name": "Cihan-GPT",
            "power": 255,
            "type": "the maximum of the universe"
        }
    ]
    spells = [
        "invisiblum",
        "teleportum",
        "brulum",
        "gelum",
        "lumierum",
        "forcum",
        "vitessum",
        "bouclium",
        "healum",
        "volum",
        "electrum",
        "tempum"
    ]
    print("\nTesting artifact sorter...")
    try:
        sorted_list = artifact_sorter(mages)
    except TypeError:
        print("Error: A value of one of your data is invalid please"
              " recheck one time")
        exit(1)
    len_sorted_list = len(sorted_list)
    for mage in sorted_list:
        if len_sorted_list == len(sorted_list):
            print(f"{mage['name']} ({mage['power']} power)"
                  f" comes before ", end="")
        elif len_sorted_list > 1:
            print(f"{mage['name']} ({mage['power']} power)"
                  f" which comes before ", end="")
        else:
            print(f"{mage['name']} ({mage['power']} power)\n")
        len_sorted_list += -1

    print("Testing power filter...")
    try:
        sorted_and_filtered = power_filter(sorted_list, 100)
    except TypeError:
        print("Error: A value of one of your data is invalid please"
              " recheck one time")
        exit(1)
    len_sort_filter = len(sorted_and_filtered)
    for mage in sorted_and_filtered:
        if len_sort_filter > 2:
            print(f"{mage['name']} ({mage['power']} power), ", end="")
        elif len_sort_filter == 2:
            print(f"{mage['name']} ({mage['power']} power) and ", end="")
        else:
            print(f"{mage['name']} ({mage['power']} power)\n")
        len_sort_filter += -1

    print("Testing spell transformer...")
    try:
        new_spells = spell_transformer(spells)
    except TypeError:
        print("Error: A value of one of your data is invalid please"
              " recheck one time")
        exit(1)
    for spell in new_spells:
        print(spell, end=" ")
    print("\n")

    print("Testing mage stats...")
    try:
        stats = mage_stats(mages)
    except TypeError:
        print("Error: A value of one of your data is invalid please"
              " recheck one time")
        exit(1)
    print(f"Most powerful mage: {stats['Most powerful mage']['name']}"
          f" ({stats['Most powerful mage']['power']} power),"
          f" {stats['Most powerful mage']['type']}")
    print(f"Least powerful mage: {stats['Least powerful mage']['name']}"
          f" ({stats['Least powerful mage']['power']} power),"
          f" {stats['Least powerful mage']['type']}")
    print(f"Average power: {stats['average power']}")


if __name__ == "__main__":
    main()
