#define trapez function

"""Compute the area under the curve defined by
y = fun(x), for x between a and b

:param fun: the function to evaluate
:type fun: a function that takes a single parameter

:param a: the start point for teh integration
:type a: a numeric value

:param b: the end point for the integration
:type b: a numeric value"""

def trapz(func,a,b,**kwargs):
    N=100
    sum=0
    for i in range (1,N):
        i=i/10
        sum = sum+func(a+i*(b-a)/N,**kwargs)
    midpoint=(func(a,**kwargs)+func(b,**kwargs))/2
    area=(b-a)/N*(midpoint+sum)
    return area



