from turtle import Turtle

class Snake:
    
    def __init__(self, length = 3):
        
        self.length = length
        self.x_offset = 0
        self.snake_segments = []
        self.head = ""
        self.create_snake()
        
    def create_snake(self):
        
        for i in range(self.length):
            snake_body = Turtle()
            snake_body.penup()
            snake_body.shape("square")
            snake_body.color("white")
            self.snake_segments.append(snake_body)
            snake_body.goto(self.x_offset, 0)
            self.x_offset -= 20
        self.head = self.snake_segments[0]
        self.head.color("green")
    
    def increase_length(self):
        snake_body = Turtle()
        snake_body.penup()
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.goto(self.snake_segments[-1].position())
        self.snake_segments.append(snake_body)
        
    def move(self):
        
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.head.forward(20)
    
    def check_collision(self, food, scoreboard):
        if self.head.distance(food) <= 15:
                self.increase_length()
                food.random_pos()
                scoreboard.increase_score()
        
        if self.head.xcor() > 295 or self.head.xcor() < -300 or self.head.ycor() > 299 or self.head.ycor() < -295:
            return True
            
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) <= 10:
                return True
    
    def go_north(self):

        if self.head.heading() != 270:
            self.head.setheading(90)

            
    def go_west(self):

        if self.head.heading() != 0:
            self.head.setheading(180)

            
    def go_east(self):

        if self.head.heading() != 180:
            self.head.setheading(0)

            
    def go_south(self):

        if self.head.heading() != 90:
            self.head.setheading(270)
