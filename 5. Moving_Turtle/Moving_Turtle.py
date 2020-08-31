import turtle
import random

#Define Boundaries
def inside_window():
    #Knowing Limits of X-Axis
    left_limit = (-turtle.window_width()) / 2.0 + 100
    right_limit = (turtle.window_width()) / 2.0 - 100
    #Knowing Limits of Y-Axis
    top_limit = turtle.window_height() / 2.0 - 100
    bottom_limit = (-turtle.window_height()) / 2.0 + 100
    #Get the Cursor Position
    (x,y) = turtle.pos()

    #Check Trutle is inside the Window or not
    inside = (left_limit < x < right_limit)and \
             (bottom_limit < y < top_limit)
    return inside

def move_turtle():
    #If Turtle is inside Window Move it Randomly
    if inside_window():
        angle = random.randint(0,180)
        distance = random.randint(50,300)
        turtle.right(angle)
        turtle.forward(distance)
    #If Turtle is not inside Move it Backward
    #so it comes inside window
    else:
        turtle.backward(300)

#Speed of Pen
turtle.speed("slow")

#Pen Size
turtle.pensize(10)

#Draw Turtle
turtle.shape("turtle")

#Fill Color
turtle.fillcolor("gold")

#Background color
turtle.bgcolor("black")

#Move Turtle
while True:
    move_turtle()
