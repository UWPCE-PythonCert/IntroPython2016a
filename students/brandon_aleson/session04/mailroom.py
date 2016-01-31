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


# control flow handler
def choose():
    print('What would you like to do?')
    action = input('(type \'s\' to send a thank you message, \'c\' to create a report, or \'q\' to quit)\n')
    while (action != 's' and action != 'c' and action != 'q'):
        action = input('I\'m not doing anything until you give me one of those three letters\n')
    if action == 's':
        sendThanks()
        return True
    elif action == 'c':
        createReport()
        return True
    elif action == 'q':
        return False


# main function for sending thank you email
def sendThanks():
    input('Let\'s send some thanks!\n')
    name, amount = donorInput()
    sendEmail(name, amount)
    input()


# receive input on which donor to thank
# if donor doesn't exist, add to the dictionary
def donorInput():
    name = input('Give me a full name, or type \'l\' to list the current donors on file\n')
    while name == 'l':
        printDonors()
        name = input('Choose one of the above, or give me a new name\n')
    donors.setdefault(name, [])
    while True:
        try:
            amount = input('How much did they give?\n')
            amount = int(amount)
            print()
            break
        except ValueError:
            print('That\'s not nice, you almost broke me')
            print('Donations are usually positive integers')
    donors[name].append(amount)
    return (name, amount)


# print current list of donors
def printDonors():
    print('Here are the current donors:')
    for d in donors:
        print(d)
    return ""


# send formatted thank you email
def sendEmail(name, amount):
    print('What a nice person!')
    input('Let\'s send them this heartfelt email:\n')
    print('Dear {},\nThank you for your donation of ${:,}.\nYou\'re great!'.format(name, amount))


# sorting key function for return value of computeSortedStats()
def statSorter(sorter):
    return sorter[3]


# compile relevant donor statistcs into a sorted list for printReport()
def computeSortedStats():
    stats = []
    for d, a in donors.items():
        stats.append([d, a])
    for item in stats:
        item.append(len(item[1]))
        item.append(int((sum(item[1]))/(len(item[1]))))
        item.append(sum(item[1]))
        del item[1]
    return sorted(stats, key=statSorter)


# print formatted donor report
def printReport(statList):
    print('{:-^80}'.format('DONOR REPORT'))
    print('{:<20}{:<20}{:<20}{:<20}'.format('DONOR NAME', '# OF DONATIONS', 'AVERAGE AMOUNT', 'TOTAL DONATED'))
    for item in statList:
        print('{:<20}{:<20}${:<20}${:,}'.format(item[0], item[1], item[2], item[3]))
    print('{:-^80}'.format('--'))


# main function for creating donor report
def createReport():
    input('crunching the numbers...\n')
    statList = computeSortedStats()
    printReport(statList)
    input()


if __name__ == '__main__':
    initializeDict()
    loop = True

    input('Welcome to the mailroom!\n')

    while loop:
        loop = choose()

    print('I\'ll be here when you need me')
