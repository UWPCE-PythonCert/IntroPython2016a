# Create a dictionary containing “name”, “city”, and “cake”
# for “Chris” from “Seattle” who likes “Chocolate”.
stuff = {'name': "Chris", 'city': "Seattle", 'cake': "Chocolate"}

# Display the dictionary.
print(stuff)

# Delete the entry for “cake”.
stuff.pop('cake')

# Display the dictionary.
print(stuff)

# Add an entry for “fruit” with “Mango” and display the dictionary.
stuff.update({'fruit': "Mango"})

print(stuff)

# Display the dictionary keys.
print(stuff.keys())


# Display the dictionary values.
print(stuff.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("True" if 'cake' in stuff else "False")

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("True" if "Mango" in stuff.values() else "False")

# Using the dictionary from item 1:
# Make a dictionary using same keys but with the number of ‘t’s in each value.
stuff = {'name': "Chris".count("t"), 'city': "Seattle".count("t"), 'cake': "Chocolate".count("t")}
print(stuff)

# Create sets s2, s3 and s4 containing numbers from 0-20, divisible 2, 3 and 4.
s2 = set([x for x in range(0, 20) if x % 2 == 0])
s3 = set([x for x in range(0, 20) if x % 3 == 0])
s4 = set([x for x in range(0, 20) if x % 4 == 0])

# Display the sets.
print(s2)
print(s3)
print(s4)

# Display if s3 is a subset of s2 (False)
if s3.issubset(s2):
    print(True)
else:
    print(False)

# and if s4 is a subset of s2 (True).
if s4.issubset(s2):
    print(True)
else:
    print(False)

# Create a set with the letters in ‘Python’
python = set(["p", "y", "t", "h", "o", "n"])

#add ‘i’ to the set.
python.update(["i"])
print(python)

# Create a frozenset with the letters in ‘marathon’
marathon = frozenset(["m", "a", "r", "a", "t", "h", "o", "n"])
print(marathon)

# display the union and intersection of the two sets.
print(marathon.union(python))
print(marathon.intersection(python))