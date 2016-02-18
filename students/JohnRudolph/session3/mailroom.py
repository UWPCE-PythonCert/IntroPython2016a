
'''
################################################################################
GENERATE RANDOM DONOR LIST
################################################################################
'''


def createDonors(numDonors):
    '''
    This function is used to create a donorlist
    Input desired number of into donorlist function
    For each donor input function will randomly generate_
    # of donations between 1-3
    And randomly generate a donation amount between 100-1000
    Will return a list of lists
    '''

    donorList = []

    for x in range(numDonors):

        # random # of donations between 1-3 inclusive
        numDonations = random.randint(1, 3)
        # list that holds donor name and donations amounts
        donsubList = ['donor name' + str(x + 1)]

        # create random donations amounts between $100-$1K
        for y in range(numDonations):
            donsubList.append(random.randint(100, 1000))

        donorList.append(donsubList)

    return donorList

'''
################################################################################
GENERAL FUNCTIONS
################################################################################
'''


def actionPrompt():
    '''
    This function prompts a user to select an action:
    "Send thank you" or "create a report"
    Function will loop until one of these is entered
    '''
    index_check = None
    while index_check is None:
        getAction = str(
            input("Input Action: 'Send a Thank You'\t'Create a Report'\t'Quit'\n"))
        if getAction.lower() not in ['send a thank you', 'create a report', 'quit']:
            print("Invalid Action: Try Again!")
        else:
            index_check = True
            return getAction

'''
################################################################################
THANK YOU FUNCTIONS
################################################################################
'''


def appendDonor(getName):
    '''
    This functions find the donor in the dictionary
    Prompts user for new donations and appends donation to the dictionary key
    If user does not enter a number then error will be raised
    '''
    donCheck = None
    while donCheck is None:
        try:
            donation = int(input('Enter donation amount (int) for {}:\n'.format(getName)))
            ownerDic.setdefault(getName, []).append(donation)
            print(getName, ownerDic[getName])
            donCheck = True
        except:
            print('You did not enter a valid integer Try Again!')


def sendThanks(getName):
    '''
    This function runs the steps for sending a thank your
    If user select list then print current donor dic and reprompt
    If donor is already in dic then append amounts
    If donor not in dic then append new donor and add amount
    '''
    if getName.lower() == 'list':
        for key in sorted(ownerDic):
            print(key)
        getName = input("Input a full name or 'list'\n")
        sendThanks(getName)
    elif getName in ownerDic.keys():
        print('Adding a new donation for: {}'.format(getName))
        appendDonor(getName)
        emailThanks(getName)
    elif getName == 'quit':
        print('Quitting Thank You')
    else:
        print('Adding {} to Donor Database'.format(getName))
        ownerDic.setdefault(getName, [])
        appendDonor(getName)
        emailThanks(getName)


def emailThanks(getName):
    '''
    This function grabs the last donation entered for a given donor
    Print a thank you message with donor name and donation amount
    '''
    donationList = list(ownerDic[getName])
    print('Thank you {} for your generous donation of ${}!'.format(
        getName, donationList[-1]))

'''
################################################################################
DONORS REPORT FUNCTIONS
################################################################################
'''


def getKey(item):
    '''
    Function used to sort second item in a list of lists
    '''
    return item[1]


def createtopDonors():
    '''
    Creates a new list with total donations, donation count and avg donations
    by looping over master donor dictionary
    New list is sorted based on total donation
    '''
    sortList = []
    for key in ownerDic:
        totalDon = sum(list(ownerDic[key]))
        countDon = len((list(ownerDic[key])))
        avgDon = int(totalDon / countDon)
        sortList.append([key, totalDon, countDon, avgDon])

    return(sorted(sortList, key=getKey, reverse=True))


def outputTopDonors(topDonors):
    '''
    This function loops through the sorted top donors list
    And prints each itemn in tabular format
    '''
    print('Donor Name\tTotal\tCount\tAverage')
    for x in topDonors:
        print('{}\t{}\t{}\t{}'.format(*x))


'''
################################################################################
MAIN CODE BLOCK
################################################################################
'''
if __name__ == '__main__':

    import random

    check = None
    while check is None:
        try:
            # create an arbitrary # of donors - 5 per assignment directions
            numDonors = int(
                input('Enter number (int) of donors to generate\n'))
            check = True
        except:
            print('You did not enter a valid int - Try again!')

    # create the initial list of donors
    donorList = createDonors(numDonors)
    # create an empty dictionary - will be populated in loop below
    ownerDic = {}
    # populate donor dict from donorlist
    for donor in donorList:
        donor_name = donor[0]
        donations = donor[1:]
        ownerDic[donor_name] = donations

    # flag used to quit prompting user for an action
    quit_check = False

    while quit_check is False:
        getAction = actionPrompt()
        if getAction.lower() == 'send a thank you':
            getName = input("Input a full name or 'list'\n")
            sendThanks(getName)
        elif getAction.lower() == 'create a report':
            topDonors = createtopDonors()
            outputTopDonors(topDonors)
        elif getAction.lower() == 'quit':
            print('Quitting Program!')
            quit_check = True
