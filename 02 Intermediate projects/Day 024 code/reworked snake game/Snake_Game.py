# snake game using turtle
# Day 21 was mostly adding scoreboard and food etc
# Day 24 is adding a high score system which helps to close the play loop

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.go_north, "w")
screen.onkeypress(snake.go_north, "Up")
screen.onkeypress(snake.go_west, "a")
screen.onkeypress(snake.go_west, "Left")
screen.onkeypress(snake.go_east, "d")
screen.onkeypress(snake.go_east, "Right")
screen.onkeypress(snake.go_south, "s")
screen.onkeypress(snake.go_south, "Down")

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    if snake.check_collision(food, scoreboard):
        scoreboard.reset()
        snake.reset()



screen.exitonclick()