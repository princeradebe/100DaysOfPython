# Hangman Game

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
