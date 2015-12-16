import turtle
import random

turts = turtle.Turtle()

turt = 0

red = random.random()

green = random.random()

blue = random.random()

turts.speed(23)  

while turt < 12:
	turts.shape("arrow")
	turts.forward(13)
	turts.right(35)
	turts.shape("turtle")
	turts.begin_fill()
	turts.fillcolor(red, green, blue)
	turts.color(red, green, blue)
	turts.circle(55)
	turt = turt + 1

turts.penup()

turts.right(129)
turts.forward(13)
turts.pendown()
turts.begin_fill()
turts.fillcolor("gold")
turts.color("gold")
turts.circle(25)
turts.end_fill()
turtle.exitonclick()
