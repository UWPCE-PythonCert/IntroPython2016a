# add a function called fibonacci.
# The function should have one parameter n.
# The function should return the nth value in the fibonacci series.
# Ensure that your function has a well-formed docstring

# Add a series of statements proving functions work
# Add comments about what tests are doing
# push your changes to GitHub and make a pull request


def fib(n):
    """Iterate next number in Fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def lucas(n):
    """Iterate next number in Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """Run Fibonacci or Lucas function depending on optional parameters"""
    if a == 0 and b == 1:
        return fib(n)
    elif a == 2 and b == 1:
        return lucas(n)
    else:
        return None

# test fib function
print(fib(5))
# test lucas function
print(lucas(5))
# test sum_series function running fib function
print(sum_series(5))
# test sum_series function running lucas function
print(sum_series(5, 2, 1))
