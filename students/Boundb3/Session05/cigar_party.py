#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.
Return True if the party with the given values is successful,
or False otherwise.
"""

# b3 -  ok - written this function to pass the tests.
# run (from the command line) the command "py.test" in the directory that the file and test file reside in
# this will print out the results in the command line window when you have an error - and then you can return to the code to fix / de-bug the program

print ("this is a test")
def cigar_party(cigars, is_weekend):
    print(cigars, "and ", is_weekend, "made it to the def cigar_party function")
    if 40 <= cigars <= 60 and is_weekend == False: #b3 - I had these in "quotes" like "False" and the assert tests failed, so I was able to know to keep working at it to fix it.  Note to self: Assert testing works to find errors!!
        return True
    elif cigars >= 40 and is_weekend == True: #b3 - I had mistakenly put quotes here too
        return True
    else:
        return False

'''
cigar = 40
is_weekend = False

x = cigar_party(cigar, is_weekend)
print(x)
'''