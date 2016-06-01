class Player(object):
	def __init__ (self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	def printStats(self):
		print("Name: " + self.name)
		print("Age: " + self.age)
		print("Goals: " + self.goals)
myPlayers = []
nanalan = []
while nanalan != '3':
	print("Choose an option:")
	print("(1) Add player")
	print("(2) Print players")
	print("(3) End")
	nanalan = input()
	if nanalan == '1':
		print("Enter name:")
		user_entered_name = input()
		print("Enter age:")
		user_entered_age = input()
		print("Enter goals:")
		user_entered_goals = input()
		myPlayers.append(Player(user_entered_name, user_entered_age, user_entered_goals))
	if nanalan == '2':
		for Player in myPlayers:
			Player.printStats()
