#!/usr/bin/env python3
from numpy import trapz
from numpy import isclose
from math import sin, cos
from trap import trap

#########################################################
#################INPUT Explicit f(x)#####################
#########################################################


def linefunc(x):
    '''
    Returns f(x): y = 5
    '''
    return 5


def linearfunc(x):
    '''
    Returns f(x): y = 2x + 5
    '''
    return 2 * x + 5


def quadraticfunc(x):
    ''''
    Return f(x): y = 2(x)^2 + 4(x) + 5
    '''
    return 2*x**2 + 4*x + 5


def sinfunc(x):
    ''''
    Return f(x): y = sin(x)
    '''
    return sin(x)


#########################################################
#################INPUT General f(x)######################
#########################################################
def genlinearfunc(x, A=1, B=1):
    '''
    Returns f(x): y = Ax + B
    For arbitrary values of A and B
    '''
    return A * x + B


def genquadraticfunc(x, A=1, B=1, C=1):
    '''
    Return Return f(x): y = A(x)^2 + B(x) + C
    For arbitrary values of A, B and C
    '''
    return A*x**2 + B*x + C


def gensinfunc(x, A=1, w=1):
    '''
    Return Return f(x): y = Asin(wx)
    For arbitrary values of A, B and C
    '''
    return A*sin(w*x)


#########################################################
################TESTS USING CALC THEORY##################
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

def test_genlinear1():
    '''
    Check if area under linear function for Trap
    Is approx equal to analytical solution
    (1/2)A(b^2 - a^2)+B(b-a)
    '''
    A, B, a, b = 3, 4, 0, 100
    area1 = .5*A*(b**2 - a**2) + B*(b-a)
    area2 = trap(genlinearfunc, 0, 100, 1000, A=A, B=B)
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


def test_genquadratic1():
    '''
    Check if area under quadratic function for Trap
    Is approx equal to analytical solution
    (A/3)(b^3 - a^3) + (B/2)(b^2-a^2) + C(b-a)
    '''
    A, B, C, a, b = 2, 4, 5, 0, 100
    area1 = (A/3)*(b**3 + a**3) + (B/2)*(b**2 + a**2) + C*(b-a)
    area2 = trap(genquadraticfunc, 0, 100, 1000, A=A, B=B, C=C)
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
    assert isclose(area1, area2, atol=0.05) is True


def test_gensin1():
    '''
    Check if area under sin function for Trap
    Is approx equal to analytical solution
    sin(x) = cos(a) - cos(b)
    '''
    A, w, a, b = 2, 4, 0, 100
    area1 = (A/w)*(cos(w*a) - cos(w*b))
    area2 = trap(gensinfunc, 0, 100, 1000, A=A, w=w)
    assert isclose(area1, area2, atol=0.05) is True


#########################################################
####################TESTS USING TRAPZ####################
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


def test_genlinear2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = ax + b - generalized
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(genlinearfunc(i, A=2, B=2))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(genlinearfunc, x1, x2, step, A=2, B=2)
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


def test_genquadratic2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = ax + b - generalized
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(genquadraticfunc(i, A=2, B=2, C=2))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(genquadraticfunc, x1, x2, step, A=2, B=2, C=2)
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
    assert isclose(area1, area2, atol=0.05) is True


def test_gensin2():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = Asin(wx) - generalized
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(gensinfunc(i, A=2, w=3))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = len(xvector)
    area2 = trap(gensinfunc, x1, x2, step, A=2, w=3)
    assert isclose(area1, area2, atol=0.05) is True
