# A simple turtle race where you can bet on the turtle who is gonna win

from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ").lower().strip()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False
winning_color = ""


for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y = y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0, 10)
    chosen_turtle = random.choice(all_turtles)
    chosen_turtle.forward(rand_distance)
    if chosen_turtle.xcor() > 230:
        winning_color = chosen_turtle.color()[0]
        is_race_on = False

if user_bet == winning_color:
    print(f"You've win! The {winning_color} turtle is the winner!")
else:
    print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()