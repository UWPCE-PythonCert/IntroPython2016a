
feast = ["lambs", "sloths", "orangutans", "breakfast cereals", "fruit bats"]

compression = [delicacy.capitalize() for delicacy in feast]

print(compression[0])

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

print (comp)

print("length of feast: ", len(feast))
print("length of comp: ", len(comp))


list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

new_comprehension = [ skit * number for number, skit in list_of_tuples ]

print(new_comprehension)

