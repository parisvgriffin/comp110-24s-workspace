
"""Working with Dictionaries."""

__author__ = "730558866"


def invert(words: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values."""
    inverted_dict: dict[str, str] = {}  # new string
    # need to make sure key values are unique
    for key in words:
        if words[key] in inverted_dict:  # keys turn into values so we have to check values.
            raise KeyError("Error! Keys cannot be duplicated within the dictionary.")
        else: 
            inverted_dict[words[key]] = key
    return inverted_dict
 

def favorite_color(colors: dict[str, str]) -> str:
    """Returning the most frequent color."""
    color_count: dict[str, int] = {}
    max_count: int = 0
    popular_color: str = ""
    for color in colors:
        if colors[color] in color_count:
            color_count[colors[color]] += 1
        else:
            color_count[colors[color]] = 1
    for color in color_count:
        if color_count[color] > max_count:
            popular_color = color
            max_count = color_count[color]
    return popular_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Number of times value appears on input list."""
    freq_dict: dict[str, int] = {}
    for item in inp_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Unique letters and values that begin with the letter."""
    result_dict: dict[str, list[str]] = {}
    
    for word in words:
        first_letter = word[0].lower()
        if first_letter in result_dict:
            result_dict[first_letter].append(word)
        else:
            result_dict[first_letter] = [word]
    return result_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updating attendance with new info by mutating."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]