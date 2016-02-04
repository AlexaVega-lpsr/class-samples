# im opening haiku3.txt and haiku4.txt and turning them into objects
thethirdhaiku = open('haiku3.txt', 'r')
thefourthhaiku  = open('haiku4.txt', 'r')
 
 
#Printing out the following, and taking their answer and turning into an object called answer
print("Hi, welcome to the haiku reader!")
print("Choose..")
print("(3) for a haiku of a silly person")
print("(4) for a haiku about haikus")
answer = raw_input()
#If their answer was 3 it will print out the third haiku                                                              
if answer == '3':                                                                                                     
        print(thethirdhaiku.read())
                                                                                                                      
#If their answer was 4 it will print out the fourth haiku
if answer == '4':   
