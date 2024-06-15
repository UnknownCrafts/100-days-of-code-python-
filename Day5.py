#Password generator
import random
import string

print("Welcome to the PyPassword Generator!")

amount_of_letters = int(input("How many letters would you like in your password?\n"))
amount_of_symbols = int(input("How many symbols would you like?\n"))
amount_of_numbers = int(input("How many numbers would you like?\n"))

randint = random.randint(0,2)
letter_list = string.ascii_letters
digit_list = string.digits
symbol_list = '!@#$%^&*()_'
password = ""

for i in range(amount_of_letters):
    password += random.choice(letter_list)
for i in range(amount_of_numbers):
    password += random.choice(digit_list)
for i in range(amount_of_symbols):
    password += random.choice(symbol_list)
    
password = list(password)
random.shuffle(password)
password = "".join(password)

print(f"Here is you password: {password}")