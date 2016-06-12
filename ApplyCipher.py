import string

# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
# Im doing comments for once, what a change ;)
# Author: rc.vega.alexa [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters


def createDictionary(key):
	#I will be making an alphabet for both upper case and lower case letters! :D 
	alphabet = string.ascii_lowercase
	ALPHABET = string.ascii_uppercase
	#Now we will create our dictionary
	Dict = {}
	#The for loops will be adding all the letters to the 2 alphabets.
	for a in range(0, len(alphabet)):
		Dict[ALPHABET[(a + key) % 26]] = ALPHABET[a] 	
	for a in range(0, len(alphabet)):
		Dict[alphabet[(a + key) % 26]] = alphabet[a]
	for a in range(32, 64):
		Dict[chr(a)] = chr(a)
	return Dict

# gets the encrypted message from the user
# arguments: the decoded message
# returns: encoded message
def getMessage():
	#This will ask the user for their message then decode or encode it!
	print("Ay, what message will ya like to encode?")
	m = raw_input()
	return m

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	#we will create a blank str so we can append the users decoded message too
	nm = " "
	#This for loop will now take note of the letters in the message we have given it and decode it or encode it, then after that, it will append our secret message to nm, nm = new message WHOA 
	for b in message:
		nm = nm + dictionary[b] 
	# return the secret message
	return nm
# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	print(message)


# execution starts here

# ask user for key

try:
	print("What key would you like to use to decode?")
	key = int(raw_input())

	dictionary = createDictionary(key)
	encodedMessage = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("I have done magic! Here is your message lazy bones :3 ")
	printMessage(decodedMessage)
	
except:
	print("Sorry! Can't encode or decode that! I'm just a stupid computer!")
