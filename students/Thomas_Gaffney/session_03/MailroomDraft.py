def sendathankyou(donorDict):
        userselection = input('Please input the name of the donor, or list to display a list of current users:')
        if(userselection == 'list'):
            print(donorDict.keys())
            sendathankyou(donorDict)
        elif(userselection in donorDict.keys()):
            user = userselection
        else:
            user = userselection
            donorDict[user] = []
        donationamount = input('Please enter the donation amount for the selected user:')

        #Test if a number was given.
        while (True):
            try:
                float(donationamount)
                break
            except:
                donationamount = input('That was not a number, please try again:')

        donorDict[user].append(float(donationamount))
        thankyou = 'Dear {user}: \n \nThank You For Your Generous Donation of {donationamount}. \n \nThe Charity \n'.format(user = user, donationamount = donationamount)
        print(thankyou)

def printareport(donorDict):
    str = ""
    for key in donorDict:
        str += '|{donor}  |{donated}  |{donations}  |{avgdonation}|\n'.format(donor = key,
                                                                               donated = sum(donorDict[key]),
                                                                               donations = len(donorDict[key]),
                                                                               avgdonation = sum(donorDict[key])/len(donorDict[key]))
    print(str)


if __name__ == '__main__' :
    donorDict = {'Tom Jones' : [25, 10, 15],
             'Brad Hardy' : [5, 9],
             'Manuel Miller' : [4, 21],
             'Josh Benson' : [1],
             'Ashley Scanlon' : [4, 9, 50]}

    while(True):
        userinput = input('Welcome to the mailroom!  Would you like to :\n    \1. Send a Thank you  \n    2. Create a report  \n    3.  Quit \nChoice 1, 2 or 3?:')
        if (userinput == str(1)):
            donorDict = sendathankyou(donorDict)
        if (userinput == str(2)):
            printareport(donorDict)
        if (userinput == str(3)):
            break


