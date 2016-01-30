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
    action = input('(type \'s\' to send a thank you message, \'c\' to create a report, or \'q\' to quit)\n')
    while (action != 's' and action != 'c' and action != 'q'):
        action = input('I\'m not doing anything until you give me one of those three letters\n')
    if action == 's':
        return(action)
    elif action == 'c':
        return(action)
    elif action == 'q':
        return False


def sendThanks():
    print('sending thanks')


def createReport():
    print('creating report')


def redirect(choice):
    if not choice:
        print('I\'ll be here when you need me')
    elif choice == 's':
        sendThanks()
    elif choice == 'c':
        createReport()


if __name__ == '__main__':
    initializeDict()

    print('Welcome to the mailroom!')
    print('What would you like to do?')

    choice = choose()
    redirect(choice)
