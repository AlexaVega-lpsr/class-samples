import turtle

t = turtle.Turtle()

t.fillcolor("red")
t.begin_fill()

li = 0

while li < 3:
	t.forward(100)
	t.left(120)
	li = li + 1

t.end_fill()
turtle.exitonclick()
