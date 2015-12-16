
import turtle

Squirtle = turtle.Turtle()

Squirtle.shape("turtle")

Squirtle.color("red")

lines = 0

while lines < 8:
	Squirtle.forward(100)
	Squirtle.backward(100)
	Squirtle.left(45)
	lines = lines + 1
