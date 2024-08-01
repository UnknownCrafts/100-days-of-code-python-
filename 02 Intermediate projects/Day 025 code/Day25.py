# U.S States Naming Game using turtle

import turtle
import pandas


screen = turtle.Screen()

screen.title("U.S States Naming Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()

correct_guesses = []
csv = pandas.read_csv("50_states.csv")
all_states = csv["state"].to_list()
count = 0

while len(correct_guesses) < 50:

    answer = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name? ").title().strip()
    
    if answer == "Exit":
        missed_states = [state for state in all_states if state not in correct_guesses]

        df = pandas.DataFrame(missed_states)
        df.to_csv('states_to_learn.csv')
        break
    
    if answer in all_states and answer not in correct_guesses:
        correct_guesses.append(answer)
        mask = csv['state'].values == answer
        x_value = csv[mask]["x"].iloc[0]
        y_value = csv[mask]["y"].iloc[0]
        writer_turtle.goto((x_value, y_value))
        writer_turtle.write(answer)
        count += 1