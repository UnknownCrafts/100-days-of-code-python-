# Text based Higher or Lower game

import art
import gamedata
import random
import os

print(art.logo)

repeat_flag = False
choice_A = random.choice(gamedata.data)
choice_B = random.choice(gamedata.data)
score = 0

print(f"Compare A: {choice_A.get('name')}, a {choice_A.get('description')}, from {choice_A.get('country')}.")
print("")
print("")
print(art.vs)
print(f"Against B: {choice_B.get('name')}, a {choice_B.get('description')}, from {choice_B.get('country')}.")
user_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize().strip()

if user_choice == "A":
    if choice_A["follower_count"] > choice_B["follower_count"]:
        score += 1
        repeat_flag = True
    else:
        repeat_flag = False
else:
    if choice_B["follower_count"] > choice_A["follower_count"]:
        score += 1
        repeat_flag = True
    else:
        repeat_flag = False

while repeat_flag:
    
    os.system("cls||clear")
    print(art.logo)
    
    choice_A = random.choice(gamedata.data)
    choice_B = random.choice(gamedata.data)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {choice_A.get('name')}, a {choice_A.get('description')}, from {choice_A.get('country')}.")
    print("")
    print("")
    print(art.vs)
    print(f"Against B: {choice_B.get('name')}, a {choice_B.get('description')}, from {choice_B.get('country')}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize().strip()

    if user_choice == "A":
        if choice_A["follower_count"] > choice_B["follower_count"]:
            score += 1
            repeat_flag = True
        else:
            repeat_flag = False
    else:
        if choice_B["follower_count"] > choice_A["follower_count"]:
            score += 1
            repeat_flag = True
        else:
            repeat_flag = False

os.system("cls||clear")
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")