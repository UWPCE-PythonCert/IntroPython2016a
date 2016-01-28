'''
################################################################
				CREATE DONOR LIST AND ASK FOR ACTION
################################################################
It should have a data structure that holds a list of your donors 
and a history of the amounts they have donated. This structure 
should be populated at first with at least five donors, with between 
1 and 3 donations each

The script should prompt the user (you) to choose from a menu of 
2 actions: ‘Send a Thank You’ or ‘Create a Report’
'''

import random

def createDonors(numDonors):
	'''
	This function is used to create a list of donorlist
	Input desired number of donorlist
	For each donor input function will randomly generate # of donations between 1-3
	And randomly generate a donation amount between 100-1000
	Will return a list of lists
	'''

	donorList = []

	for x in range(numDonors):

		numDonations = random.randint(1,3) #random # of donations between 1-3 inclusive
		donsubList = ['donor' + str(x+1)] #list that holds donor name and donations amounts

		for y in range(numDonations): #create random donations amounts
			donsubList.append(random.randint(100,1000))

		donorList.append(donsubList)

	return donorList

#create an arbitrary # of donors - 5 per assignment directions
numDonors = 5
# dreate the initial list of donors
donorList = createDonors(numDonors)

#create an empty dictionary - will be populated in loop below
ownerDic = {}
#populate donor dict from donorlist
for donor in donorList:
	donor_name = donor[0]
	donations = donor[1:]
	ownerDic[donor_name] = donations

#Add an error handler so that user has to input a valid action
index_check = None
while index_check is None:
	getAction = str(input("Input Action: 'Send a Thank You' or 'Create a Report\n"))
	if getAction.lower() != ('send a thank you' or 'create a report'):
		print("Invalid Action: Try Again!")
	else:
		index_check = True

'''
################################################################################
						THANK YOU ACTION
################################################################################
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
If the user types ‘list’, show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data 
    structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isn’t.
Once an amount has been given, add that amount to the donation history 
    of the selected user.
Finally, use string formatting to compose an email thanking the donor for 
    their generous donation. Print the email to the terminal and return to 
    the original prompt.
'''

def appendDonor(getName):
	'''
	This function find the donor in the dictionary
	Prompts user for new donations and appends donation to the dictionary key
	If user does not enter a number then error will be raised
	'''
	donCheck = None
	while donCheck is None:
		try:
			donation = float(input('Enter donation amount:\n'))
			ownerDic.setdefault(getName, []).append(donation)
			print(ownerDic[getName])
			donCheck = True
		except:
			print('You did not enter a number. Try Again!')

if getAction == 'send a thank you':
	getName = input("Input a full name\n")
	if getName.lower() == 'list':
		print(ownerDic)
	elif getName in ownerDic.keys():		
		appendDonor(getName)
	else:
		print('Adding ', getName, ' to Donor Database')
		ownerDic.setdefault(getName, [])
		appendDonor(getName)










		







