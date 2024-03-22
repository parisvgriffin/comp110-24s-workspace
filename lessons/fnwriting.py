"""Practicing for COMP quiz."""

def sum(nums: list[int]) -> int:
    total: int = 0.0
    idx: int = 0
    while idx < len(nums):
        total += nums[idx]
        idx += 1
    return total

def count_even(nums: list[int]) -> int:
    idx_count: int = 0
    for num in nums:
        if num % 2 == 0:
            idx_count += 1
    return idx_count


def average_list(nums:list[int]) -> float:
    """Returning the average list of elements."""
    total: int = 0
    for num in nums:
       total += nums
    if len(nums) != 0:
        return total/len(nums)
    else:
        return 0
    
def odd_and_even(inp_list:list[int]) -> list[int]:
    """Returning inps elements that are odd and have an even index."""
    new_list: list[int] = []
    idx: int = 0
    while i < len(inp_list):
        if inp_list[idx] % 2 == 1 and idx % 2 == 0:
            new_list.append(inp_list[idx])
        i += 1
    return new_list

def short_words(words:list[str]) -> list[str]:
    """Returning a list of words less than five characters long."""
    short_words: list[str] = []
    for idx in words:
        if len(words[idx]) < 5:
            short_words.append(words[idx])
        else:
            print("Error! Word was too long.")
        idx += 1