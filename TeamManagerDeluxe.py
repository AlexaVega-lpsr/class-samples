import time

class Player(object):
	def __init__(self, name, age, goals, jn, pos): 
 
        	self.name = name
        	self.age = age
        	self.goals = goals
        	self.jn = jn
        	self.pos = pos
	def printStats(self):	
	       print("Name: " + self.name)
 	       print("Age: " +  self.age)
 	       print("Goals: " + self.goals)
 	       print("Jersey Number: " + self.jn)  
 	       print("Position:" + self.pos)
 	       print(" ")

def saveTeam(playerList, filename):
 	# open the file
	file = open((filename), "a")
 	# write it to the file
 	for o in nlist:
 		file.write(o.name + " "  + str(o.age) + " " + str(o.goals) + " " + str(o.jn) + " " + str(o.pos) + " ")
	# close the file
	file.close()	 
 
 
#takes a file name for a file of players
#returns a list of Players
def LoadTeam(filename, file): 
	list = []
        file = open(filename, "w", )
	wrds = file.readline()
	while file != " ":
		file.split()
		stry = file.split()
		list.append(Player(stry[0], stry[1], stry[2], stry[3], stry[4]))
		file = filename.readline()
	file.close()
	return list
 
 
print("Hello! Welcome to Team Manager Deluxe!" '\n' "Enter the 3 of your choice and press Enter.")
print("(1) Start with a new team" '\n' "(2) Open a file for an existing team")
answer_choice = int(raw_input())
 
 
if answer_choice == 2:
        print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
        filename = raw_input()
	file = open(filename, "w")
	my_players = LoadTeam(filename, file)
        print("Success!... What now...?")
else:
        my_players = []
        list = []
 
nlist = []
print("Enter any number!")
time.sleep(.5)
print("(1) Make a Player")
time.sleep(.2)
print("(2) List Players")
time.sleep(.2)
print("(3) Save Players")
time.sleep(.2)
print("(4) Exit and Delete Players")
time.sleep(.2)
 
 
a = raw_input() 
while a != "4":
 
        if a == "1":
 
# user creates a player with name, age etc
 
                print("_____________________________________")
 
                print("Enter FIRST Name: ")
 
                name = raw_input()
 
 
                print("Enter Age: ")
 
                age = raw_input()
 
 
                print("Enter Goals: ")
 
                goals = raw_input()
 
 
 
                print("Enter Jersey Number: ")
 
                jn = raw_input()
 
 
 
                print("Enter Position: ")
 
                pos = raw_input()
 
 
# saves name, age, and goals to their profile and adds to list
 
                nlist.append(Player(name, age, goals, jn, pos))
                time.sleep(.5)
 
                print(" ")
 
                print("Player Made.")
 
                print("_____________________________________")
 
 
# more options
 
                time.sleep(.6)
 
                print("Anything else?")
 
                time.sleep(1)
 
                print("(1) Make Player")
 
                time.sleep(.1)
 
                print("(2) List Players")
 
                time.sleep(.1)
 
                print("(3) Save Players")
 
                time.sleep(.1)
 
                print("(0) Exit and delete players")
 
                time.sleep(.1)
 
                a = raw_input()
 
 
# if 2, will print the player's stats -- name, age etc
 
        elif a == "2":
 
                time.sleep(1)
 
                print("-------------------------------------")
 
                print("Current List:")
 
                time.sleep(.5)
 
                for p in nlist:
                        p =  p.printStats()
 
                        time.sleep(.5)
 
                for pl in list:
 
                        pl.printStats()
 
                        time.sleep(.5)
 
                print("-------------------------------------")
 
 
# more options
 
                time.sleep(.6)
 
                print("Anything else?")
 
                time.sleep(.1)
 
                print("(1) Make Player")
 
                time.sleep(.1)
 
                print("(2) List Players")
 
                time.sleep(.1)
 
                print("(3) Save Players")
 
                time.sleep(.1)
 
                print("(4) Exit and delete players")
 
                time.sleep(.1)
 
                a  = raw_input()
 
 
# if user input equals 3
 
# will add the new list to the loaded list and save to the same file to load later
 
        if a  == "3":
 
                print("What will your file be called? (include .tmd)")
 
                filename = raw_input()  
 
                x = saveTeam(list, filename)
 
		nlist.append(x)

                time.sleep(.3)
 
                print("Saved it!  Press (4) to exit. Restart the program to view your team.")
 
                a  = raw_input()
 
# if they enter 4
 
	if a  == "4":
 
        	time.sleep(.5)
 
	        print("Good bai")

		a = "4"
