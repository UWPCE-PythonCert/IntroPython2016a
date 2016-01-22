def fibonacci (n):
    '''Calculates the Fibanocci sequence given the length of the series, n
	Parameters
	==========
	n : Int
	    The length of the the sequence

	Results
	=========
	returns nth value of the Fibonacci series'''
    if(n == 0): return 0
    if(n == 1): return 1
    else: return (fibonacci(n-2) + fibonacci(n-1))


def lucas (n):
	'''Calculates the Lucas sequence given the length of the series, n
	Parameters
	==========
	n : Int
	    The length of the the sequence

	Results
	=========
	returns the nth value of the Lucas series'''
	if(n == 0): return 2
	if(n == 1): return 1
	else: return (lucas(n-2) + lucas(n-1))


def sum_series (n, startval = 0, secondval=1):
	'''Calculates the a series given the length of the series, n
	Parameters
	==========
	n : Int
	    The length of the the sequence
	startval : Int
		The first value in the sequence
	secondval : Int
		The second value in the sequence

	Results
	=========
	returns the nth value of the series'''
	if(n == 0): return startval
	if(n == 1): return secondval
	else: return (sum_series(n-2, startval = startval, secondval = secondval) + sum_series(n-1,startval = startval, secondval = secondval))

assert fibonacci(6) == 8
assert lucas(6) == 18
assert sum_series(6, startval=0, secondval=1) == 8
assert sum_series(6, startval=2, secondval=1) == 18
