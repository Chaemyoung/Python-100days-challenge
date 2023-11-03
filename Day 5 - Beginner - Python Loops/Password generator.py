#Password Generator Project
import random

list = []

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like\n"))

for letter in range(1, nr_letters+1):
    chosen_letter = random.choice(letters)
    list.append(chosen_letter)

for num in range(1, nr_numbers+1):
    chosen_num = random.choice(numbers)
    list.append(chosen_num)

for sym in range(1, nr_symbols+1):
    chosen_sym = random.choice(symbols)
    list.append(chosen_sym)    

random.shuffle(list)

password = "".join(list)

print(f"Your password is: {password}")