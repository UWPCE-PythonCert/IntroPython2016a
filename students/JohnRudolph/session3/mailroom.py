#Creating list for each donor containing donation amounts
#onorlist = [('donor1', 100, 200, 300)]
#donorlist.append(('donor2', 200, 300, 400))

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


print(createDonors(5))


