# Text Based Tic Tac Toe

import random

is_running = True
first_run = True
player_goes_first = False
player_win = False
computer_win = False

player_symbol = ""
computer_symbol = ""

symbols = ["O", "X"]

grid = [["","",""],
        ["","",""],
        ["","",""]]

empty_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

spot_to_grid = {
    "A1": "00",
    "A2": "10",
    "A3": "20",
    "B1": "01",
    "B2": "11",
    "B3": "12",
    "C1": "02",
    "C2": "12",
    "C3": "22",
}


def clear_grid():
    global grid, empty_spots
    grid = [["","",""],
            ["","",""],
            ["","",""]]
    empty_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def print_grid() -> None:
    print("   A   B   C")
    for i in range(3):
        print(f"{i+1} {grid[i]}")
    print("")

def print_symbols():
    print(f"Player: {player_symbol}")
    print(f"Computer: {computer_symbol}\n")

def assign_symbols():
    global player_symbol, computer_symbol
    player_choice = input("Enter 1 for O, 2 for X, 3 for random: ").strip()

    if player_choice == "1":
        player_symbol = "O"
        computer_symbol = "X"

    elif player_choice == "2":
        player_symbol = "X"
        computer_symbol = "O"

    else:
        player_symbol = random.choice(symbols)
        for symbol in symbols:
            if symbol != player_symbol:
                computer_symbol = symbol
                break

def input_validation():
    recieved_input = False
    while not recieved_input and empty_spots.count("") != 9:
        player_input = input("Where would you like to place your symbol e.g A1, B2 etc: ").strip()
        if player_input != "" and player_input in empty_spots:
            recieved_input = True
            chosen_spot = spot_to_grid[player_input]
            grid[int(chosen_spot[0])][int(chosen_spot[1])] = player_symbol
            index = empty_spots.index(player_input)
            empty_spots[index] = ""

def choose_random():
    chosen_symb = ""
    while empty_spots.count("") <= 9 and chosen_symb == "":
        chosen_symb = random.choice(empty_spots)
    chosen_spot = spot_to_grid[chosen_symb]
    print(f"Computer has chosen: {chosen_symb}\n")
    grid[int(chosen_spot[0])][int(chosen_spot[1])] = computer_symbol
    index = empty_spots.index(chosen_symb)
    empty_spots[index] = ""

print("Welcome to Tic Tac Toe")
player_turn = random.randint(0,1)
while is_running:
    if first_run:
        assign_symbols()
        print_symbols()
        
        if player_turn:
            print("Player goes first\n")
            input_validation()
            player_turn = False
        else:
            print("Computer goes first\n")
            choose_random()
            player_turn = True
        first_run = False
        print_grid()
        
    if player_turn:
        input_validation()
        print_grid()
        player_turn = False
    else:
        choose_random()
        print_grid()
        player_turn = True
