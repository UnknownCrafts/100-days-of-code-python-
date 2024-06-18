# Making the hirst dots painitng using turtle, maybe I will make a million dollars after this

# import colorgram

# colors = colorgram.extract('image.jpg', 30)

# color_list = []

# for i in range(30):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     color_list.append((r, g, b))


import turtle
import random


#colors extracted using colorgram

color_list = [(244, 242, 239), (198, 166, 109), (141, 77, 54), (245, 242, 244), (73, 98, 123), (158, 148, 54), (234, 237, 242), (213, 203, 144), (238, 243, 239), 
              (120, 39, 29), (137, 160, 179), (70, 108, 74), (144, 176, 139), (195, 91, 70), (69, 52, 46), (96, 81, 89), (60, 52, 56), (224, 177, 163), 
              (102, 141, 131), (97, 130, 164), (156, 141, 159), (49, 60, 83), (73, 67, 50), (111, 38, 42), (47, 56, 72), (108, 136, 140), (182, 199, 183), 
              (182, 190, 205), (168, 101, 106), (51, 76, 61)]


turtle.colormode(255)
painter = turtle.Turtle()
painter.speed("fastest")
painter.penup()
painter.hideturtle()
painter.setheading(225)
painter.forward(300)
painter.setheading(0)
x_coord = painter.xcor()
y_increment = painter.ycor() + 50

for i in range(10):
    for i in range(10):
        painter.dot(15, random.choice(color_list))
        painter.forward(50)
    painter.goto(x_coord,y_increment)
    y_increment += 50

turtle.exitonclick()