import turtle

def drawTee(myTurtle):
	myTurtle.forward(200)
	myTurtle.backward(50)
	myTurtle.right(90)
	myTurtle.forward(50)
	myTurtle.backward(100)
	myTurtle.forward(50)
	myTurtle.right(90)
	myTurtle.forward(150)
	myTurtle.right(90)




def draw4T(myTurtle):
	c = 0
	while c < 4:
		drawTee(squirtle)
		c = c + 1


squirtle = turtle.Turtle()

draw4T(squirtle)

turtle.exitonclick()


