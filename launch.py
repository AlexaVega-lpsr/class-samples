import turtle

def makeSquare(myTurtle, side):
 	lines = 0
	while lines < 4:
		myTurtle.forward(side)
		myTurtle.left(90)
		lines = lines + 1

squeak = turtle.Turtle()
makeSquare(squeak, 30)
makeSquare(squeak, 60)
