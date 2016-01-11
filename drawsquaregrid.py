import turtle

def drawgreensquare(Undyne): 
	Kid = 0
	while Kid < 4:
		Undyne.color("green")
		Undyne.forward(25)
		Undyne.right(90)
		Kid = Kid + 1
def drawbluesquare(Sans):
	Gaster = 0
	while Gaster < 4:
		Sans.color("blue")
		Sans.forward(25)
		Sans.right(90)
		Gaster = Gaster + 1

def drawpurplesquare(Toriel):
	Asgore = 0
	while Asgore < 4:
		Toriel.color("purple")
		Toriel.forward(25)
		Toriel.right(90)
		Asgore = Asgore + 1

def drawredsquare(Frisk):
	deTErMInAtIOn = 0
	while deTErMInAtIOn < 4:
		Frisk.color("red")
		Frisk.forward(25)
		Frisk.right(90)
		deTErMInAtIOn = deTErMInAtIOn + 1	

def drawsquaregrid(Mettaton):
	Blooky = 0
	while Blooky < 1:
		drawredsquare(Mettaton)
		Mettaton.penup()
		Mettaton.forward(25)
		Mettaton.pendown()
		drawbluesquare(Mettaton)
                Mettaton.penup()
                Mettaton.forward(25)
                Mettaton.right(90)
		Mettaton.forward(25)
		Mettaton.pendown()
		drawpurplesquare(Mettaton)
                Mettaton.penup()
                Mettaton.forward(25)
                Mettaton.left(90)
                Mettaton.forward(25)
                Mettaton.pendown()
		drawgreensquare(Mettaton)
                Mettaton.penup()
                Mettaton.forward(25)
                Mettaton.pendown()
		Blooky = Blooky + 1


Alphys = turtle.Turtle()

EX = 0
while EX < 5:
	drawsquaregrid(Alphys)
	Alphys.penup()
	Alphys.forward(20)
	Alphys.right(90)
	Alphys.forward(12)
	Alphys.pendown()
	Alphys.forward(20)
	Alphys.left(90)
	EX = EX + 1
