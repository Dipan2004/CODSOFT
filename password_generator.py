import random
import string

print("Welcome to the PyPassword Generator!")

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

nr_letters = int(input("How many letters would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your random password to use is: {password}")