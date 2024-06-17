# Text based blackjack

import art
import random
import os

def user_score():
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")

def computer_deck():
    print(f"Computer's first card: {computer_cards[0]}")

is_running = True
user_passed = False
repeat_flag = True
opponent_blackjack = False
user_blackjack = False

user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()

if user_choice != "y":
    repeat_flag = False

while repeat_flag:
    
    print(art.logo)
    
    is_running = True
    user_passed = False
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = [random.choice(cards)]*2
    computer_cards = [random.choice(cards)]*2
    
    user_card_sum = sum(user_cards)
    computer_card_sum = sum(computer_cards)
    
    while user_card_sum > 21 and 11 in user_cards:
            for card in user_cards:
                if card == 11:
                    user_cards[user_cards.index(11)] = 1
                    break
                
    while computer_card_sum > 21 and 11 in computer_cards:
        for card in computer_cards:
            if card == 11:
                computer_cards[computer_cards.index(11)] = 1
                break
    
    if computer_card_sum == 21:
        opponent_blackjack = True
        
    elif user_card_sum == 21:
        user_blackjack = True
    
    else:
        user_score()
        computer_deck()
    
    while is_running and not opponent_blackjack and not user_blackjack:
        
        if not user_passed:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
            if user_input == "y":
                user_cards.append(random.choice(cards))
            else:
                user_passed = True
            
        elif sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
            
        else:
            is_running = False
        
        while sum(user_cards) > 21 and 11 in user_cards:
            for card in user_cards:
                if card == 11:
                    user_cards[user_cards.index(11)] = 1
                    break
                
        while sum(computer_cards) > 21 and 11 in computer_cards:
            for card in computer_cards:
                if card == 11:
                    computer_cards[computer_cards.index(11)] = 1
                    break
                    
        if sum(computer_cards) > 21 or sum(user_cards) > 21:
            is_running = False
        
        if is_running and not user_passed:
            user_score()
            computer_deck()
    
    user_card_sum = sum(user_cards)
    computer_card_sum = sum(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_card_sum}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_card_sum}")
    
    if user_card_sum == computer_card_sum:
        print("Draw 🙃")
    elif opponent_blackjack:
        print("Lose, opponent has Blackjack 😱")
    elif user_blackjack:
        print("Win with a Blackjack 😎")
    elif user_card_sum > 21:
        print("You went over. You lose 😭")
    elif computer_card_sum > 21:
        print("Opponent went over. You win 😁")
    elif user_card_sum > computer_card_sum:
        print("You win 😃")
    elif computer_card_sum > user_card_sum:
        print("You lose 😤")
    
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()

    if user_choice != "y":
        repeat_flag = False
    else:
        os.system("cls||clear")
    
