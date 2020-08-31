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

def circle(radius,color,angle):
    #Set Pen color
    turtle.pencolor(next(colors))
    #Circle With Specific Radius
    turtle.circle(radius)
    #Rotate the pen to Specific Angle
    turtle.right(angle)

#Speed of the Pen - Fast Movement
turtle.speed("fast")

#BackGround Color - Turtle Screen Color
turtle.bgcolor("black")

#Size of the Pen
turtle.pensize(4)

#Draw Colorful Flower
for _ in range(9):
    circle(50,"red",40)

#Hide Pen
turtle.hideturtle()
