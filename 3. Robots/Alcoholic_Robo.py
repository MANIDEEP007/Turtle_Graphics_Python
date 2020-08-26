import turtle
def rectangle(leng,bre,color):
    turtle.pendown()
    turtle.pensize(1)
    turtle.color(color,color)
    turtle.begin_fill()
    for _ in range(2):
        #Horizontal Lines of Rectangle
        turtle.forward(leng)
        turtle.right(90)
        #Vertical Lines of Rectangle
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
#Left Arm
turtle.goto(-150,70)
rectangle(60,15,"grey")
turtle.goto(-150,110)
rectangle(15,40,"grey")
#Right Arm
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
turtle.goto(-50,170)
rectangle(5,5,"black")
#Right Eye
turtle.goto(-30,170)
rectangle(10,10,"white")
turtle.goto(-30,165)
rectangle(5,5,"black")
#Left Hand
turtle.goto(-155,120)
rectangle(25,10,"green")
turtle.goto(-155,135)
rectangle(5,15,"green")
turtle.goto(-135,135)
rectangle(5,15,"green")
#Right Hand
turtle.goto(50,120)
rectangle(25,10,"green")
turtle.goto(50,135)
rectangle(5,15,"green")
turtle.goto(70,135)
rectangle(5,15,"green")
#Hide Pen
turtle.hideturtle()
