#!/usr/bin/env python3

# Add the file to your clone of the repository and commit changes frequently while working on the following tasks.
#  When you are done, push your changes to GitHub and issue a pull request.
#
# (if you are struggling with git – just write the code for now)
#
# When the script is run, it should accomplish the following four series of actions:
#
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.

aDict = { "name": 'Chris', 'city': "Seattle", 'cake': 'Chocolate'}


# Display the dictionary.

print(aDict)

# Delete the entry for “cake”.

del aDict['cake']

# Display the dictionary.

print(aDict)

# Add an entry for “fruit” with “Mango” and display the dictionary.

aDict['fruit'] = 'Mango'

# Display the dictionary keys.

print(aDict.keys())

# Display the dictionary values.

print(aDict.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).

print('cake' in aDict)

# Display whether or not “Mango” is a value in the dictionary (i.e. True).

print('Mango' in aDict.values())


# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.

aDict2 = {}
for k in aDict:
    aDict2[k] = aDict[k].count('t')
print(aDict2)

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

s2 = set([i for i in range(21) if i % 2 == 0])
s3 = set([i for i in range(21) if i % 3 == 0])
s4 = set([i for i in range(21) if i % 4 == 0])


# Display the sets.

print(s2)
print(s3)
print(s4)

# Display if s3 ise a subset of s2 (False)

if s3.issubset(s2): print('s3 is a subset of s2', s2)


# and if s4 is a subset of s2 (True).

if s4.issubset(s2): print('s4 is a subset of s2', s4)

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.

p = set('Python')
p.add('i')
print(p)

# Create a frozenset with the letters in ‘marathon’

f = frozenset('marathon')

# display the union and intersection of the two sets.
#

print(p.union(f))
print(p.intersection(f))

if __name__ == '__main__':
    pass

