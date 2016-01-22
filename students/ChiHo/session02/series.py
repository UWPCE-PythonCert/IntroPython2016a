# Week 2 - Lab #4: Series
# Date: Monday, January 18, 2016
# Student: Chi Kin Ho


def sum_series(n, *starting_values):

    """
        This function takes one required parameter, n, and two optional
        parameters, *starting_values. The required parameter will determine
        which element in the series to print. The two optional parameters
        will have default values of 0 and 1 and will determine the first two
        values for the series to be produced.

        Calling this function with no optional parameters will produce numbers
        from the fibonacci series. Calling it with the optional arguments 2 and 1
        will produce values from the lucas numbers. Other values for the optional
        parameters will produce other series.

        :param n: the term number, which starts from 0, 1, 2, ...
        :param starting_values: the first and second optional starting values of the series
        :return: the nth term of the sum sequence
    """

    if len(starting_values) == 0: # fibonacci sequence
        return fibonacci(n)
    elif len(starting_values) == 2:
        if starting_values[0] == 2 and starting_values[1] == 1: # lucas sequence
            return lucas(n)
        else: # other series
            if n == 0 or n == 1:
                return starting_values[n]
            else:
                return sum_series(n-2, *starting_values) + sum_series(n-1, *starting_values)
    else:
        return None # Invalid number of starting_values


def fibonacci(n):

    """
        This function calculates and returns the nth term of the Fibonacci sequence

        :param n: the term number, which starts from 0, 1, 2, ...
        :return: the nth term of the Fibonacci sequence
    """

    if n == 0 or n == 1: # base cases: when n == 0 or n == 1
        return n
    else: # recursive step
        return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):

    """
        This function calculates and returns the nth term of the Lucas sequence

        :param n: the term number, which starts from 0, 1, 2, ...
        :return: the nth term of the Lucas sequence
    """

    if n == 0: # base case: when n == 0
        return 2
    elif n == 1: # base case: when n == 1
        return 1
    else: # recursive step
        return lucas(n-2) + lucas(n-1)


# Test Case 1: the 8th term of the Fibonacci sequence
f_series = ''
for i in range(8):
    f_series += str(sum_series(i))
    if (i < 7):
        f_series += ', '
print(f_series)

# Test Case 2: the 8th term of the Lucas sequence
l_series = ''
for i in range(8):
    l_series += str(sum_series(i, 2, 1))
    if (i < 7):
        l_series += ', '
print(l_series)

# Test Case  3: the 8th term of the sum series with the starting values of 5 and 10
other_series = ''
for i in range(8):
    other_series += str(sum_series(i, 5, 10))
    if (i < 7):
        other_series += ', '
print(other_series)

# Test Case 4: Invalid number of starting values
print(sum_series(3, 4))
print(sum_series(3, 4, 5, 6))