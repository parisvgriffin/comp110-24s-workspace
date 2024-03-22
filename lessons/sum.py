"""Writing the same function in three different ways."""


def w_sum(vals: list[float]) -> float:
    """Running a while loop for my list and range."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Running a for and in loop for my list and range."""
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Running a for and in loop for my list and range."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total