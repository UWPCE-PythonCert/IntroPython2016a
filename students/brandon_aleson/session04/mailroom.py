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
        return False
    elif choice == 's':
        sendThanks()
        return True
    elif choice == 'c':
        createReport()
        return True


def printDonors():
    print('Here are the current donors:')
    for d in donors:
        print(d)
    return ""


def donorInput():
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
    return (name, amount)


def sendEmail(name, amount):
    print('What a nice person!')
    print('Let\'s send them this heartfelt email:')
    print('Dear {}:\nThank you for your donation of ${}.\nYou\'re great!'.format(name, amount))


def sendThanks():
    print('Let\'s send some thanks!')
    name, amount = donorInput()
    sendEmail(name, amount)


def statSorter(sorter):
    return sorter[3]


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


def printReport(statList):
    print('{:-^80}'.format('DONOR REPORT'))
    print('{:<20}{:<20}{:<20}{:<20}'.format('DONOR NAME', '# OF DONATIONS', 'AVERAGE AMOUNT', 'TOTAL DONATED'))
    for item in statList:
        print('{:<20}{:<20}{:<20}{:,}'.format(item[0], item[1], item[2], item[3]))
    print('{:-^80}'.format('--'))


def createReport():
    print('crunching the numbers...')
    input()
    statList = computeSortedStats()
    printReport(statList)


if __name__ == '__main__':
    initializeDict()
    loop = True

    print('Welcome to the mailroom!')

    while loop:
        choice = choose()
        loop = redirect(choice)

    print('I\'ll be here when you need me')
