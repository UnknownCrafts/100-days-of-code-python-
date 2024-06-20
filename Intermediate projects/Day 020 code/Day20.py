# snake game using turtle

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.listen()
game_is_on = True

snake = Snake(5) 

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    if snake.check_collision():
        game_is_on = False
    
    screen.onkeypress(snake.go_north, "w")
    screen.onkeypress(snake.go_north, "Up")
    screen.onkeypress(snake.go_west, "a")
    screen.onkeypress(snake.go_west, "Left")
    screen.onkeypress(snake.go_east, "d")
    screen.onkeypress(snake.go_east, "Right")
    screen.onkeypress(snake.go_south, "s")
    screen.onkeypress(snake.go_south, "Down")



screen.exitonclick()