
def fibonacci(n):
	'''
	This function creates a fibonacci sequence and returns the last number in series based on input 'n'
	The sequnece generates a new number based on sum of previous 2 numbers in the sequence
	Sequence starts n = 1 return 0 and n = 2 return 1
	Sequence can populate recursively when n > 2	
	'''
	if n == 1:
		fib = 0
		return fib
	elif n == 2:
		fib = 1
		return fib
	else:
		fib = fibonacci(n-1) + fibonacci(n-2)
		return fib

def lucas(n):
	'''
	This function creates lucas numbers and returns the last number in series based on input 'n'
	The sequnece generates a new number based on sum of previous 2 numbers in the sequence
	Same logic as fibonacci but sequence starts n = 1 return 2 and n = 2 return 1
	Sequence can populate recursively when n > 2	
	'''
	if n == 1:
		luc = 2
		return luc
	elif n == 2:
		luc = 1
		return luc
	else:
		luc = lucas(n-1) + lucas(n-2)
		return luc

def sum_series(n, int1=0, int2=1):
	'''
	This function creates a recursive series similar to fibonacci and lucas functions
	Except it accepts optional input parameters that determin which 2 values are used to start sequence
	If optional parameters are left blank then fibonacci starting values are used	
	'''
	if n == 1:
		s = int1
		return s
	elif n == 2:
		s = int2
		return s
	else:
		s = sum_series(n-1, int1, int2) + sum_series(n-2, int1, int2)
		return s

print(fibonacci(8), lucas(8), sum_series(8,2,1))



