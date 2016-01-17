#!/usr/bin/env python3

def fibonacci(n):
    """Returns nth value in the Fibonacci sequence"""
    if type(n) is not int:
      return
    elif n < 2:
      return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Returns nth value in the Lucas sequence"""
    if type(n) is not int:
      return
    elif n == 0:
      return 2
    elif n == 1:
      return n
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, a=0, b=1):
    sum = 0
    if a == 0 and b == 1:
        for i in range(0,n+1):
            sum += fibonacci(i)
    elif a == 2 and b == 1:
        for i in range(0,n+1):
            sum += lucas(i)
    else:
        return
    return sum


# This compares the output of fibonacci() to known values
assert fibonacci(10) == 55
assert fibonacci(20) == 6765

# This compares the output of lucas() to known values
assert lucas(10) == 123
assert lucas(20) == 15127

# This tests sum_series() with Fibonacci numbers
assert sum_series(10) == 143
assert sum_series(20) == 17710

# This tests sum_series() with Lucas numbers
assert sum_series(10,2,1) == 321
assert sum_series(20,2,1) == 39602

