"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730558866"

tarheelboat1 = input("Pick a secret boat location between 1 and 4:")
tarheelboat1: int = (tarheelboat1)
if tarheelboat1 < 1:
    print(f"Error! {tarheelboat1} too low!")
if tarheelboat1 > 4:
    print(f"Error! {tarheelboat1} too high!")