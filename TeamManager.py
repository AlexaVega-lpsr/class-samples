class Player(object):
    def __init__(self, name, age, goals): 
        self.name = name
        self.age = age
        self.goals = goals
    def printStats(self):
        print("Name: " + self.name)
        print("Age: " +  self.age)
        print("Goals: " + self.goals)
    
  
myPlayers = []

answer = raw_input()
while answer != '3':
    print("Hello! Would you like to see a players stats (1), or customize a player(2), or exit(3)?")
    answer = input()
    if answer == '1':
        print("Enter Name:")
        entered_name = raw_input()
        print("Enter Age:")
        entered_age = raw_input()
        print("Enter Goals:")
        entered_goals = raw_input()
        myPlayers.append(Player(entered_name, entered_age, entered_goals))
    if answer == '2':
        for Player in myPlayers:
            Player.printStats()
