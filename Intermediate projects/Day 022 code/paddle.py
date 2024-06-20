from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position = (350, 0)):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)
    
    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)