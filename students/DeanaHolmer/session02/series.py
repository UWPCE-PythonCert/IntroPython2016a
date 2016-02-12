# Deana Holmer
# UWPCE Python 2016 Winter
# "series.py" due 1/21/2016
# In this exercise we compute finbonacci series
import os
os.chdir('C:\\Documents\\Python\\python35src\\UWPython1\\week2')


def fibonacci(n):
    """Compute and return next number in fibonacci sequence."""
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def lucas(n):
    """Compute and return next number in lucas sequence."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n - 1) + lucas(n - 2))

def sum_series(n, a=0, b=1):
    """Decide on fibonacci lucas or other series and run it."""
    if a == 0 and b == 1:
        return fibonacci(n)
    elif a == 2 and b == 1:
        return lucas(n)
    else:
        return None

# test it
nterms = 10

print ("Test fibonacci")
for i in range(nterms):
    print(fibonacci(i))

print ("Test lucas")
for i in range(nterms):
    print(lucas(i))

print ("Test sum_series with defaults")
for i in range(nterms):
    print(sum_series(i))

print ("Test sum_series with lucas params")
for i in range(nterms):
    print(sum_series(i,2,1))

print ("Test sum_series with other params")
for i in range(nterms):
    print(sum_series(i,4,5))
