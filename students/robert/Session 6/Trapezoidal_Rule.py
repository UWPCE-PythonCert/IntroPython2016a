#!/usr/bin/env python 

#import math

"""
def line(x):
    function = 2*x + 5
    return function

def line(x,A,w)
    function = A*math.sin(w*x)
    return function
"""

def quadratic(x, A=0, B=0, C=0):
    return A * x**2 + B * x + C

def trapz(quadratic,a,b,A,B,C):
#def trapz(line,a,b):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for teh integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    """
    f1 = 0  
    for i in range(99):
        f1 += quadratic(a+ (b-a)/100*(i + 1),A,B,C)
#        f1 += line(a+ (b-a)/100*(i + 1))
    area = (b-a)/100*((quadratic(a,A,B,C)+quadratic(b,A,B,C))/2+f1)
#    area = (b-a)/100*((line(a)+line(b))/2+f1)
    return area
#   pass

"""
    area = (b-a)*line
    return area
    line = line()

"""
coef = {'A':1,'B':3,'C':2}
area = trapz(quadratic,0,10,**coef)
#area = trapz(line,0,10)

print(area)

#How to pass function?
