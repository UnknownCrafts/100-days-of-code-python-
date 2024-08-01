from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.score = 0
        self.write_score()
        
        self.border_turtle = Turtle(visible=False)
        self.border_turtle.penup()
        self.border_turtle.pencolor("red")
        self.make_border()
    
    def make_border(self):
        self.border_turtle.goto(-295, 280)
        self.border_turtle.pendown()
        self.border_turtle.forward(580)
        self.border_turtle.right(90)
        self.border_turtle.forward(565)
        self.border_turtle.right(90)
        self.border_turtle.forward(580)
        self.border_turtle.right(90)
        self.border_turtle.forward(565)
        self.border_turtle.right(90)
        self.border_turtle.penup()
    
    def write_score(self):
        self.goto(-20, 278)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        