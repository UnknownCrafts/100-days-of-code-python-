#crossy road but turtle

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy Turtle")


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_up, "Up")

car_manager.generateCars()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if player.check_finish():
        scoreboard.increase_score()
        car_manager.increase_speed()
    
    if car_manager.movementCheck(player):
        screen.update()
        game_is_on = False


scoreboard.game_over()

screen.exitonclick()