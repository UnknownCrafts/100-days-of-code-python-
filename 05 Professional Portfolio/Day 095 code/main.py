# Space Invaders

import time
from player import Player
from turtle import Screen
from scoreboard import Scoreboard
from alienManager import AlienManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Space Invaders")

# Register the alien and player sprites
screen.register_shape('player.gif')
screen.register_shape('alien0_pose1.gif')
screen.register_shape('alien0_pose2.gif')
screen.register_shape('alien1_pose1.gif')
screen.register_shape('alien1_pose2.gif')
screen.register_shape('alien2_pose1.gif')
screen.register_shape('alien2_pose2.gif')
screen.register_shape('mysteryship.gif')

alienManager = AlienManager()
scoreboard = Scoreboard()
player = Player()

game_speed_inc = 0.01
game_speed = 0.3
game_is_on = True
game_won = False

screen.listen()
screen.onkey(player.go_left, "a")
screen.onkey(player.go_right, "d")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
screen.onkey(player.shoot, "space")


while game_is_on:
    time.sleep(game_speed)
    screen.update()
    player.updateBulletPos()
    resMovementCheck = alienManager.movementCheck(player)
    
    if resMovementCheck != None:
        if resMovementCheck[0]:
            scoreboard.score_increase()
            game_speed -= game_speed_inc
        
        if resMovementCheck[1]:
            scoreboard.decrease_lives()
    
    if scoreboard.get_lives() <= 0:
        game_is_on = False
    
    if alienManager.aliensRemaining() == 0:
        game_is_on = False
        game_won = True

if game_won:
    scoreboard.won()
else:
    scoreboard.lose()

screen.exitonclick()