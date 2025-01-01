from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.goto(320, 260)
        self.write(f'Score: {self.score}', align="center", font=("Courier", 15, "normal"))
        self.goto(-320, 260)
        self.write(f'Lives: {self.lives}', align="center", font=("Courier", 15, "normal"))
    
    def score_increase(self, increment=1):
        self.score += increment
        
        self.write_score()
    
    def decrease_lives(self):
        self.lives -= 1
        
        self.write_score()
    
    def get_lives(self):
        return self.lives
    
    def won(self):
        self.goto(0, 0)
        self.pencolor("green")
        self.write("You Win!", align="center", font=("Courier", 40, "normal"))
    
    def lose(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("You Lose.", align="center", font=("Courier", 40, "normal"))
        