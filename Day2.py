#A simple tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
print("Each person should pay: $" + str(round((bill/total_people)*((tip/100) + 1), 2)))