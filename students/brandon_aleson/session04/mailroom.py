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


if __name__ == '__main__':
    initializeDict()
    print(donors)
