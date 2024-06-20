from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
    
    def move(self, paddles):
        
        if self.distance(paddles[1]) < 55 and self.xcor() > 320 or (self.distance(paddles[0]) < 55 and self.xcor() < -320):
            self.move_speed *= 0.9
            self.bounce(True)
            
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce()
            
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)
    
    def bounce(self, direction_x = False):
        
        if direction_x:
            self.xmove *= -1
        else:
            self.ymove *= -1
    
    def check_miss(self):
        
        if self.xcor() > 380:
            self.goto(0,0)
            self.move_speed = 0.1
            return True
        elif self.xcor() < -380:
            self.goto(0,0)
            self.move_speed = 0.1
            return False