# Pong based on turtle

from turtle import Screen, Turtle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)


def go_up():
    if paddle.ycor() < 240:
        paddle.goto(350, paddle.ycor() + 20)
    
def go_down():
    if paddle.ycor() > -240:
        paddle.goto(350,paddle.ycor() - 20)

game_is_on = True

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

while game_is_on:
    screen.update()
screen.exitonclick()