
'''

Brennen Bounds
Python 100a

Create a new module series.py in the session02 folder in your student folder.
In it, add a function called "fibonacci".

The function should have one parameter n.
The function should return the nth value in the fibonacci series.

add a new function "lucas" that returns the nth value in the lucas numbers series.

then add a third function called sum_series with one required parameter and two optional parameters.
The required parameter will determine which element in the series to print.
The two optional parameters will have default values of 0 and 1 and will determine
the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series.
Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
Other values for the optional parameters will produce other series.

Ensure that your function has a well-formed docstring

'''

def fibinacci_n(n):
    """Return the nth value in a fibinacci series."""
    a,b =0,1
    #print (a)
    for i in range(n-1):
        a,b = b, a+b
        #print (a)
    return a


def lucas_n(n):
    """Return the nth value in a Lucas series."""
    a,b =2,1
    #print (a)
    for i in range(n-1):
        a,b = b, a+b
        #print (a)
    return a


def sum_series(n, startnum1=0,startnum2=1):
    """Return the nth value in a additive summation series given the two starting numbers.
    The default series is the fibinacci series."""
    startnum1, startnum2 = startnum1, startnum2
    #print (a)
    for i in range(n-1):
        startnum1,startnum2 = startnum2, startnum1+startnum2
        #print (a)
    return startnum1


n = int(input("Type in the number of the nth value in the sequence you want."))
assert (n>0), "Need to have a positve number for the nth value."

startnum1 = int(input("Type in the starting number."))
startnum2 = int(input("Type in the second starting number."))
assert (startnum1 > 0 or startnum2 > 0), "Both starting numbers cannont have zero values."

print("\n",fibinacci_n.__doc__, ":")
print ("\tThe", n, "'th number in the fibinacci sequence is: ", fibinacci_n(n))
print("\n",lucas_n.__doc__, ":")
print ("\tThe", n, "'th number in the lucas sequence is: ",lucas_n(n))
print("\n",sum_series.__doc__)
print ("\tThe", n, "'th number in a made up series is:",sum_series(n,startnum1,startnum2), "(for starting numbers:)",startnum1,startnum2)

