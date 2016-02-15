#!/usr/bin/env python3
from numpy import trapz
from numpy import isclose
from trap import trap


def linefunc(x):
    '''
    Returns f(x): y = 5
    '''
    return 5

def linearfunc(x):
    return 2 * x

def linearfunc(x):
    '''
    Returns f(x): y = 2x
    '''
    return 2 * x

def test_line():
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
    step = (xvector[-1]-xvector[0])/len(xvector)
    area2 = trap(linefunc, x1, x2, step)
    assert isclose(area1, area2) is True

def test_linear():
    '''
    Checks if area under curve computed for Trap func
    Is approximately equal to Trapz function from Numpy
    For f(x) = 2x
    '''
    xvector = range(100)
    yvector = []
    for i in xvector:
        yvector.append(linearfunc(i))
    area1 = trapz(yvector, x=xvector)
    x1, x2 = xvector[0], xvector[-1]
    step = (xvector[-1]-xvector[0])/len(xvector)
    area2 = trap(linefunc, x1, x2, step)