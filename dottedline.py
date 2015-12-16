import turtle

notshawn = turtle.Turtle()

count = 0
while count < 100:
	notshawn.forward(5)
	notshawn.penup()
	notshawn.forward(5)
	notshawn.pendown()
	count = count + 1

notshawn.penup()
notshawn.goto(-100,-55)

notshawn.pendown()
notshawn.circle(10)


	
turtle.exitonclick()

