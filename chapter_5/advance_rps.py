import sys
import random
from enum import Enum


class Game(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
print("-----------------------")

playerchoice = input(
    "Enter Your Choice...\n----------------------- \n 1 For ROCK ✊.\n 2 For PAPER 🫱 . \n 3 For SCISSORS ✌️ .\n\n")

print("-----------------------")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You Entered Invalid Number.\n")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You Chose " + str(Game(player)).replace("Game.", "") + ".")
print("Python Chose " + str(Game(computer)).replace("Game.", "") + ".")

print("-----------------------")

if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("🎉 YOU WON!")

elif player == computer:
    print("🤝 MATCH DRAW")

else:
    print("🐍 PYTHON WON!")

print("-----------------------")
