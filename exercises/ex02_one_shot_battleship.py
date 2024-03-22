"""Leveling up in Battleship."""

__author__ = "730558866"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
correct: bool = False

# making the grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

user_row = int(input("Guess a row: "))
while user_row > grid_size or user_row < 1:
    user_row = int(input("The grid is only 4 by 4. Try again: "))
user_column = int(input("Guess a column: "))
while user_column > grid_size or user_column < 1:
    user_column = int(input("The grid is only 4 by 4. Try again: "))

if 0 < user_row <= grid_size and 0 < user_column <= grid_size:
    if user_row == secret_row and user_column == secret_column:
        result_box = RED_BOX
    
    elif user_row == secret_row:
        result_box = WHITE_BOX

    elif user_column == secret_column:
        result_box = WHITE_BOX

    else:
        result_box = WHITE_BOX

    # hit is red
    # miss is white
    row_counter: int = 1

    while row_counter <= grid_size:
        emoji_str: str = ""
        column_counter: int = 1
        if user_row == row_counter:
            while column_counter <= grid_size:
                if user_column == column_counter:
                    emoji_str = emoji_str + result_box
                else:
                    emoji_str = emoji_str + BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid_size:
                emoji_str = emoji_str + BLUE_BOX
                column_counter += 1
        print(emoji_str)
        row_counter += 1
if user_row == secret_row and user_column == secret_column:
    print("Hit!")
elif user_row == secret_row:
    print("Close! Correct row, wrong column.")
elif user_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")