def fibonacci (n):
    '''Calculates the Fibanocci sequence given a certain value, n
	Parameters
	==========
	n : Int
	    The starting value of the sequence.

	Results
	=========
	returns value of the Fibonacci sequence'''
    if(n == 0): return 0
    if(n == 1): return 1
    else: return (fibonacci(n-2) + fibonacci(n-1))


def lucas (n):
	'''Calculates the Lucas sequence given a certain value, n
	Parameters
	==========
	n : Int
	    The starting value of the sequence.

	Results
	=========
	returns the nth value of the lucas series'''
	n = n -1
	if(n == 0): return 2
	if(n == 1): return 1
	else: return (lucas(n-2) + lucas(n-1))


