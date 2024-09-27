#
# Trapazoid rule project: uses f(x) = x**2 as a function to be passed to the trapz function

import random
import string
import sys

# The function that will be passed to trapz
def f(x):
    # f(x) = x**2 is used as an equation
    y = x ** 2
    return y

def trapz(func, start, end):
	#Compute the area under the curve defined by
	#y = fun(x), for x between a and b

	N = 100 #max
	x = 0
	first = 0
	for x in range(0, N):
		if first ==0:
			first = 1
			summ = f(x)
			#print('summ at 0....',summ)
			#print('x at 0....',x)
		else:
			#print('x at N0....',x)
			summ = summ + (2*f(x))
			#print('x at N0....',x)
		#f = f + x
		#print('summ...',summ)
	area = (((end-start))/2*N)*summ

	return area

area = trapz(f, 5, 10)
print("The area under the curve from {} to {} is {}: ".format(5,10,area),'\n')


