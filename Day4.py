# Text based Rock, paper, scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choice = random.randint(0,2)

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("")
if player_input == 0:
    print(rock)
elif player_input == 1:
    print(paper)
else:
    print(scissors)
print("")
print("Computer chose:\n")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if (player_input == 0 and computer_choice == 2 or player_input == 1 and computer_choice == 0 or player_input == 2 and computer_choice == 1):
    print("You Win.")
elif(player_input == computer_choice):
    print("It's a draw.")
else:
    print("You Lose.")