'''

Notes in Prep for doing this assignment:
You can do that in a for loop, also:

In [4]: l = [(1, 2), (3, 4), (5, 6)]

In [5]: for i, j in l:
            print("i:%i, j:%i"%(i, j))

i:1, j:2
i:3, j:4
i:5, j:6



'''
Looping through two loops at once:
zip

In [10]: l1 = [1, 2, 3]

In [11]: l2 = [3, 4, 5]

In [12]: for i, j in zip(l1, l2):
   ....:     print("i:%i, j:%i"%(i, j))
   ....:
i:1, j:3
i:2, j:4
i:3, j:5
Can be more than two:

for i, j, k, l in zip(l1, l2, l3, l4):

   FUTURE week 5 stuff:

    update mailroom from last week to:
Use dicts where appropriate
Write a full set of letters to everyone to individual files on disk
See if you can use a dict to switch between the users selections
Try to use a dict and the .format() method to do the letter as one big template – rather than building up a big string in parts.

'''
TO DO:
also need to set in command window the ability to read this directly

"""