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


    # Again, using the list from series 1:
    #
    # Ask the user for input displaying a line like “Do you like apples?”
    # for each fruit in the list (making the fruit all lowercase).

    for item in fruit[:]:
        done = False
        while not done:
            prompt = 'Do you like ' + item.lower() + '?  Yes or no? '
            response = input(prompt)

            # For each “no”, delete that fruit from the list.
            if 'no' in response.lower():
                fruit.remove(item)
                done = True
            if 'yes' in response.lower():
                done = True
    # Display the list.
    print(fruit)


    # Once more, using the list from series 1:
    #
    # Make a copy of the list and reverse the letters in each fruit in the copy.

    fruit_reversed = []
    for item in fruit[:]:
        item_reversed = item[::-1]
        fruit_reversed.append(item_reversed)


    # Delete the last item of the original list. Display the original list and the copy.
    fruit.pop()
    print(fruit)
    print(fruit_reversed)
