# Text based number guessing game

import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

computer_choice = random.randint(1, 100)
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
lives = 10
game_end = False

if user_choice == "hard":
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")

while lives > 0 and not game_end:
    
    user_input = int(input("Make a guess: ").strip())
    
    if (computer_choice > user_input):
        print("Too low.")
        lives -= 1
    elif (computer_choice < user_input):
        print("Too high.")
        lives -= 1
    else:
        print("Correct!")
        game_end = True
    
    if lives <= 0:
        print("You've run out of guesses, you lose.")
        game_end = True
    elif not game_end:
        print("Guess again.")
        print(f"You have {lives} attempts remaining to guess the number.")

print(f"The number was: {computer_choice}")