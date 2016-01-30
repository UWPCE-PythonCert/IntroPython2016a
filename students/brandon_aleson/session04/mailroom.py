#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# Brandon Aleson
# Intro to Python
# 1/29/16
# mailroom


donorList = ['Brandon Aleson', 'Paulina Ploszajska', 'Jesse Montini-Vose', 'Mary Montini', 'Shirley Aleson']
amountList = [[120000], [4000], [500, 300, 800], [1467, 1467], [8, 5, 25]]
donors = {}


def initializeDict():
    for i, j in zip(donorList, amountList):
        donors[i] = j
    return donors


def choose():
    print('What would you like to do?')
    action = input('(type \'s\' to send a thank you message, \'c\' to create a report, or \'q\' to quit)\n')
    while (action != 's' and action != 'c' and action != 'q'):
        action = input('I\'m not doing anything until you give me one of those three letters\n')
    if action == 's':
        return(action)
    elif action == 'c':
        return(action)
    elif action == 'q':
        return False


def redirect(choice):
    if not choice:
        print('I\'ll be here when you need me')
    elif choice == 's':
        sendThanks()
    elif choice == 'c':
        createReport()


def printDonors():
    print('Here are the current donors:')
    for d in donors:
        print(d)
    return ""


def sendThanks():
    print('Let\'s send some thanks!')
    name = input('Give me a full name, or type \'l\' to list the current donors on file\n')
    while name == 'l':
        name = input(printDonors())
    donors.setdefault(name, [])
    while True:
        try:
            amount = input('How much did they give?\n')
            amount = int(amount)
            break
        except ValueError:
            print('That\'s not nice, you almost broke me\nDonations are usually positive integers')
    donors[name].append(amount)
    print(donors)


def createReport():
    print('creating report')





if __name__ == '__main__':
    initializeDict()

    print('Welcome to the mailroom!')

    choice = choose()
    redirect(choice)
