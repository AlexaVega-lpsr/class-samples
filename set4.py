# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
 
# bring in the packages of functions we need
import random
import turtle
 
# Make random colors available for the functions

red = random.random()

green = random.random()

blue = random.random()


# -------- functions start here ----------------
 
def regular_triangle(myTurtle, x, y, side):
        myTurtle.color(red, blue, green)
	myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        while side_count < 3:
                myTurtle.forward(side)
                myTurtle.right(120)
                side_count = side_count + 1
 
def regular_square(myTurtle, x, y, side):
        myTurtle.color(red, green, blue)
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	sides = 0
	while sides < 4:
		myTurtle.forward(side)
		myTurtle.right(90)
		sides = sides + 1
 
def regular_pentagon(myTurtle, x, y, side):
        myTurtle.color(red, green, blue)
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	sidess = 0
	while sidess < 5:
		myTurtle.forward(side)
 		myTurtle.left(72)
		sidess = sidess + 1
def regular_hexagon(myTurtle, x, y, side):
 	myTurtle.color(red, green, blue)
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        sidess = 0
        while sidess < 6:
                myTurtle.forward(side)
                myTurtle.right(60)
                sidess = sidess + 1

 
def regular_octagon(myTurtle, x, y, side):
	myTurtle.color(red, green, blue)
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        sidess = 0
        while sidess < 8:
                myTurtle.forward(side)
                myTurtle.right(45)
                sidess = sidess + 1

def regular_triforce(myTurtle, x, y, side):
	myTurtle.color(red, blue, green)
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	ganon = 0
	zelda = 0
	sheik = 0
	while ganon < 3:
		myTurtle.forward(100)
		myTurtle.left(120)
		ganon = ganon + 1
	myTurtle.right(120)
	myTurtle.forward(2)
	while sheik < 3:
		myTurtle.forward(100)
        	myTurtle.left(120)
		sheik = sheik + 1
	myTurtle.forward(100)
	myTurtle.left(120)
	myTurtle.forward(100)
	while zelda < 3:
        	myTurtle.forward(100)
        	myTurtle.left(120)
		zelda = zelda + 1

	


def circle(myTurtle, x, y, radius):
	myTurtle.color(red, green, blue)
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
	linesss = 0
	while linesss < 3:
		myTurtle.circle(radius)
		linesss = linesss + 3
# -------- execution starts here ----------------
 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
 
squirt = turtle.Turtle()
 
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, triforce, and circle.")
        print("If you're done making shapes, just type 'exit'.")
        shape = raw_input()
 
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
 
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        elif shape == 'hexagon':
                regular_hexagon(squirt, randx, randy, randside)
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)
	elif shape == 'triforce':
		regular_triforce(squirt, randx, randy, randside)
