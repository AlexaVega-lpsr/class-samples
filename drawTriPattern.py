import turtle

def drawtriangle(nyeh):
	nyeh.forward(10)
	nyeh.right(120)
	nyeh.forward(10)
	nyeh.right(120)
	nyeh.forward(10)
	nyeh.right(120)


def drawTri(papy):
	hill = 4
	while hill > 0:
		drawtriangle(papy)
		papy.penup()
		papy.forward(20)
		papy.pendown()
		hill = hill - 1



def drawtripattern1(heeh):
	o = 0
	while o < 3:
		heeh.penup()
		heeh.forward(30)
		heeh.pendown()
		drawtriangle(heeh)
		o = o + 1

def drawtripattern(sans):
	bone = 0
	while bone < 6:
		drawTri(sans)
		sans.penup()
		sans.goto(0,0)
		sans.right(90)	
		sans.pendown()
		sans.right(30)
		bone = bone + 1

heh = turtle.Turtle()

drawtripattern(heh)

turtle.exitonclick()
