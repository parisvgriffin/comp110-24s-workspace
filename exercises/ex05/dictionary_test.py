"""Unit tests for the functions in exercises.ex05.dictionary."""

__author__ = "730558866"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

# Testing for invert

import pytest


def test_invert_use_case1() -> None:
    """Testing invert with expected use case."""
    words = {'1': 'Alice', '2': 'Bob', '3': 'Charlie'}
    inverted = invert(words)
    expected_output = {'Alice': '1', 'Bob': '2', 'Charlie': '3'}
    assert inverted == expected_output


def test_invert_use_case2() -> None:
    """Testing invert with another expected use case."""
    inp_dict = {'fruit': 'apple', 'meat': 'beef', 'vegetable': 'carrot'}
    groceries = invert(input)
    assert groceries == {'apple': 'fruit', 'beef': 'meat', 'carrot': 'vegetable'}


def test_invert_edge_case() -> None:
    """Testing invert with an unexpected edge case."""
    words = {}
    inverted = invert(words)
    assert inverted == {}


# Testing for favorite_color


def test_favorite_color_use1() -> None:
    """Testing favorite_color with expected use case."""
    colors = {'red': '1', 'blue': '2', 'green': '3', 'red2': '4', 'blue2': '5', 'green2': '6', 'red3': '7'}
    assert favorite_color(colors) == 'red'


def test_favorite_color_use2() -> None:
    """Testing favorite_color with another expected use case."""
    colors = {'Mark': 'red', 'David': 'blue', 'Jacob': 'green', 'Tanner': 'red', 'Caroline': 'blue', 'green2': '6', 'red3': '7', 'blue3': '8'}
    assert favorite_color(colors) == 'red'


def test_favorite_color_edge() -> None:
    """Testing favorite_color with an unexpected edge case."""
    colors = {}
    assert favorite_color(colors) == ''


# Testing cases for count


def test_count_use_case1() -> None:
    """Testing count with expected use case."""
    inp_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    assert count(inp_list) == {'apple': 3, 'banana': 2, 'orange': 1}


def test_count_use_case2() -> None:
    """Testing count with another expected use case."""
    inp_list = ['a', 'b', 'c', 'd', 'a', 'b', 'c']
    assert count(inp_list) == {'a': 2, 'b': 2, 'c': 2, 'd': 1}


def test_count_edge_case() -> None:
    """Testing count function with an unexpected edge case."""
    inp_list = []
    assert count(inp_list) == {}


# Testing cases for alphabetize


def test_alphabetize_use_case1() -> None:
    """Testing alphabetize with an expected use case."""
    words = ["Apple", "Brown", "Color", "Door", "Elephant"]
    letter_groups = alphabetizer(words)
    print("Words organized by first letter:")
    for letter, words in letter_groups.items():
        print(f"Words starting with '{letter}': {words}")


def test_alphabetize_use_case2() -> None:
    """Testing alphabetize with another expected use case."""
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    name_group = alphabetizer(names)
    print("Words organized by first letter:")
    for letter, names in name_group.items():
        print(f"Words starting with '{letter}': '{names}'")


def test_alphabetize_edge_case() -> None:
    """Testing alphabetize with an unexpected edge case."""
    empty_list = []
    empty_result = alphabetizer(empty_list)
    print("Empty Word list resulted", empty_result)


# Testing cases for update_attendance
    

def test_update_attendance_use_case1() -> None:
    """Testing update_attendance with an expected use case."""
    attendance = {'Monday': ['Paris', 'Jack'], 'Tuesday': ['Elena']}
    update_attendance(attendance, 'Wednesday', 'Rachel')
    assert attendance == {'Monday': ['Paris', 'Jack'], 'Tuesday': ['Elena'], 'Wednesday': ['Rachel']}


def test_update_attendance_use_case2() -> None:
    """Testing update_attendance with another expected use case."""
    attendance = {'Monday': ['Paris', 'Jack'], 'Tuesday': ['Elena']}
    update_attendance(attendance, 'Monday', 'Rachel')
    assert attendance == {'Monday': ['Paris', 'Jack', 'Rachel'], 'Tuesday': ['Elena']}


def test_update_attendance_edge_case() -> None:
    """Testing update_attendance with an unexpected edge case."""
    attendance = {}
    update_attendance(attendance, 'Monday', 'Paris')
    assert attendance == {'Monday': ['Paris']}