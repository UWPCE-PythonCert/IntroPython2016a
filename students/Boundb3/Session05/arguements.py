"""
from class notes session 6:

Function arguments in variables
function arguments are really just

a tuple (positional arguments)
a dict (keyword arguments)
def f(x, y, w=0, h=0):
    print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))

position = (3,4)
size = {'h': 10, 'w': 20}

!!!!!!!!!!!!!!!!!!!! notice the * and ** below : one * for tuple items, and ** for values from a dictionary !!!!!!!

>>> f(*position, **size)
position: 3, 4 -- shape: 20, 10
Function parameters in variables
You can also pull the parameters out in the function as a tuple and a dict:

def f(*args, **kwargs):
    print("the positional arguments are:", args)
    print("the keyword arguments are:", kwargs)

In [389]: f(2, 3, this=5, that=7)
the positional arguments are: (2, 3)
the keyword arguments are: {'this': 5, 'that': 7}
This can be very powerful...

Passing a dict to str.format()
Now that you know that keyword args are really a dict, you know how this nifty trick works:

The string format() method takes keyword arguments:

In [24]: "My name is {first} {last}".format(last="Barker", first="Chris")
Out[24]: 'My name is Chris Barker'
Build a dict of the keys and values:

In [25]: d = {"last":"Barker", "first":"Chris"}
And pass to format()``with ``**

In [26]: "My name is {first} {last}".format(**d)
Out[26]: 'My name is Chris Barker'

"""
