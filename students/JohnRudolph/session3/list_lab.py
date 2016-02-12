#!/usr/bin/python3.4

'''
#########################################################################
					SECTION 1 OF LIST LAB
#########################################################################

#1 Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
#2 Display the list
#3 Ask the user for another fruit and add it to the end of the list
#4 Display the list
#5 Ask the user for a number and display the number back to the user and 
	the fruit corresponding to that number (on a 1-is-first basis)
#6 Add another fruit to the beginning of the list using “+” and display the list
#7 Add another fruit to the beginning of the list using insert() and display the list
#8 Display all the fruits that begin with “P”, using a for loop
'''

#1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

#2
print(fruit)

#3
new_fruit = input("Add another fruit to list\n")

fruit.append(new_fruit)

#4
print(fruit)

#5
#Add an error handler so that user has to input a valid list index
index_check = None
while index_check is None:
	try:
		get_num = int(input("Select a number from 1 to " + str(len(fruit)) + " inclusive\n"))
		print(get_num, " ", fruit[get_num - 1])
		index_check = True
	except:
		print("Invalid index number try again")

#6
new_fruit = [input("Add another new fruit to list\n")]

fruit = new_fruit + fruit

print("List with ", new_fruit[0],"\n", fruit)

#7
new_fruit  = input("Add another fruit to list\n")

fruit.insert(0,new_fruit)

print("List with ", new_fruit,"\n", fruit)

#8
#create empty list to hold values that will be populated in loop below
p_fruits = []

#loop over each fruit in list and determine if fruit starts with p (not case sensitive)
for item in fruit:
	if item[0].lower() == "p":
		p_fruits.append(item)

print("List of fruits that start with P\n", p_fruits)


'''
#########################################################################
					SECTION 2 OF LIST LAB
#########################################################################

#9 Display the list.
#10 Remove the last fruit from the list.
#11 Display the list.
#12 Ask the user for a fruit to delete and find it and delete it.
#13 Bonus: Multiply the list times two. Keep asking until a match is found. 
	Once found, delete all occurrences.)
'''

#9
print("Current fruit list\n", fruit)

#10
#creating a new list called fruit 2 based on list from section 1
fruit2 = list(fruit)
del fruit2[-1]

#11
print("Deleted the last item from list\n", fruit2)

#12
#Add an error handler so that user has to input a valid list index
index_check = None
while index_check is None:
	try:
		get_str = input("Type a fruit from current list to delete\n")
		fruit2.remove(get_str)
		index_check = True
	except:
		print("The fruit you typed in not in the list! Try again ")

print("You deleted ", get_str, "New list\n", fruit2)

#13 - Doing this on the deleted list from #12
'''
First while loop checks to see if fruit entered exists in list
If fruit does exist in list the loop through list until all instance of fruit is removed
If fruit does not exist in list then copy fruit list and append to existing list
'''
index_check = None #flag to determine if a valid fruit has been entered
while index_check is None:
	get_str = input("Type the fruit from current list to delete\n")
	if get_str in fruit2:
		while get_str in fruit2:
			fruit2.remove(get_str)
			index_check = True #set flag to True to quit valid fruit loop
	else:
		fruit2_copy = list(fruit2)
		fruit2 = fruit2_copy + fruit2_copy
		print("The fruit you typed in not in the list so I doubled the list! Try again ")
		print(fruit2)

print("You deleted ", get_str,"\n", fruit2)

'''
#########################################################################
					SECTION 3 OF LIST LAB
#########################################################################
#14 Ask the user for input displaying a line like “Do you like apples?”
#15 Display the list.
'''

#14
for item in fruit:
	'''
	For each item in fruit list prompt a response from user
	If reponse is not yes or no then retry
	Else if no then remove item from list
	'''
	response = input("Do you like " + item.lower() + " ?\n")
	
	while response.lower() not in ["yes", "no"]:
		print("You didn't answer Yes or No! Try again. ")
		response = input("Do you like " + item.lower() + " ?\n")

	if response == 'no':
		fruit.remove(item)
#15
print(fruit)

'''
#########################################################################
					SECTION 4 OF LIST LAB
#########################################################################
#16 Make a copy of the list and reverse the letters in each fruit in the copy.
#17 Delete the last item of the original list. Display the original list and the copy.
'''
#16
fruit_copy = list(fruit)

for item in fruit_copy[:]:
	item_flip = item[::-1]	
	fruit_copy.remove(item)
	fruit_copy.append(item_flip)

#17
del fruit[-1]

print(fruit)
print(fruit_copy)







