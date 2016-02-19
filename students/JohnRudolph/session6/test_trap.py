#!/usr/bin/env python3
from numpy import trapz
from numpy import isclose
from math import sin, cos
from trap import trap

#########################################################
###############          INPUT f(x)       ###############
#########################################################
def linefunc(x):
    '''
    Returns f(x): y = 5
    '''
    return 5


def linearfunc(x):
    '''
    Returns f(x): y = Ax + B
    '''
    return 2 * x + 5


def quadraticfunc(x):
    ''''
    Return f(x): y = A(x)^2 + B(x) + C
    '''
    return 2*x**2 + 4*x + 5


def sinfunc(x):
    ''''
    Return f(x): y = sin(x)
    '''
    return sin(x)

#########################################################
############     TESTS USING CALC THEORY    #############
#########################################################
def test_linear1():
    '''
    Check if area under linear function for Trap
    Is approx equal to analytical solution
    (1/2)A(b^2 - a^2)+B(b-a)
    '''
    A, B, a, b = 2, 5, 0, 100
    area1 = .5*A*(b**2 - a**2) + B*(b-a)
    area2 = trap(linearfunc, 0, 100, 1000)
    assert isclose(area1, area2) is True

def test_quadratic1():
    '''
    Check if area under quadratic function for Trap
    Is approx equal to analytical solution
    (A/3)(b^3 - a^3) + (B/2)(b^2-a^2) + C(b-a)
    '''
    A, B, C, a, b = 2, 4, 5, 0, 100
    area1 = (A/3)*(b**3 + a**3) + (B/2)*(b**2 + a**2) + C*(b-a)
    area2 = trap(quadraticfunc, 0, 100, 1000)
    assert isclose(area1, area2) is True


def test_sin1():
    '''
    Check if area under sin function for Trap
    Is approx equal to analytical solution
    sin(x) = cos(a) - cos(b)
    '''
    a, b = 0, 100
    area1 = cos(a) - cos(b)
    area2 = trap(sinfunc, 0, 100, 1000)
    assert isclose(area1, area2, atol=0.01) is True

#########################################################
###############     TESTS USING TRAPZ     ###############
#########################################################

def test_line2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = 5
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(linefunc(i))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(linefunc, x1, x2, step)
    assert isclose(area1, area2) is True


def test_linear2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = ax + b
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(linearfunc(i))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(linearfunc, x1, x2, step)
    assert isclose(area1, area2) is True


def test_quadratic2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = ax^2 + bx + c
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(quadraticfunc(i))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(quadraticfunc, x1, x2, step)
    assert isclose(area1, area2) is True


def test_sin2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = sin(x)
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(sinfunc(i))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(sin, x1, x2, step)
    assert isclose(area1, area2, atol=0.01) is True
