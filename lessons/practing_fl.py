"""Summing the elements of a list using different loops."""

__author__ = "730558866"

def w_sum(vals: list[float]) -> int:
    sum: int = 0.0
    i: int = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum
