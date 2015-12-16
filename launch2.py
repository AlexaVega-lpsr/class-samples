import turtle

usuf = turtle.Turtle()
count = 10
while count > 0:
	usuf.forward(count*10)
	usuf.right(90)
	count = count - 1

turtle.exitonclick()
