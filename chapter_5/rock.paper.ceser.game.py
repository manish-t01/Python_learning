import sys
import random

print("")
print("-----------------------")

playerchoice = input(
    "Enter Your Choice...\n----------------------- \n 1 For Rock.\n 2 For Paper. \n 3 For Scessior.\n\n")

print("-----------------------")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You Entered Invalid Number.\n")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You Chose " + playerchoice + ".")
print("Python Chose " + computerchoice + ".")

print("-----------------------")

if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("YOU WON!")

elif player == computer:
    print("MATCH DRAW")

else:
    print("PYTHON WON!")

print("-----------------------")
