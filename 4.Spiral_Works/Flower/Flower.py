import turtle
def circle(radius,color,angle):
    #Set Pen color
    turtle.pencolor(color)
    #Circle With Specific Radius
    turtle.circle(radius)
    #Rotate the pen to Specific Angle
    turtle.right(angle)

#Speed of the Pen - Fast Movement
turtle.speed("slow")

#BackGround Color - Turtle Screen Color
turtle.bgcolor("black")

#Size of the Pen
turtle.pensize(4)

#Draw Flower
for _ in range(9):
    circle(20,"red",40)

#Hide Pen
turtle.hideturtle()
