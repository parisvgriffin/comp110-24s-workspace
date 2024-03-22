"""Splitting a dictionary into two lists."""

__author__ = "730558866"


def get_keys(my_dict: dict[str, int]) -> list[str]:
    """Producing an empty list of values in dict."""
    list1: list[str] = []
    for key in my_dict:
        list1.append(key)
    return list1


def get_values(dict2: dict[str, int]) -> list[int]:
    """Producing a list of all the values of in dict."""
    list2: list[int] = []
    for key in dict2:
        list2.append(dict2[key])
    return list2