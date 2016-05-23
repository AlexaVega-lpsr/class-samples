# this allows the program to get the contact information
# arguments: dictionary_name, contact_name, contact_number
# returns:none
def getNumber(contacts_list, contact_name, contact_number):
	contacts_list[contact_name] = contact_number	
# this allows the user to print all of the contacts
# arguments: dictonary
# returns: contacts' name and number
def printContacts(contacts_list):
	for contact in contacts_list:
		print(" ")
		print(contact + ": " + contacts_list[contact])
# this allows the user to print a certain contact
# arguments: name and dictonary
# returns: that specific's contact information
def accessContacts(contacts_list, name):
	for contact in contacts_list:
		if contact == name:
			print(" ")
			print(contact + ": " + contacts_list[contact])
# this will remove a contact from the list
# arguments: dictionary, name
# returns: none 
def removingContact(contacts_list, name):
	print(" ")
	del contacts_list[name]
# this will allow the user to change a contact from the list
# argument: directory, name
# returns: none
def changeContact(contacts_list, name):
	print(" ")
	print("What do you want to change? The 'name', 'number', or 'both'? Type it below:")
	decision_made = raw_input()
	if decision_made == 'name':
		print(" ")
		print("What is the new name that you want the contact to have now? Type it below:")
		new_name = raw_input()
	if decision_made == 'number':
		print(" ")
		print("What is the new number that you want the contact to have now? Type it below:")
		new_number = raw_input()
	if decision_made == "both":
		print(" ")
		print("What is the new name that you want the contact to have now? Type it below:")
		new_name = raw_input()
		print(" ")
		print("What is the new number that you want the contact to have now? Type it below:")
		new_number = raw_input()
	if decision_made == "name":
		new_number = contacts_list[name]
	if decision_made == "number":
		new_name = name
	contacts_list[new_name] = new_number
	del contacts_list[name]
# this is setting a value of 0 to the variable that allows the loops to begin
user_decision = "0"
# Here is an empty list!
my_Dictionary = {}

while user_decision == "0":
# this asks the user for their decision!
	print(" ")
	print("Hello there, and welcome to to Contacts.app")
	print("You have three choices:")
	print("Add a phone number (1)")
	print("Print the full list of contacts (2)")
	print("Retrieve a contact number (3)")
	print("Exit the app (0)")
	decision = input()
# If decision is 1 this will happen
	if decision == "1":
		print(" ")
		print("What is the name of the contact?")
		name = input()
		print(" ")
		print("What is the number of the contact? Type the dashes:")
		number = str(input())
		phone_number = getNumber(my_Dictionary, name, number)
# if decision 2 is chosen, it will print all the contacts
	if decision == "2":
		print(" ")
		print("Here is the list of your phone numbers:")
		contacts_list = printContacts(my_Dictionary)
# If decision 3 is chosen, it will print a certain person.	
	if decision == "3":
		print(" ")
		print("What is the name of your contact?")
		contact_name = input()
		contact_Name = accessContacts(my_Dictionary, contact_name)
	if decision == "0":
		print(" ")
		print("Thank you for choosing contact.app! Goodbye!")
		user_decision = "1"
