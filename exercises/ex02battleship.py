"""EX01 - Simple Battleship - A cute step towards Battles."""

___author___ = "730558866"

grid_size : int = 4
secret_row: int = 3
secret_column: int = 2
correct: bool = False

# making the grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#did you hit or miss while loop
emoji_str: str = ""
correct: bool = False
while not correct:
    user_row = int(input("Guess a row: "))
    user_column = int(input("Guess a column: "))

    if 0 < user_row <= grid_size and 0 < user_column <= grid_size:
        if user_row == secret_row and user_column == secret_column:
            print("Hit!")
            result_box = RED_BOX
            correct = True
        elif user_row == secret_row or user_column == secret_column:
            print("Close! Correct row, wrong column." if user_row == secret_row else "Close! Correct column, wrong row.")
            result_box = WHITE_BOX
        else:
            print("Miss!")
            result_box = WHITE_BOX
    else:
        if user_row > grid_size or user_column > grid_size or user_row < 1 or user_column < 1:
            print("The grid is only 4 by 4. Try again:")

row_counter: int = 1
column_counter: int = 1


# emoji while loop
while row_counter <= grid_size:
    column_counter = 1
    while column_counter <= grid_size:
        if user_row == row_counter and user_column == column_counter:
            emoji_str += result_box
        else:
            emoji_str += BLUE_BOX
        column_counter += 1
    emoji_str += "\n"
    row_counter += 1

print(emoji_str)