import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

all_password_chars = []
for letter in range(0, nr_letters):
    all_password_chars.append(letters[random.randint(0, len(letters) - 1)])
for symbol in range(0, nr_symbols):
    all_password_chars.append(symbols[random.randint(0, len(symbols) - 1)])
for number in range(0, nr_numbers):
    all_password_chars.append(numbers[random.randint(0, len(numbers) - 1)])

randomise_password = ""
for char in range(0, len(all_password_chars)):
    index = random.randint(0, len(all_password_chars) - 1)
    randomise_password += all_password_chars.pop(index)

print(f"Your password is: {randomise_password}")
