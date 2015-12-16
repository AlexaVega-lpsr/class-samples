# myFractalTemplate.py
 
import turtle
import random


# make a random color
red = random.random()

green = random.random()

blue = random.random()


def makeSquare(myTurtle, side):
        squeak.color(red, blue, green)
	squeak.circle(side)
	squeak.forward(5)

 
# make our turtle
squeak = turtle.Turtle()
 
# squeak makes squares centered at the same point
# but going in a slightly rotated position with each loop
# and with a slightly smaller side length each time
length = 90
while length > 0:
        makeSquare(squeak, length)
# rotate and make the sides shorter
        squeak.right(5)
        length = length - 1
 
# wait to exit until I've clicked
turtle.exitonclick()

