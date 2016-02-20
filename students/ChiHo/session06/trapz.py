# Week 6 - Lab #1: Trapezoidal Rule
# Date: Friday, February 12, 2016
# Student: Chi Kin Ho
import math


def trapezoidal_rule(function, x1, x2, *coefficients):
    """
    calculates the area of a trapezoidal between x = x1 and x = x2

    :param function: the height of the trapezoid represented by a function
    :param a: left-most x-coordinate at x = x1
    :param b: right-most x-coordinate at x = x2
    :param: coefficients: the list of coefficients of the function
    :return: the area of the trapezoid
    """
    return (x2 - x1) * (function(x1, *coefficients)+function(x2, *coefficients))/2


def line(x, m=1, B=0):
    """
    a very simple straight horizontal line at y = mx+B
    :param x: the x-coordinate
    :param m: the slope of the line
    :param B: the y-intercept of the line
    :return: the y-coordinate at the x-coordinate
    """
    return m*x + B


def quadratic(x, A=0, B=0, C=0):
    """
    Evaluates a quadratic equation at x
    :param x: the x-coordinate
    :param A: the A coefficient of the quadratic function
    :param B: the B coefficient of the quadratic function
    :param C: the C coefficient of the quadratic function
    :return: the y-coordinate of the quadratic function evaluated at x
    """
    return A * x**2 + B * x + C


def trapz(function, a, b, h, *coefficients):
    """
    Compute the area under the curve defined by
    y = function(x), for x between a and b

    :param function: the function to evaluate
    :param a: the start point for teh integration
    :param b: the end point for the integration
    :param h: the step size of the trapezoid
    :param coefficients: the list of coefficients of the function
    :return: the area under the function from a to b with the step size of h
    """

    area = 0 # the area under a function
    while a < b:
        # Calculate the area of a trapezoid.
        area += trapezoidal_rule(function, a, a+h, *coefficients)
        # Update the lower bound.
        a += h
    return area


if __name__ == '__main__':
    print(trapz(line, 0, 10, 0.5))
    print(trapz(line, 0, 10, 0.5, 2, 5))
    print(trapz(quadratic, 0, 1, 0.5, 1))
    print(trapz(quadratic, 0, 1, 0.1, 1))
    print(trapz(quadratic, 0, 1, 0.01, 1))
    print(trapz(quadratic, 0, 1, 0.001, 1))
    print(trapz(quadratic, 2, 20, 0.001, 1, 3, 2))
    print(trapz(math.sin, 2, 20, 0.001))
