#!/usr/bin/env python3

#########################################################
###############TRAPEZOIDAL FUNCTIONS ####################
#########################################################


def genquadratic(x, A=1, B=1, C=1):
    return A*x**2 + B*x + C


def createxvector(x1, x2, step):
    '''
    Creates a vector of values from
    x1 to x2 by specified step increments
    '''
    xvector = []
    while x1 <= x2:
        xvector.append(x1)
        x1 += step
    return xvector


def createyvector(fx, xvector, **kwargs):
    '''
    Creates a vector of values based on
    a given function (fx) and given x values vector
    '''
    keys = kwargs
    yvector = []
    for i in xvector:
        yvector.append(fx(i, **keys))
    return yvector


def trap(fx, x1, x2, div, **kwargs):
    '''
    This function integrates under a given function
    By using the trapezoid rule
    A defined function must be supplied
    With a start value for x1 and end value x2 which is used
    And the number of intervals to split between x1 and x2
    '''
    step = (x2 - x1) / div
    keys = kwargs
    xvector = createxvector(x1, x2, step)
    yvector = createyvector(fx, xvector, **keys)
    areavector = []
    cntr = -1
    for i, n in zip(xvector, yvector):
        cntr += 1
        if cntr < len(xvector) - 1:
            deltax = xvector[cntr + 1] - i
            deltay = (n + yvector[cntr + 1])/2
            areavector.append(deltax * deltay)

    return sum(areavector)

print(trap(genquadratic, 0, 100, 20, A=2, B=2, C=2))