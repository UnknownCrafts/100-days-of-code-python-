# Pong based on turtle

from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle()
paddle_list = [l_paddle, r_paddle]
ball = Ball()

game_is_on = True

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(paddle_list)
    miss_check = ball.check_miss()
    
    if miss_check:
        scoreboard.score_increase()
    elif miss_check == False:
        scoreboard.score_increase(leftscored=False)

screen.exitonclick()