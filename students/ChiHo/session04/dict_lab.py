# Dictionary and Key Lab
# Student: Chi Kin Ho
# Date: Thursday, January 28, 2016

# Create a dictionary containing "name", "city", and "cake" for "Chris" from "Seattle" who likes "Chocolate".
dictionary = dict()
dictionary['cake'] = ['name', 'city']
dictionary['Chocolate'] = ['Chris', 'Seattle']
# Display the dictionary.
print(dictionary)

# Delete the entry for "cake".
dictionary.pop('cake')
# Display the dictionary.
print(dictionary)

# Add an entry for "fruit" with "Mango" and display the dictionary.
dictionary['Mango'] = ['David', 'Toronto']

# Display the dictionary keys.
for key in dictionary.keys():
    print(key)
# Display the dictionary values.
for value in dictionary.values():
    print(value)

# Display whether or not "cake" is a key in the dictionary (i.e., False) (now).
print('cake' in dictionary)
# Display whether or nto "Mango" is a value in the dictionary (i.e., True).
print('Mango' in dictionary)

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 't's in each value.
dictionary2 = dict()

def find_the_number_of_t(v):
    """
       This function takes an input string argument and returns the number of t's in this string argument.

       :param v: the input string argument
       :return: the number of t's in this string argument
    """
    number_of_ts = 0
    for letter in v:
        if letter == 't' or letter == 'T':
            number_of_ts += 1
    return number_of_ts

for key in dictionary:
    dictionary2[key] = [find_the_number_of_t(dictionary[key][0]), find_the_number_of_t(dictionary[key][1])]

# Display the two dictionaries.
print(dictionary)
print(dictionary2)

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s2 = set()
s3 = set()
s4 = set()
for number in range(0, 21):
    if number % 2 == 0:
        # Add the number that is divisible by 2 to s2.
        s2.add(number)
    if number % 3 == 0:
        # Add the number that is divisible by 3 to s3.
        s3.add(number)
    if number % 4 == 0:
        # Add the number that is divisible by 4 to s4.
        s4.add(number)

# Display the sets.
print(s2) # set 2
print(s3) # set 3
print(s4) # set 4

# Display if s3 is a subset of s2 (False).
print(s3.issubset(s2))
# Display if s4 is a subset of s2 (True).
print(s4.issubset(s2))

# Create a set with letters in 'Python' and add 'i' to the set.
python_set = set()
for letter in 'Python':
    python_set.add(letter)
python_set.add('i')

# Display the set.
print(python_set)

# Create a frozenset with the letters in 'marathon'.
frozenset = set()
for letter in 'marathon':
    frozenset.add(letter)

# Display the set.
print(frozenset)

# Display the union and intersection of the two sets.
print(python_set.union(frozenset))
print(python_set.intersection(frozenset))







