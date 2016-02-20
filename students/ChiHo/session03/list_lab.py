# List Lab
# Student: Chi Kin Ho
# Date: Sunday, January 24, 2016

# When the script is run, it should accomplish the following four series of actions:

# ---------------------------------------------------------------------------------------------------------------------
# Series 1
# ---------------------------------------------------------------------------------------------------------------------

# Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list.
print(fruit_list)

# Ask the user for another fruit and add it to the end of the list.
fruit = input("Enter another fruit: ")
fruit_list.append(fruit)

# Display the list.
print(fruit_list)

# Ask the user for a number and display the number back to theuser and the fruit corresponding to that number
# (on a 1-is-first basis).
number = input("Enter a number: ")
print(number)
number = int(number)
if 1 <= number <= len(fruit_list):
    print(fruit_list[number-1])
else:
    print("Error: number must be between 1 and", len(fruit_list))

# Add another fruit to the beginning of the list using "+" and display the list.
new_fruit_list = ''
if len(fruit_list) > 0:
    # Convert the fruit list into string so that I can use the "+" operator to add a new fruit,
    for i in range(len(fruit_list)):
        if i == 0:
            new_fruit_list = fruit_list[i]
        else:
            new_fruit_list += ', ' + fruit_list[i]

fruit_list = new_fruit_list
fruit_list = "Mangoes, " + new_fruit_list
# Convert the string back to the list.
fruit_list = fruit_list.split(', ')
print(fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list.
fruit_list.insert(0, 'Pineapples')
print(fruit_list)

# Display all the fruits that begin with "P" using a for-loop.
all_fruits_begin_with_P = list()
for fruit in fruit_list:
    if fruit.startswith('P'):
        all_fruits_begin_with_P.append(fruit)
print(all_fruits_begin_with_P)


# ---------------------------------------------------------------------------------------------------------------------
# Series 2
# ---------------------------------------------------------------------------------------------------------------------

# Using the list created in series 1 above:

# Display the list.
fruit_list_2 = fruit_list[:]
print(fruit_list_2)

# Remove the last fruit from the list.
fruit_list_2.pop()

# Display the list.
print(fruit_list_2)

# Ask the user for a fruit to delete and find it and delete it.
fruit = input('Enter a fruit to delete: ')
if fruit in fruit_list_2:
   fruit_list_2.remove(fruit)
print(fruit_list_2)

# Bonus: Multiply the list times two.  Keep asking until a match is found.  Once found, delete all occurrences.
fruit_list_2 *= 2
print(fruit_list_2)
# Repeatedly ask the user for a fruit until a match is found.
fruit = ''
is_match_found = False
while not is_match_found:
    fruit = input('Enter a fruit to delete: ')
    is_match_found = fruit in fruit_list_2
# Delete all occurrences.
while fruit in fruit_list_2[:]:
    fruit_list_2.remove(fruit)
# Display the list.
print(fruit_list_2)


# ---------------------------------------------------------------------------------------------------------------------
# Series 3
# ---------------------------------------------------------------------------------------------------------------------

# Again, using the list from series 1:
fruit_list_3 = fruit_list[:]
print(fruit_list_3)

# Ask the user for input displaying a line like "Do you like apples?"

# For each fruit in the list (making all lowercase).
for i in range(len(fruit_list_3)):
    fruit_list_3[i] = fruit_list_3[i].lower()
print(fruit_list_3)

# Repeatedly ask the user whether or not he/she likes apples until he/she types 'yes' or 'no'.
is_done = False
while not is_done:
    response = input('Do you like apples? ')
    if response.lower() == 'no':
        if 'apples' in fruit_list_3:
            fruit_list_3.remove('apples')
        is_done = True
    elif response.lower() == 'yes':
        is_done = True

# Display the list.
print(fruit_list_3)


# ---------------------------------------------------------------------------------------------------------------------
# Series 4
# ---------------------------------------------------------------------------------------------------------------------

# Make a copy of the list and reverse the letters in each fruit in the copy.
fruit_list_4 = fruit_list[:]
print(fruit_list_4)

# Reverse the letters in each fruit in the copy.
for i in range(len(fruit_list_4)):
    fruit_list_4[i] = fruit_list_4[i][::-1]
# Display the list.
print(fruit_list_4)

# Delete the last item of the original list.
fruit_list.pop()
# Display the original list and the copy.
print(fruit_list)
print(fruit_list_4)