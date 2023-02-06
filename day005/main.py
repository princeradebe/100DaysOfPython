# Prince Radebe
# DAY 005
# 05 February 2023
# 100 Days of Python

# For loops

# Fruits = ["Apple", "Peach", "Pear"]
# for fruit in Fruits:
#     print(f'This fruit is {fruit}')  # String interpolation
# total_height = 0
# number_of_student = 0
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# for height in student_heights:
#     total_height += height
#     number_of_student += 1

# average_height = round(total_height / number_of_student)
# print(f'The average height is {average_height}')

# Password Generator Project
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?"))
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

print(password)
