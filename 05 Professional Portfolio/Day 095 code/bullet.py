from turtle import Turtle

BULLET_RESET_POS = (500, 500)

class Bullet(Turtle):
    
    def __init__(self, color="green"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(BULLET_RESET_POS)