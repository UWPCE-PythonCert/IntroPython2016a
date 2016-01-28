#!/usr/bin/env python3

def fib(n):
    """ Return nth fibonacci number - iteratively
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibonacci(n):
    """ Returns nth fibonacci number - recursively 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """ Returns nth lucas number
    """
    a, b = 2, 1
    for i in range(n):
        a, b = b, a + b
    return a

def series_sum(n, first=0, second=1):
    """ Returns nth series sum given first and second series elements
    """
    a, b = first, second
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3

    assert series_sum(0) == 0
    assert series_sum(1) == 1
    assert series_sum(2) == 1
    assert series_sum(3) == 2
    assert series_sum(4) == 3

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7

    assert series_sum(0, 2, 1) == 2
    assert series_sum(1, 2, 1) == 1
    assert series_sum(2, 2, 1) == 3
    assert series_sum(3, 2, 1) == 4
    assert series_sum(4, 2, 1) == 7


    n = int(input('Enter n: '))
    print("Fibonacci(", n, ") = ",  fibonacci(n))
    print("Fibonacci(", n, ") = ",  series_sum(n, 0, 1))
    print("Lucas(", n, ") = ",      lucas(n))
    print("Lucas(", n, ") = ",      series_sum(n, 2, 1))




