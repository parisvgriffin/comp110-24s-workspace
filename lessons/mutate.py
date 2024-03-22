"""Mutating Functions."""

__author__ = "730558866"

# part 1


def manual_append(word: list[int], i: int) -> None:
    """Defining manual_append."""
    word.append(i)


def double(word2: list[int]) -> None:
    """List with double."""
    int_counter: int = 0
    while int_counter < len(word2):
        word2[int_counter] *= 2
        int_counter += 1 
    


    
