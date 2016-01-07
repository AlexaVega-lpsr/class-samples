import turtle


def drawSide(myturtle):
	count = 0
	while count < 4:
		drawVee(myturtle)
		count = count + 1

def drawVee(myturtle):
	myturtle.forward(10)
	myturtle.right(90)
	myturtle.forward(10)
	myturtle.left(90)

shawn = turtle.Turtle()
count = 0
while count < 4:
	drawSide(shawn)
	shawn.right(90)
turtle.exitonclick()
