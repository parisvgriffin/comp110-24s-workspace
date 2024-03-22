"""Getting Functional with Battlehsip."""

__author__ = "730558866"

import random

# my emoji boxes
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"


def input_guess(grid_size: int, guess_type: str) -> int:
    """User is prompted for row or column within grid size."""
    assert guess_type == 'row' or guess_type == 'column'
    if guess_type == "row":
        row_guess: int = int(input("Guess a row: "))
        while row_guess > grid_size or row_guess < 1:
            row_guess = int(input(f"The grid is only { grid_size} by {grid_size}. Try again: "))
        return row_guess
    else:
        column_guess: int = int(input("Guess a column: "))
        while column_guess > grid_size or column_guess < 1:
            column_guess = int(input(f"The grid is only { grid_size} by {grid_size}. Try again: "))
        return column_guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Print the colorful boxes!"""
    row_counter = 1
    while row_counter <= grid_size:
        row_output = ""  # Initialize an empty string to accumulate characters for the row
        column_counter = 1
        while column_counter <= grid_size:
            if row_counter == row_guess and column_counter == column_guess:
                if correct:
                    row_output += RED_BOX
                else:
                    row_output += WHITE_BOX
            else:
                row_output += BLUE_BOX
            column_counter += 1
        print(row_output)  # Print the emoji strpy for the row
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Check to see if the user matched the secret boat location."""
    return row_guess == secret_row and column_guess == secret_column


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Run the main game loop."""
    turn_total = 5
    turn = 1
    while turn <= turn_total:
        print(f"=== Turn {turn}/{turn_total} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_column, row_guess, column_guess):
            print_grid(grid_size, row_guess, column_guess, True)
            print("Hit!")
            print(f"You won in {turn}/{turn_total} turns!")
            return
        else:
            print_grid(grid_size, row_guess, column_guess, False)
            print("Miss!")
        turn += 1

    print(f"X/{turn_total} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
                    
