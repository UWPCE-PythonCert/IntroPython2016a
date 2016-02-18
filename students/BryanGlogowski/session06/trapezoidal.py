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
        area += ((fun(i) + fun(i+step)) / 2.0) * step

    return area


# Example functions
def l(x):
    return 5.0

def s(x):
    return math.sqrt(1+math.sin(x)**3)

def t(x):
    return math.tan(x)

def st(x):
    return math.tan(x) * math.sin(x)

# Assert my answers are similar to a Trapezoidal Rule Calculator

# ...with a specified precision:
precision = 5

print(round(trapz(s, 0, 10),precision))
print(round(10.1810116595807,precision))
assert round(trapz(s, 0, 10),precision) == round(10.1810116595807,precision)

print(round(trapz(l, 0, 10),precision))
print(round(50.0,precision))
assert round(trapz(l, 0, 10),precision) == round(50.0,precision)

print(round(trapz(t, 0, 10),precision))
print(round(16.5054761640473,precision))
assert round(trapz(t, 0, 10),precision) == round(16.5054761640473,precision)

# More tests...
assert round(trapz(st, 0, 10),precision) == round(9.8923666153375,precision)
assert round(trapz(st, 10, 20),precision) == round(9.44777265586442,precision)
assert round(trapz(st, -10, 20),precision) == round(58.5233631220135,precision)
assert round(trapz(st, -10.2, 20.53),precision) == round(-0.409523489721687,precision)
