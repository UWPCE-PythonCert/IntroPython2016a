# Create a list with “Apples”, “Pears”, “Oranges” and “Peaches”
a = "Apples"
b = "Pears"
c = "Oranges"
d = "Peaches"
fruits = [a, b, c, d]

# Display the list.
print(fruits)

# ask the user for new fruit and add it to end of the list.
print("Please type in a type of fruit")
e = input()
fruits.append(e)

# Display the list.
print(fruits)

# Ask the user for a number
print("Please type in a type number")
num = input()

# display the number and that number's fruit (on a 1-is-first basis).
tada = fruits[int(num) - 1]
print(num, tada)

# Add fruit to the beginning of the list using “+”
fruits2 = ["kiwi"] + fruits

# display the list.
print(fruits2)

# Add fruit to the beginning of the list using insert()
fruits2.insert(0, "pineapple")

# display the list.
print(fruits2)

# Display all the fruits that begin with “P”, using a for loop.
p_fruits = []
for pfruit in fruits2:
    if pfruit[0] == "p" or pfruit[0] == "P":
        p_fruits.append(pfruit)
print(p_fruits)

# Display the list.
print(fruits2)

# Remove the last fruit from the list.
fruits2.pop(-1)

# Display the list.
print(fruits2)

# Ask the user for a fruit to delete
print(fruits2)
print("Please select a fruit from the list to delete.  Your typed response should be case sensitive and match the listed item exactly.")
rotten_fruit = input()

# find it and delete it.
shazaam = []
for find_it in fruits2:
    if find_it != rotten_fruit:
        shazaam.append(find_it)
print(shazaam)


# (Bonus: Multiply the list times two.
# Keep asking until a match is found.
# Once found, delete all occurrences.)


# Ask user for input "Do you like apples?”
# for each fruit in the list (making the fruit all lowercase).
likes = []
for opinions in fruits2:
    print("Do you like " + opinions + "?")
    yes_no = input()
    str.lower(yes_no)
    yes = "yes"
    no = "no"
# For any answer that is not “yes” or “no”, prompt user to answer yes or no
    if yes_no == yes:
        print("Thank you.")
        likes.append(opinions)
# For each “no”, delete that fruit from the list.
    elif yes_no == no:
        print("Okay.  We will take that one off the list.")
    while yes_no != yes or no:
        print("Please answer yes or no.")
        break
# Display the list.
print("Please see the fruits you like listed below.")
print(likes)


# Make a copy of the original list
backwards_fruits = fruits[0:-1]

# reverse the letters in each fruit in the copy.
# for bwards in backwards_fruits:

# print(backwards_fruits)

# Delete the last item of the original list.
# fruits.pop(-1)

# Display the original list and the copy.
# print(fruits)
# print(backwards_fruits)
