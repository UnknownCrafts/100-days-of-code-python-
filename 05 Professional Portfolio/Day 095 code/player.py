from turtle import Turtle
from bullet import Bullet

BULLET_RESET_POS = (500, 500)
BULLET_Y_MOVE = 20
class Player(Turtle):
    
    def __init__(self, position = (0, -250)):
        super().__init__()
        self.shape("player.gif")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.bullet = Bullet()
        self.bullet_shot = False
    
    def go_right(self):
        if self.xcor() < 330:
            self.goto(self.xcor() + 20, self.ycor())
    
    def go_left(self):
        if self.xcor() > -350:
            self.goto(self.xcor() - 20, self.ycor())
    
    def shoot(self):
        if not self.bullet_shot:
            self.bullet.goto(self.pos())
            self.bullet.goto(self.bullet.xcor(), self.bullet.ycor() + BULLET_Y_MOVE)
            self.bullet_shot = True
        
    def updateBulletPos(self):
        if self.bullet.ycor() < 290:
            self.bullet.goto(self.bullet.xcor(), self.bullet.ycor() + BULLET_Y_MOVE)
        else:
            self.resetBullet()
    
    def resetBullet(self):
        self.bullet.goto(BULLET_RESET_POS)
        self.bullet_shot = False