 
#Introduction:
print("Welcome to the haiku Generator!")
print("Provide the first line of your Haiku(5):")
line = raw_input()
 
print("Provide your second line of Haiku(7):")
secondline = raw_input()
 
print("Provide your last line of Haiku(5):")
thirdline = raw_input()
 
print("What would you like to name your haiku's file?")
filename = raw_input()
 
print("Done! Type in cat (name of your file).txt")
file = open((filename), "a")
 
file.write(line + '\n' + secondline + '\n' + thirdline + '\n')
 
file.close()
 
 
 
 
 
