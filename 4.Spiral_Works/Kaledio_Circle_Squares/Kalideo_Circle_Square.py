import turtle
from itertools import cycle #For Cycle of Colors

colors = cycle([
    "red",
    "blue",
    "green",
    "orange",
    "grey",
    "purple",
    "pink",
    ])


def square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def circle(radius,color,angle,forward,shape):
    #Set Pen color
    turtle.pencolor(next(colors))
    next_shape = ""
    #Draw Circle and Change Shape
    if shape == "circle":
        turtle.circle(radius)
        next_shape = "square"
    #Draw Square and Change Shape
    elif shape == "square":
        square(radius * 2)
        next_shape = "circle"
    #Changle Angle of Pen
    turtle.right(angle)
    #Change Center of Shape
    turtle.forward(forward)
    circle(radius+5,color,angle+1,forward+5,next_shape)

#Speed of the Pen - Fast Movement
turtle.speed("fast")

#BackGround Color - Turtle Screen Color
turtle.bgcolor("black")

#Size of the Pen
turtle.pensize(4)

circle(30,"red",30,1,"circle")

#Hide Pen
turtle.hideturtle()
