"""Test my garden functions."""

__author__ = "730558866"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

# testing add_by_kind


def test_add_by_kind_edge():
    """Testing add_by_kind by using an innapropriate edge case."""
    by_kind = {}
    new_plant_kind = "flower"
    new_plant = "rose"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert new_plant_kind in by_kind
    assert by_kind[new_plant_kind] == [new_plant]


def test_add_by_kind_use():
    """Testing add_by_kind by using an appropriate use case."""
    by_kind = {"vegetable": ["carrot", "tomato"]}
    new_plant_kind = "flower"
    new_plant = "daisy"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert new_plant_kind in by_kind
    assert by_kind[new_plant_kind] == [new_plant]


# testing add_by_date
def test_add_by_date_edge():
    """Testing add_by_date by using an innapropriate edge case."""
    garden_date = {}
    month = 'April'
    plant = 'rose'
    add_by_date(garden_date, month, plant)
    assert month in garden_date
    assert plant in garden_date[month]


def test_add_by_date_use():
    """Testing add_by_date using an appropriate use case."""
    garden_date = {"May": ["daisy"]}
    month = "May"
    plant = "rose"
    add_by_date(garden_date, month, plant)
    assert month in garden_date
    assert plant in garden_date[month]


# testing lookup_by_kind_and_date
def test_lookup_by_kind_and_date_edge():
    """Testing lookup_by_kind_and_date using an innapropriate edge case."""
    plant_kind = {}
    plant_date = {}
    kind = "flower"
    month = "April"
    result = lookup_by_kind_and_date(plant_kind, plant_date, kind, month)
    assert result == "No flowers to plant in April."


def test_lookup_by_kind_and_date_use():
    """Testing lookup_by_kind_and_date using an appropriate use case."""
    plant_kind = {"flower": ["rose", "daisy"], "vegetable": ["carrot"]}
    plant_date = {"April": ["rose", "carrot"], "May": ["daisy"]}
    kind = "flower"
    month = "April"
    result = lookup_by_kind_and_date(plant_kind, kind, month, plant_date)
    assert result == "flowers to plant in April: ['rose]"


if __name__ == "__main__":
    test_add_by_kind_edge()
    test_add_by_kind_use()
    test_add_by_date_edge()
    test_add_by_date_use()
    test_lookup_by_kind_and_date_use()
    test_lookup_by_kind_and_date_edge()