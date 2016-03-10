# list lab execises from session-03

import random
import string
import sys
import os

# List of fruits
mylist = ["apples", "pears","oranges","peaches"]

# Display the list
print('\n',"List of fruit",mylist,'\n')

# Prompt for another type of fruit
newfruit = input('Enter a type of fruit:')

mylist.append(newfruit)

mylen = len(mylist)

# Display the list with the new fruit added
print("List of fruit with the {} added".format(newfruit),mylist,'\n')

# Prompt for a number
num = int(input('Enter a number from 1 to {:d}:'.format(mylen)))
#int(input("Please enter an integer: "))

for i in range(0,mylen):
	if (i == num-1):
		print("The fruit at that number is",mylist[i],'\n')

addfruit = ["lemon"]
mylist = addfruit + mylist

# Display the list with lemon added
print("List of fruit with lemon added",mylist)

mylist.insert(0,"kiwi")

# Display the list with kiwi added
print("List of fruit with kiwi added",mylist,'\n')

for i in mylist:
	# find fruits that start with a 'P'
	if (i[0] == "p"):
		print("This fruit starts with p",i,'\n')


############################## Series 2 ---- actions #######################################
# Display the list
print("List of fruit:",mylist,'\n')

# Remove the last fruit
mylist.pop()

# Display the list
print("List of fruit with the last item removed:",mylist,'\n')

# Double the elements in the list
mylist = mylist + mylist
# Display the list
print("List of fruit.... multiplied by 2:",mylist,'\n')

# Prompt for a fruit to delete
delfruit = input('Enter a fruit to be deleted:')

temp = mylist.copy()
lenth = len(temp)

# for loop to go through the list and delete occurances of the seleted fruit
for i in range(0,(lenth-1)):
	if (temp[i] == delfruit):
		#delete the spcified fruit
		mylist.remove(temp[i])
	else:
		print("This fruit was not selected for removal",temp[i],'\n')

# Display the list with the selected fruit removed
print("List of fruit with all occurances of {} removed".format(delfruit),mylist,'\n')

############################## Series 3 ---- actions #######################################

# Change each fruit's first letter to capital
ntemp = mylist.copy()
for i, elem in enumerate(ntemp):
	s = elem
	mylist.remove(elem)
	# Set the first letter in each item in the list to upper case
	s = s.capitalize()
	elem = s
	# insert the the capitalized item right back in its place
	mylist.insert(i,elem)

# Display the list with each item capitalized
print("List of fruit with each item capitalized ...:",mylist,'\n')

# Change each fruit's first letter to lower case
ntemp = mylist.copy()
for i, elem in enumerate(ntemp):
	s = elem
	mylist.remove(elem)
	# Set the first letter in each item in the list to lower case
	s = s.lower()
	elem = s
	# insert the the capitalized item right back in its place
	mylist.insert(i,elem)

# Display the list with each item in lower case 
print("List of fruit with each item in lower case ...:",mylist,'\n')

tlist = mylist.copy()
# Loop through the list and ask the user if they like the fruit item
for i in tlist:
	# Prompt for a fruit to delete
	answ = (input('Do you like {}:'.format(i)))
	if (answ == "no"):
		# Remove the item
		mylist.remove(i)
	elif (answ == "yes"):
		print('you like this fruit:',i,'\n')
	# insist on a "yes" or "no" answer
	else:
		answ = input('Enter "yes" or "no" Please:')
		if (answ == "no"):
			# Remove the item
			mylist.remove(i)
		elif (answ == "yes"):
			print('you like this fruit:',i,'\n')

# Display the list of liked fruits
print("List of fruit with the ones you don't like removed:",mylist,'\n')

############################## Series 4 ---- actions #######################################

# copy the last list
nextlist = mylist.copy()
print("List of fruit displayed... ",nextlist,'\n')
nlist = []
ilist = []
# loop through the list of fruit items 
for i in nextlist:
	n = 1
	strg = ''
	# Loop through each fruit item to get each letter that needs to be reversed
	for j in i:
		ln = len(i)
		last = (i[ln-n])
		n = n+1
		if (n > 1):
			strg = ''.join((strg,last))
			ilist = [strg]
	nlist = nlist + ilist
	
# Display the list of liked fruits
print("List of fruit with letters in each fruit reversed...",nlist,'\n')

# copy the list
lastlist = nextlist.copy()

# Remove last item in the list
lastlist.pop()

# Display the original list
print("The original list of fruit displayed... ",nextlist,'\n')


# Display the original list
print("The original list of fruit with the last item deleted... ",lastlist,'\n')
