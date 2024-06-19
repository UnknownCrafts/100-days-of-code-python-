# Etch-A-Sketch app using python turtle.

from turtle import Turtle, Screen

painter = Turtle()
screen = Screen()

def move_forwards():
    painter.forward(10)
def move_backwards():
    painter.backward(10)
def move_right():
    painter.setheading(painter.heading() - 10)
def move_left():
    painter.setheading(painter.heading() + 10)
    
screen.listen()
# move forwards
screen.onkey(move_forwards, "w")
screen.onkey(move_forwards, "Up")

#move backwards
screen.onkey(move_backwards, "s")
screen.onkey(move_backwards, "Down")

#For some reason when the a and d keys and the right and left arrow keys, get inverted when using the same functions
#turn right
screen.onkey(move_left, "a")
screen.onkey(move_right, "Right")

#turn left
screen.onkey(move_right, "d")
screen.onkey(move_left, "Left")

# reset
screen.onkey(key="c", fun=painter.reset)

screen.exitonclick()