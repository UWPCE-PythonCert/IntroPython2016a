feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
print(comprehension[0])
print(comprehension[2])

comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print(len(feast))
print(len(comp))

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [skit * number for number, skit in list_of_tuples]
print(comprehension[0])
print(len(comprehension[2]))

eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print(len(comprehension))
print(comprehension[0])

comprehension = {x for x in 'aabbbcccc'}
print(comprehension)

dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third':'ruthless efficiency', 'forth':'fanatical devotion', 'fifth': None}
dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print(len(dict_of_weapons))
print(len(dict_comprehension))

#count_evens([2, 1, 2, 3, 4]) == 3
#count_evens([2, 2, 0]) == 3
#count_evens([1, 3, 5]) == 0

#def count_evens(nums):
#   one_line_comprehension_here
