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
            snake_body.heading
            snake_body.penup()
            snake_body.shape("square")
            snake_body.color("white")
            self.snake_segments.append(snake_body)
            snake_body.goto(self.x_offset, 0)
            self.x_offset -= 20
        self.head = self.snake_segments[0]
        
    def move(self):
        
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.head.forward(20)
    
    def check_collision(self):
        for i in range(1, self.length):
            if self.head.distance(self.snake_segments[i]) <= 1 or self.head.xcor() > 280 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -280:
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
