from turtle import Turtle
from bullet import Bullet

BULLET_RESET_POS = (500, 500)
BULLET_Y_MOVE = -20

class Alien(Turtle):
    
    def __init__(self, pose="classic", position = (0, -250)):
        super().__init__()
        self.shape(pose)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)
        self.bullet = Bullet(color="white")
        self.bullet_shot = False
    
    def shoot(self):
        if not self.bullet_shot:
            self.bullet.goto(self.pos())
            self.bullet.goto(self.bullet.xcor(), self.bullet.ycor() + BULLET_Y_MOVE)
            self.bullet_shot = True
        
    def updateBulletPos(self, player, bullet):
        player_bullet_hit = False
        player_hit = False
        
        if self.bullet.ycor() > -270:
            self.bullet.goto(self.bullet.xcor(), self.bullet.ycor() + BULLET_Y_MOVE)
        else:
            self.resetBullet()
            
        if self.bullet.distance(player) < 24:
            self.resetBullet()
            player_hit = True
            return (player_bullet_hit, player_hit)
    
        if self.bullet.distance(bullet) < 24:
            self.resetBullet()
            player_bullet_hit = True
            return (player_bullet_hit, player_hit)
        
    def was_bullet_shot(self):
        return self.bullet_shot
    
    def resetBullet(self):
        self.bullet.goto(BULLET_RESET_POS)
        self.bullet_shot = False