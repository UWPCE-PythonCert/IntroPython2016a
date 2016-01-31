"""

from greantreepress chapter 5.9 - recursion


"""

def func_n(f,t):
    f(t)

def func_action(t):
    if t>1:
       print("hi "*t)
       t=t-1
       func_action(t)
    else:
       print("this is the end of the series")



x=8
n=func_n(func_action,x)



