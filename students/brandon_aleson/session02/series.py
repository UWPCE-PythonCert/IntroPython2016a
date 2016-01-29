# Brandon Aleson
# Intro to Python
# 1/27/16
# series


def fibonacci(n):
    """ This function returns the nth value in the fibonacci series """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """ This function returns the nth value in the lucas series """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, i=0, j=1):
    """
    Calling this function with no optional parameters will print numbers from the fibonacci series.
    Calling it with the optional parameters 2 and 1 will print values from the lucas series.
    Other values for the optional parameters will print other series.
    """
    if n == 0:
        return i
    elif n == 1:
        return j
    else:
        return sum_series(n - 1) + sum_series(n - 2)


# these assert statements test the preceding functions
assert fibonacci(10) == 55
assert lucas(10) == 123
assert sum_series(10) == 55
assert sum_series(10, 2, 1) == 123
