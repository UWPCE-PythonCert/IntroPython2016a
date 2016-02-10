#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# Brandon Aleson
# Intro to Python
# 1/27/16
# list lab


# 1st section
fruit = ['apples', 'pears', 'oranges', 'peaches']
print(fruit)

fruit.append(input("What is another fruit that you like?\n"))
print(fruit)

fruitIndex = int(input("Pick a number between 1 and 5\n"))
print('You picked', end=" ")
print(fruit[(fruitIndex-1)])

fruit = ['cherries'] + fruit
print(fruit)

fruit.insert(0, 'blueberries')
print(fruit)

for fruits in fruit:
    if fruits[0] == 'p':
        print(fruits)


# 2nd section
fruity = fruit[:]
print(fruity)

del fruity[-1]
print(fruity)

fruity.remove(input("What is your least favorite fruit from the list above?\n"))
print('It\'s gone! ', end="")
print(fruity)


# 3rd section
fruities = fruit[:]
for fruitiez in fruities[:]:
    preference = input("Do you like {}?\n".format(fruitiez))
    while (preference != 'yes' and preference != 'no'):
        preference = input("It's a simple yes or no question\n")
    if preference == 'no':
        fruities.remove(fruitiez)
        print("removing {} from your list of fruits your majesty".format(fruitiez))

if fruities:
    print('so you like these fruits: ')
    print(fruities)
else:
    print('you must not like fruit very much')


# 4th section
fruitz = fruit[:]
fruitzCopy = []
for sweetThing in fruitz[:]:
    sweetThing = sweetThing[::-1]
    fruitzCopy.append(sweetThing)
del fruitz[-1]
print(fruitz)
print(fruitzCopy)
