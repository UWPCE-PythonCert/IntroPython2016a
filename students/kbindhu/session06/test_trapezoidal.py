#!/usr/bin/env python
from trapezoidal import trapz
import math as mt

#definition of function to be passed to trapezoidal function
def line(x):
    return 5
def slopedLine(x,m=0,B=0):
    return m*x+B
def quadratic(x,A=0,B=0,C=0):
    return A*x**2+B*x+C
def sine(x,A=0,w=0,t=0):
    return A*(mt.sin(w*t))


#calculate area of different curves uisng actual formula
def val_line_func(m=0,B=0,a=0,b=0):
    area = .5*m*(b**2-a**2)+B*(b-a)
    return area
def val_sloped_line_func(m=0,B=0,a=0,b=0):
    area = .5*m*(b**2-a**2)+B*(b-a)
    return area
def quadratic_func(A=0,B=0,C=0,a=0,b=0):
    area=.33*A*(b*b*b-a*a*a)+.5*B*(b**2-a**2)+C*(b-a)
    return area
def sin_func(A=0,w=0,t=0,a=0,b=0):
    area=A*(mt.cos(w*a)-mt.cos(w*b))*.33
    return area

#TESTS
def test_line():
    area1 =trapz(line,0,100)
    area2=val_line_func(B=5,a=0,b=100)
    t=isclose(area1,area2)
    print (t)

def test_slopedline():
    area1=trapz(slopedLine,0,100,m=2,B=2)
    area2=val_sloped_line_func(m=2,B=2,a=0,b=100)
    t=isclose(area1,area2)
    print (t)

def test_quadratic():
    area1=trapz(quadratic,0,100,A=1,B=1,C=2)
    area2=quadratic_func(A=1,B=1,C=2,a=0,b=100)
    t=isclose(area1,area2)
    print (t)

def test_sine():
    area1=trapz(sine,0,100,A=2,w=1,t=1)
    area2=sin_func(A=2,w=1,t=1,a=0,b=100)
    t=isclose(area1,area2)
    print (t)

def isclose(area1,area2):
    if (abs(area2-area1)<1e-2):
        return True
