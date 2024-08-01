# The text based coffee machine from day 15 but with OOP

import art
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


MENU = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

repeat_flag = True


user_input = ""

def check_input():
    
    global repeat_flag, coffee_machine, money_machine, MENU
    
    if user_input == "report":
        coffee_machine.report()
        money_machine.report()

    elif user_input == "off":
        repeat_flag = False

    else:
        menu_item = MENU.find_drink(user_input)
        if menu_item != None and coffee_machine.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_machine.make_coffee(menu_item)
                
print(art.logo)

while repeat_flag:
    
    user_input = input(f"What would you like ({MENU.get_items()[:-1]}): ").lower().strip()
    check_input()