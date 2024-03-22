"""EX01 - Simple Battleship - A cute step towards Battles."""

__author__ = "730558866"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

tank1_input = input("Pick a secret boat location between 1 and 4:")
tank1 = int(tank1_input)

if tank1 < 1:
    print(exit(f"Error! {tank1} too low!"))
if tank1 > 4:
    print(exit(f"Error! {tank1} too high!"))

predictor2_input = input("Guess a number between 1 and 4:")
predictor2 = int(predictor2_input)

if predictor2 < 1:
    print(exit(f"Error! {predictor2} too low!"))

if predictor2 > 4:
    print(exit(f"Error! {predictor2} too high!"))

predictor_result: str = ""

if tank1 == predictor2:
    predictor_result = RED_BOX
    if tank1 == 1:
        print(f"{predictor_result}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
        print("Correct! You hit the ship.")
    if tank1 == 2:
        print(f"{BLUE_BOX}{predictor_result}{BLUE_BOX}{BLUE_BOX}")
        print("Correct! You hit the ship.")
    if tank1 == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{predictor_result}{BLUE_BOX}")
        print("Correct! You hit the ship.")
    if tank1 == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{predictor_result}")
        print("Correct! You hit the ship.")

else:
    predictor_result = WHITE_BOX
    if predictor2 == 1:
        print(f"{predictor_result}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
        print("Incorrect! You missed the ship.")
    if predictor2 == 2:
        print(f"{BLUE_BOX}{predictor_result}{BLUE_BOX}{BLUE_BOX}")
        print("Incorrect! You missed the ship.")
    if predictor2 == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{predictor_result}{BLUE_BOX}")
        print("Incorrect! You missed the ship.")
    if predictor2 == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{predictor_result}")
        print("Incorrect! You missed the ship.")