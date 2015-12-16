import turtle

link = turtle.Turtle()

ganon = 0

zelda = 0

sheik = 0

link.color("gold")

while ganon < 3:
	link.begin_fill()
	link.fillcolor("yellow")
	link.forward(100)
	link.left(120)
	link.end_fill()
	ganon = ganon + 1

link.right(120)
link.forward(2)

while sheik < 3:
	link.begin_fill()
        link.fillcolor("orange")
        link.forward(100)
        link.left(120)
        link.end_fill()
	sheik = sheik + 1

link.forward(100)
link.left(120)
link.forward(100)

while zelda < 3:
        link.begin_fill()
        link.fillcolor("gold")
        link.forward(100)
        link.left(120)
        link.end_fill()
	zelda = zelda + 1


turtle.exitonclick()
