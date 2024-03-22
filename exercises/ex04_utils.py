
"""Implementing lists into functions."""

__author__ = "730558866"


def all(nums: list[int], target: int) -> bool:
    """Check if nums are equal to target."""
    if not nums:
        return False
    index = 0
    while index < len(nums):
        if nums[index] != target:
            return False
        index += 1
    return True


def max(nums: list[int]) -> int:
    """Finding the maximum value."""
    maximum = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] > maximum:
            maximum = nums[index]
        index += 1
    return maximum


def is_equal(nums1: list[int], nums2: list[int]) -> bool:
    """Check if two lists are equal."""
    if len(nums1) != len(nums2):
        return False
    index = 0
    while index < len(nums1):
        if nums1[index] != nums2[index]:
            return False
        index += 1
    return True


def extend(nums1: list[int], nums2: list[int]) -> None:
    """Adding to the list."""
    index = 0
    while index < len(nums2):
        nums1.append(nums2[index])
        index += 1