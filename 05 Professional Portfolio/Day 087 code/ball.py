from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -10)
        self.xmove = -10
        self.ymove = -10
        self.move_speed = 0.1
    
    def move(self, paddle):
        
        if self.distance(paddle) < 55 and self.ycor() < -230:
            self.move_speed *= 0.9
            self.bounce()
            
        if self.ycor() > 280:
            self.bounce()
        
        if self.xcor() > 370 or self.xcor() < -380:
            self.bounce(True)
            
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)
    
    def bounce(self, direction_x = False):
        
        if direction_x:
            self.xmove *= -1
        else:
            self.ymove *= -1
    
    def check_miss(self):
        return self.ycor() < -280
    
    def reset(self):
        self.goto(0, -10)
        self.move_speed = 0.1