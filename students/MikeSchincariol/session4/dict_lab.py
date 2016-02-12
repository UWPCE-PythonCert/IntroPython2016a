#!/usr/bin/python3

# Create a dictionary containing “name”, “city”, and “cake” for “Chris”
# from “Seattle” who likes “Chocolate”.
d = {"name": "Chris",
     "city": "Seattle",
     "cake": "Chocolate"}


# Display the dictionary
print(d)


# Delete the entry for “cake”.
del d['cake']


# Display the dictionary
print(d)


# Add an entry for “fruit” with “Mango” and display the dictionary.
d['fruit'] = "Mango"
#     Display the dictionary keys.
print("")
for key in d.keys(): print(key)
print("")
#     Display the dictionary values.
print("")
for val in d.values(): print(val)
print("")
#     Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
if "cake" in list(d.keys()):
    print("True")
else:
    print("False")
#     Display whether or not “Mango” is a value in the dictionary (i.e. True).
if "Mango" in list(d.values()):
    print("True")
else:
    print("False")

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
d = {"name": "Christ".count('t'),
     "city": "Seattle".count('t'),
     "cake": "Chocolate".count('t')}


# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s2 = set([x for x in range(0, 21) if x % 2 == 0])
s3 = set([x for x in range(0, 21) if x % 3 == 0])
s4 = set([x for x in range(0, 21) if x % 4 == 0])

# Display the sets.
print("Numbers divisible by 2: {0}".format(s2))
print("Numbers divisible by 3: {0}".format(s3))
print("Numbers divisible by 4: {0}".format(s4))


# Display if s3 is a subset of s2 (False)
s3.issubset(s2)

#  and if s4 is a subset of s2 (True).
s4.issubset(s2)

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s5 = set("Python")
s5.add("i")


# Create a frozenset with the letters in ‘marathon’
f1 = frozenset("marathon")

# Display the union and intersection of the two sets.
s5.union(f1)
s5.intersection(f1)
