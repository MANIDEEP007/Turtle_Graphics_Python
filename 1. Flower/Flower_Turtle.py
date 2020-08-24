import turtle
turtle.color('Green','Yellow')

#Draw Petals
for r in range(6):
    turtle.begin_fill()
    turtle.circle(r+90)
    turtle.left(50)
    turtle.end_fill()

#Lift Pen and Go to Center of Flowe
turtle.penup()
turtle.goto(0,0)
turtle.right(90)

#Draw Stem
turtle.pendown()
turtle.pensize(10)
turtle.color('green','green')
turtle.circle(240,90)
