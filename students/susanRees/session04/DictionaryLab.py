# Create a dictionary containing “name”, “city”, and “cake”
# for “Chris” from “Seattle” who likes “Chocolate”.
dict = {'name': "Chris", 'city': "Seattle", 'cake': "Chocolate"}

# Display the dictionary.
print(dict)

# Delete the entry for “cake”.
dict.pop('cake')

# Display the dictionary.
print(dict)

# Add an entry for “fruit” with “Mango” and display the dictionary.
dict.update({'fruit': "Mango"})

print(dict)

# Display the dictionary keys.
print(dict.keys())


# Display the dictionary values.
print(dict.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("True" if 'cake' in dict else "False")

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("True" if "Mango" in dict.values() else "False")

# Using the dictionary from item 1:
# Make a dictionary using same keys but with the number of ‘t’s in each value.
# Not sure I understand the assingment...

# Create sets s2, s3 and s4 containing numbers from 0-20, divisible 2, 3 and 4.
s2 = set([1:20])
s3 = set([1:20])
s4 = set([1:20])

# Display the sets.

# Display if s3 is a subset of s2 (False)

# and if s4 is a subset of s2 (True).

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.

# Create a frozenset with the letters in ‘marathon’

# display the union and intersection of the two sets.