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

def circle(radius,color,angle,forward):
    #Set Pen color
    turtle.pencolor(next(colors))
    #Circle With Specific Radius
    turtle.circle(radius)
    #Change the Center of Circle
    turtle.forward(forward)
    #Rotate the pen to Specific Angle
    turtle.right(angle)
    #Change Radius, Angle, Center
    circle(radius+5,color,angle+1,forward+5)

#Speed of the Pen - Fast Movement
turtle.speed("fast")

#BackGround Color - Turtle Screen Color
turtle.bgcolor("black")

#Size of the Pen
turtle.pensize(4)

#Initial Circle
circle(30,"red",20,5)

#Hide Pen
turtle.hideturtle()
