#!/usr/bin/env python3

import math

def trapz(fun, a, b):

    # Redefine range to do floating point
    def frange(start, stop, step):
        i = start
        while i < stop:
            yield i
            i += step

    # Increase precision by always using floating point
    area = 0.0
    step = (float(b) - float(a)) / 200.0

    for i in frange(float(a),float(b),step):
        area += fun(i) * step

    return area


# Example functions
def l(x):
    return 5.0

def s(x):
    return math.sqrt(1+math.sin(x)**3)

def t(x):
    return math.tan(x)

# Assert my answers are similar to a Trapezoidal Rule Calculator

assert round(trapz(s, 0, 10),2) == round(10.1810116595807,2)
assert round(trapz(l, 0, 10),2) == round(50.0,2)
assert round(trapz(t, 0, 10),1) == round(16.5054761640473,1)

