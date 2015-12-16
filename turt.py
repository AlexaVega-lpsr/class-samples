#square.py

import turtle

#make our turtle
Eddy = turtle.Turtle()

Eddy.shape("turtle")
Eddy.color("orange")
#Eddy makes a square
lines = 0
while lines < 4:
	Eddy.forward(150)
	Eddy.left(90)
	lines = lines + 1

turtle.exitonclick()


