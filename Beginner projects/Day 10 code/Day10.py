# Text based calculator

import art
import os

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1**n2

def print_operations():
    for op in operations:
        print(op,end="\n")

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "^": power,
}

def calculator():
    
    print(art.logo)
    
    first_number = float(input("What's the first number?: ").strip())

    print_operations()

    operation_select = input("Pick an operation: ").strip()

    calculator = operations[operation_select]

    second_number = float(input("What's the next number?: ").strip())

    answer = calculator(first_number, second_number)

    print(f"{first_number} {operation_select} {second_number} = {answer}")

    choice_input = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, type 'q' to quit: ").lower().strip()

    repeat_flag = choice_input == "y" or choice_input == "n"

    while repeat_flag:
        
        if choice_input == "y":
            
            operation_select = input("Pick an operation: ").strip()
            calculator = operations[operation_select]
            second_number = float(input("What's the next number?: ").strip())
            old_answer = answer
            answer = calculator(answer, second_number)

            print(f"{old_answer} {operation_select} {second_number} = {answer}")
            
        elif choice_input == "n":
            
            os.system("cls||clear")
            
            answer = 0
            
            print(art.logo)
            
            first_number = float(input("What's the first number?: ").strip())

            print_operations()

            operation_select = input("Pick an operation: ").strip()
            calculator = operations[operation_select]
            second_number = float(input("What's the next number?: ").strip())

            answer = calculator(first_number, second_number)

            print(f"{first_number} {operation_select} {second_number} = {answer}")

        else:
            repeat_flag = False
        
        choice_input = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, type 'q' to quit: ").lower().strip()

        repeat_flag = choice_input == "y" or choice_input == "n"

calculator()

print("Thank you for using the calculator. Goodbye!")