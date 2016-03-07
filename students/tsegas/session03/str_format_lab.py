# String format lab execises from session-03
# produce 'file_002 :   123.46, 1e+04'

import random
import string
import sys
import os
import math

#passnum function to pass the 3 numbers
def passnum(x,y,z):
	print("The first 3 numbers are: {:d}, {:d}, {:d}".format(x,y,z))
	n = ('{:d}{:d}{:d}'.format(x,y,z))
	return n

#call the function
n=passnum(x=7,y=8,z=9)

# Convert the returned value to an integer
n = int(n)
f1 = '{:.4f}'.format(.4567).lstrip('0')

# Convert to float
f = float(f1)

m = ('{:d}{:.4f}'.format(n,f).lstrip('0'))

# Convert to float
m = float(m)
# This was the only way for now I could get rid of the leading zero
m = (m/10)+0.41103

strg = (2,m,10000)
print("Change this............",strg)

a = ('{:d}'.format(strg[0]))
b = ('{:05.2f}'.format(strg[1]))
# Format the last value as an exponent
c = ('{:01.0e}'.format(strg[2]))

print("To this................ file_00{} :   {},".format(a,b),c,'\n')

