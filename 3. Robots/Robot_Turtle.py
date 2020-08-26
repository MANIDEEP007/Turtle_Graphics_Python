import turtle
def rectangle(leng,bre,color):
    turtle.pendown()
    turtle.pensize(1)
    turtle.color(color,color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(leng)
        turtle.right(90)
        turtle.forward(bre)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

turtle.penup()
turtle.speed('fast')
turtle.bgcolor("Dodger blue")
#Foots
turtle.goto(-100,-150)
rectangle(50,20,"blue")
turtle.goto(-30,-150)
rectangle(50,20,"blue")
#Legs
turtle.goto(-30,-50)
rectangle(15,100,"grey")
turtle.goto(-65,-50)
rectangle(15,100,"grey")
#Upper Body
turtle.goto(-90,100)
rectangle(100,150,"red")
#Left Hand
turtle.goto(-150,70)
rectangle(60,15,"grey")
turtle.goto(-150,110)
rectangle(15,40,"grey")
#Right Hand
turtle.goto(10,70)
rectangle(60,15,"grey")
turtle.goto(55,110)
rectangle(15,40,"grey")
#Neck
turtle.goto(-50,130)
rectangle(20,30,"grey")
#Face
turtle.goto(-80,180)
rectangle(80,50,"red")
#Lips
turtle.goto(-55,145)
rectangle(40,8,"black")
#Left Eye
turtle.goto(-50,170)
rectangle(10,10,"white")
turtle.goto(-45,165)
rectangle(5,5,"black")
#Right Eye
turtle.goto(-30,170)
rectangle(10,10,"white")
turtle.goto(-25,165)
rectangle(5,5,"black")

turtle.hideturtle()
