# Prince Radebe
# DAY 004
# 04 February 2023
# 100 Days of Python

import random
from ascii_art import rock, paper, scissors

# ARefactored my code and included a separete file for ascii art
user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user not in [0, 1, 2]:
    print("Invalid choice. Please type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    exit()

computer = random.randint(0, 2)
print(f"Computer chose {computer}")

choices = [rock, paper, scissors]
user_choice = choices[user]
computer_choice = choices[computer]

result = None
if user == computer:
    result = "It's a draw"
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    result = "You win"
else:
    result = "You lose"

print(user_choice)
print(computer_choice)
print(result)
