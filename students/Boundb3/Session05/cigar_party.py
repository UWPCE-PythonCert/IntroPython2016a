#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.
Return True if the party with the given values is successful,
or False otherwise.
"""

print ("this is a test")
def cigar_party(cigars, is_weekend):
    print(cigars,is_weekend, "made it to the def cigar_party function")
    return (cigars*2)



cigar = 40
is_weekend = False

x = cigar_party(cigar, is_weekend)
print(x)
