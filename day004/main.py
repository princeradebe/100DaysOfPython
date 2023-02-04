import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)
print(f"Computer chose {computer}")

if user == 0 and computer == 0:
    print(rock)
    print(rock)
    print("It's a draw")

elif user == 0 and computer == 1:
    print(rock)
    print(paper)
    print("You lose")

elif user == 0 and computer == 2:
    print(rock)
    print(scissors)
    print("You win")

elif user == 1 and computer == 0:
    print(paper)
    print(rock)
    print("You win")

elif user == 1 and computer == 1:
    print(paper)
    print(paper)
    print("It's a draw")

elif user == 1 and computer == 2:
    print(paper)
    print(scissors)
    print("You lose")

elif user == 2 and computer == 0:
    print(scissors)
    print(rock)
    print("You lose")

elif user == 2 and computer == 1:
    print(scissors)
    print(paper)
    print("You win")

elif user == 2 and computer == 2:
    print(scissors)
    print(scissors)
    print("It's a draw")

else:
    print("You typed an invalid number, you lose!")
