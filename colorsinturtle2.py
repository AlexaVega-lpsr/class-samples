import turtle

weegee = turtle.Turtle()
weegee.speed(25)

dulce = 0

while dulce < 360:
	weegee.color("green")
	weegee.forward(1)
	weegee.left(1.15)
	dulce = dulce + 1

weegee.penup()
weegee.right(90)
weegee.forward(5)

morgan = 0
weegee.pendown()
while morgan < 360:
        weegee.color("orange")
        weegee.forward(1)
        weegee.left(1.15)
        morgan = morgan + 1




turtle.exitonclick()
