"""Some functions for my garden plan!"""

__author__ = "730558866"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant under its kind."""
    # if the kind is already in the dictionary ('flower' is in by_kind, so I did this)
    if new_plant_kind in by_kind: 
        by_kind[new_plant_kind].append(new_plant)
    else:  # if the kind is not in the dictionary (e.g. "fruit" is not in by_kind)
        by_kind[new_plant_kind] = []
    by_kind[new_plant_kind].append(new_plant)


def add_by_date(garden_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in garden_date:
        garden_date[month].append(plant)
    else:
        garden_date[month] = []
        garden_date[month].append(plant)


def lookup_by_kind_and_date(plant_kind: dict[str, list[str]], plant_date: dict[str, list[str]], kind: str, month: str):
    """Return string with list of plants of a specific kind to plant in a specific month."""
    assert kind in plant_kind
    assert month in plant_date
    # get a list of all plants of the specific kind input
    if kind in plant_kind:
        kind_list: list[str] = plant_kind[kind]
    # get a list o fll plants of the specific month
    month_list: list[str] = plant_date[month]
    # go through both lists and find elements that appear in both
    # say kind_list = ["marigold", "daisy"]
    # month_list = ["daisy","rose"]
    combined_list: list[str] = []   # if we put this in it, it would reset the variable value
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:   # plant is in both kind_list and month_list
                combined_list.append(other_plant)
    # "<kind>s to plant in <month>: <combined_list>"
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {kind}s to plant in {month}."
    