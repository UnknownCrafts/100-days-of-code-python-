# Atari Breakout

import time
from ball import Ball
from paddle import Paddle
from turtle import Screen
from scoreboard import Scoreboard
from tileManager import TileManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Breakout")

tileManager = TileManager()
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()

game_is_on = True
game_won = False

screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(paddle)
    miss_check = ball.check_miss()
    collision_check = tileManager.tileCollisionCheck(ball)
    
    if miss_check:
        ball.reset()
        scoreboard.decrease_lives()

    if collision_check != None:
        scoreboard.score_increase(collision_check[0])
        
        if collision_check[1] == 0:
            game_won = True
            game_is_on = False
    
    if scoreboard.get_lives() == 0:
        game_is_on = False

if game_won:
    scoreboard.won()
else:
    scoreboard.lose()

screen.exitonclick()