from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()
        self.make_line()
    
    def make_line(self):
        line_maker = Turtle()
        line_maker.hideturtle()
        line_maker.penup()
        line_maker.pencolor("white")
        line_maker.pensize(3)
        line_maker.goto(0, 300)
        line_maker.setheading(270)
        for i in range(581):
            line_maker.pendown()
            line_maker.forward(10)
            line_maker.penup()
            line_maker.forward(10)
        line_maker.penup()
    
    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    def score_increase(self, leftscored=True):
        if leftscored:
            self.l_score += 1
        else:
            self.r_score += 1
        
        self.write_score()