#!/usr/bin/env python3
#
# list_lab.py
#

if __name__ == '__main__':

    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

    # Display the list.
    print(fruit)

    # Ask the user for a number and display the number back to the user and the fruit corresponding to that number
    # (on a 1-is-first basis).
    index = int(input('Enter fruit list index:'))
    print(fruit[index - 1])

    # Add another fruit to the beginning of the list using “+” and display the list.
    fruit = ['Kiwi'] + fruit
    print(fruit)

    # Add another fruit to the beginning of the list using insert() and display the list.
    fruit.insert(0, 'Banana')
    print(fruit)

    # Display all the fruits that begin with “P”, using a for loop.
    for item in fruit:
        if 'P' in item: print(item)

    #
    # Using the list created in series 1 above:
    #
    # Display the list.
    # Remove the last fruit from the list.
    # Display the list.
    # Ask the user for a fruit to delete and find it and delete it.

    print(fruit)
    fruit.pop()
    print(fruit)
    item = input('Enter fruit to be deleted:')
    if item in fruit:
        fruit.remove(item)
    print(fruit)
