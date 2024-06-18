# Text based coin operated coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

repeating_flag = True
money_earned = 0

def get_payment(cost):
    global money_earned
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    money_given = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    
    if money_given > cost:
        print(f"Here is ${round(money_given - cost, 2)} dollars in change.")
        money_earned += cost
        return True
    elif money_given < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money_earned += cost

def check_input(input):
    global repeating_flag, resources, MENU, money_earned
    cost = 0
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]
    
    if input == "report":
        for key in resources:
            if key == "water" or key == "milk":
                print(f"{key.capitalize()}: {resources[key]}ml")
            else:
                print(f"{key.capitalize()}: {resources[key]}g")
        print(f"Money: ${money_earned}")
            
    elif input == "off":
        repeating_flag = False
        
    elif input == "espresso":
        required_water = MENU["espresso"]["ingredients"]["water"]
        required_coffee = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]
        
        if required_water > current_water:
            print("Sorry there is not enough water.")
        elif required_coffee > current_coffee:
            print("Sorry there is not enough coffee beans.")
        else:
            if get_payment(cost):
                resources["water"] = current_water - required_water
                resources["coffee"] = current_coffee - required_coffee
                print("Here is your espresso ☕️. Enjoy!")
        
    elif input == "latte":
        required_water = MENU["latte"]["ingredients"]["water"]
        required_milk = MENU["latte"]["ingredients"]["milk"]
        required_coffee = MENU["latte"]["ingredients"]["coffee"]
        cost = MENU["latte"]["cost"]
        
        if required_water > current_water:
            print("Sorry there is not enough water.")
        elif required_coffee > current_coffee:
            print("Sorry there is not enough coffee beans.")
        elif required_milk > current_milk:
            print("Sorry there is not enough milk.")
        else:
            if get_payment(cost):
                resources["water"] = current_water - required_water
                resources["milk"] = current_milk - required_milk
                resources["coffee"] = current_coffee - required_coffee
                print("Here is your latte ☕️. Enjoy!")
        
    elif input == "cappuccino":
        required_water = MENU["cappuccino"]["ingredients"]["water"]
        required_milk = MENU["cappuccino"]["ingredients"]["milk"]
        required_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = MENU["cappuccino"]["cost"]
        
        if required_water > current_water:
            print("Sorry there is not enough water.")
        elif required_coffee > current_coffee:
            print("Sorry there is not enough coffee beans.")
        elif required_milk > current_milk:
            print("Sorry there is not enough milk.")
        else:
            if get_payment(cost):
                resources["water"] = current_water - required_water
                resources["milk"] = current_milk - required_milk
                resources["coffee"] = current_coffee - required_coffee
                print("Here is your cappuccino ☕️. Enjoy!")

while repeating_flag:
    
    user_input = input("What would you like (espresso/latte/cappucino): ").lower().strip()
    check_input(user_input)