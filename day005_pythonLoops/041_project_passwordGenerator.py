alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]

import random

numberOf_alphabet = int(input("Number of alphabets?: "))
numberOf_numbers = int(input("Number of numbers?: "))
numberOf_symbols = int(input("Number of symbols?: "))

# Generate sequential password as list, so that it can be shuffled using random.shuffle()
password = []
for i in range(0, numberOf_alphabet):
    password.append(random.choice(alphabet))
for i in range(0, numberOf_numbers):
    password.append(random.choice(numbers))
for i in range(0, numberOf_symbols):
    password.append(random.choice(symbols))

# Shuffle password list and convert it to string
random.shuffle(password)
password = "".join(password)

print(password)