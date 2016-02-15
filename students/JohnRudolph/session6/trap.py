#!/usr/bin/env python3

#########################################################
##################INPUT F(X)s############################
#########################################################

def linearfunc(x):
    return 2 * x

def linefunc(x):
    return 5

#########################################################
###############TRAPEZOIDAL FUNCTIONS ####################
#########################################################

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

def createyvector(fx, xvector):
    '''
    Creates a vector of values based on
    a given function (fx) and given x values vector
    '''
    yvector = []
    for i in xvector:
        yvector.append(fx(i))
    return yvector

def trap(fx, x1, x2, step):
    '''
    This function integrates under a given function
    By using the trapezoid rule
    A defined function must be supplied
    With a start value for x1 and end value x2 which is used
    To approximate the x-axis range
    '''
    xvector = createxvector(x1, x2 + step, step)
    yvector = createyvector(fx, xvector)
    areavector = []
    
    cntr = -1
    for i, n in zip(xvector, yvector):
        cntr += 1
        if 0 < cntr < len(xvector) - 1:
            deltax = i - xvector[cntr - 1]
            deltay = (n + yvector[cntr + 1])/2
            areavector.append(deltax * deltay)

    return sum(areavector)

