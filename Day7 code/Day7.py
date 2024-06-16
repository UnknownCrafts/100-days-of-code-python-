#Text based hangman game
import random
import os
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)

display = ["_"]*len(chosen_word)

lives = 6
correct_flag = False

print(hangman_art.logo)

while ("_" in display) and (lives > 0):

  guess = input("Guess a letter: ").lower().strip()
  
  os.system('cls||clear')
  
  if guess in display:
    print(f"The letter \"{guess}\" has already been guessed")
  
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
      display[i] = guess
      correct_flag = True
      
  if not correct_flag:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
  print("")
  
  for i in range(len(display)):
    print(display[i], end=" ")
    
  print("\n")
    
  print(hangman_art.stages[lives])
        
  correct_flag = False

print("")
if lives > 0:  
  print("You Win.")
else:
  print("You Lose.")