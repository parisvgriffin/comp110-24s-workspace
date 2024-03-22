"""Test sum functionality."""

from lessons.sum import new_su

def test_sum_empty() -> None:
    assert sum([]) == 0
