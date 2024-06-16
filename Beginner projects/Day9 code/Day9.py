# Silent auction system

import art
import os

bidders = {}

print(art.logo)

print("Welcome to the secret auction program.")

name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()

bidders[name] = bid

repeat_flag = choice == "yes"

while repeat_flag:
    os.system('cls||clear')
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()

    bidders[name] = bid
    
    if choice == "no":
        repeat_flag = False

os.system('cls||clear')

max_bid = 0
max_bid_name = ""

for key in bidders:
    if bidders[key] > max_bid:
        max_bid_name = key
        max_bid = bidders[key]

print(f"The winner is {max_bid_name} with a bid of ${max_bid}.")