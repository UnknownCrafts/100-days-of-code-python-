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

def choice_comparision():
    global repeat_flag, choice_A, choice_B, score, user_choice
    
    if user_choice == "A":
        if choice_A["follower_count"] > choice_B["follower_count"]:
                score += 1
                repeat_flag = True
                choice_B = random.choice(gamedata.data)
                while choice_A == choice_B:
                    choice_B = random.choice(gamedata.data)
        else:
            repeat_flag = False
    else:
        if choice_B["follower_count"] > choice_A["follower_count"]:
                score += 1
                repeat_flag = True
                choice_A = choice_B
                choice_B = random.choice(gamedata.data)
                while choice_A == choice_B:
                    choice_B = random.choice(gamedata.data)
        else:
            repeat_flag = False

print(f"Compare A: {choice_A.get('name')}, a {choice_A.get('description')}, from {choice_A.get('country')}.")
print("")
print("")
print(art.vs)
print(f"Against B: {choice_B.get('name')}, a {choice_B.get('description')}, from {choice_B.get('country')}.")
user_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize().strip()

choice_comparision()

while repeat_flag:
    
    os.system("cls||clear")
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {choice_A.get('name')}, a {choice_A.get('description')}, from {choice_A.get('country')}.")
    print("")
    print("")
    print(art.vs)
    print(f"Against B: {choice_B.get('name')}, a {choice_B.get('description')}, from {choice_B.get('country')}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize().strip()

    choice_comparision()

os.system("cls||clear")
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")