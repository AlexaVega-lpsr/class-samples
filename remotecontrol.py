import turtle
from Tkinter import *

def maketriangle(myTurtle, side):
        myTurtle.forward(side)
        myTurtle.left(120)
        myTurtle.forward(side)
        myTurtle.left(120)
        myTurtle.forward(side)
        myTurtle.left(120)


# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
bwd = Button(frame, text='bwd', command=lambda: shawn.backward(50))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
red = Button(frame, text='red', command=lambda: shawn.color("red"))
orange = Button(frame, text='orange', command=lambda: shawn.color("orange"))
triangle = Button(frame, text='triangle', command=lambda: maketriangle(shawn,90))
yellow = Button(frame, text='yellow', command=lambda: shawn.color("yellow"))
green = Button(frame, text='green', command=lambda: shawn.color("green"))
blue = Button(frame, text='blue', command=lambda: shawn.color("blue"))
black = Button(frame, text='black', command=lambda: shawn.color("black"))
purple = Button(frame, text='purple', command=lambda: shawn.color("purple"))
slightright = Button(frame, text='slightright', command=lambda: shawn.right(45))
slightleft = Button(frame, text='slightleft', command=lambda: shawn.left(45))


# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
bwd.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
red.pack(side=LEFT)
orange.pack(side=LEFT)
yellow.pack(side=LEFT)
green.pack(side=LEFT)
blue.pack(side=LEFT)
triangle.pack(side=LEFT)
purple.pack(side=LEFT)
black.pack(side=LEFT)
slightright.pack(side=LEFT)
slightleft.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
