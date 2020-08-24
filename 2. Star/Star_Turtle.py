import turtle

#Number of Corners in Star
corners = int(input("Enter the Number of Corners:"))

#Set Pen Color and Fill Color
turtle.color("green","green")

#Find the Angle
angle = 180-(180/corners)

#Draw and Fill the Star
turtle.begin_fill()
for _ in range(corners):
    turtle.forward(100)
    turtle.left(angle)
turtle.end_fill()


