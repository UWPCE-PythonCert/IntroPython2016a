

.. include:: include.rst

Session Ten: Functional Programming
***********************************


Announcements
=============

Review & Questions
==================

Homework
========

Code review -- let's take a look.



Lightning Talks
===============

| |lightning-session10a|
| |lightning-session10b|
| |lightning-session10c|
| |lightning-session10d|
| |lightning-session10e|
| |lightning-session10f|
| |lightning-session10g|
| |lightning-session10h|
| |lightning-session10i|
| |lightning-session10j|
|

Framing
=======


Functional Programming
======================

No real consensus about what that means.

But there are some "classic" methods available in Python.

map
---

``map``  "maps" a function onto a sequence of objects -- It applies the function to each item in the list, returning another list


.. code-block:: ipython

    In [23]: l = [2, 5, 7, 12, 6, 4]
    In [24]: def fun(x):
                 return x*2 + 10
    In [25]: map(fun, l)
    Out[25]: [14, 20, 24, 34, 22, 18]


But if it's a small function, and you only need it once:

.. code-block:: ipython

    In [26]: map(lambda x: x*2 + 10, l)
    Out[26]: [14, 20, 24, 34, 22, 18]

filter
------

``filter``  "filters" a sequence of objects with a boolean function --
It keeps only those for which the function is True -- filtering our the rest.

To get only the even numbers:

.. code-block:: ipython

    In [27]: l = [2, 5, 7, 12, 6, 4]
    In [28]: filter(lambda x: not x%2, l)
    Out[28]: [2, 12, 6, 4]

If you pass ``None`` to ``filter()``, you get only items that evaluate to true:

.. code-block:: ipython

    In [1]: l = [1, 0, 2.3, 0.0, 'text', '', [1,2], [], False, True, None ]

    In [2]: filter(None, l)
    Out[2]: [1, 2.3, 'text', [1, 2], True]

reduce
------

``reduce``  "reduces" a sequence of objects to a single object with a function that combines two arguments

To get the sum:

.. code-block:: ipython

    In [30]: l = [2, 5, 7, 12, 6, 4]
    In [31]: reduce(lambda x,y: x+y, l)
    Out[31]: 36


To get the product:

.. code-block:: ipython

    In [32]: reduce(lambda x,y: x*y, l)
    Out[32]: 20160

or

.. code-block:: ipython

    In [13]: import operator
    In [14]: reduce(operator.mul, l)
    Out[14]: 20160

Comprehensions
--------------

Couldn't you do all this with comprehensions?

Yes:

.. code-block:: ipython

    In [33]: [x+2 + 10 for x in l]
    Out[33]: [14, 17, 19, 24, 18, 16]

    In [34]: [x for x in l if not x%2]
    Out[34]: [2, 12, 6, 4]

    In [6]: l
    Out[6]: [1, 0, 2.3, 0.0, 'text', '', [1, 2], [], False, True, None]
    In [7]: [i for i in l if i]
    Out[7]: [1, 2.3, 'text', [1, 2], True]

(Except Reduce)

But Guido thinks almost all uses of reduce are really ``sum()``

Functional Programming
----------------------

Comprehensions and map, filter, reduce are all "functional programming" approaches}

``map, filter``  and ``reduce``  pre-date comprehensions in Python's history

Some people like that syntax better

And "map-reduce" is a big concept these days for parallel processing of "Big Data" in NoSQL databases.

(Hadoop, MongoDB, etc.)

Comprehensions
==============

List comprehensions
-------------------

A bit of functional programming

consider this common ``for`` loop structure:

.. code-block:: python

    new_list = []
    for variable in a_list:
        new_list.append(expression)

This can be expressed with a single line using a "list comprehension"

.. code-block:: python

    new_list = [expression for variable in a_list]


.. nextslide::

What about nested for loops?

.. code-block:: python

    new_list = []
    for var in a_list:
        for var2 in a_list2:
            new_list.append(expression)

Can also be expressed in one line:

.. code-block:: python

    new_list =  [exp for var in a_list for var2 in a_list2]

You get the "outer product", i.e. all combinations.

.. nextslide::

But usually you at least have a conditional in the loop:

.. code-block:: python

    new_list = []
    for variable in a_list:
        if something_is_true:
            new_list.append(expression)

You can add a conditional to the comprehension:

.. code-block:: python

    new_list = [expr for var in a_list if something_is_true]

.. nextslide::

Examples:

.. code-block:: ipython

    In [341]: [x**2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x+y for x in range(3) for y in range(5,7)]
    Out[342]: [5, 6, 6, 7, 7, 8]

    In [343]: [x*2 for x in range(6) if not x%2]
    Out[343]: [0, 4, 8]

.. nextslide::

Remember this from earlier today?

.. code-block:: python

    [name for name in dir(__builtin__) if "Error" in name]
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BufferError',
     'EOFError',
     ....

Set Comprehensions
------------------

You can do it with sets, too:

.. code-block:: python

    new_set = { value for variable in a_sequence }


same as for loop:

.. code-block:: python

    new_set = set()
    for key in a_list:
        new_set.add(value)


.. nextslide::

Example: finding all the vowels in a string...

.. code-block:: ipython

    In [19]: s = "a not very long string"

    In [20]: vowels = set('aeiou')

    In [21]: { l for l in s if l in vowels }
    Out[21]: {'a', 'e', 'i', 'o'}

Side note: why did I do ``set('aeiou')`` rather than just `aeiou` ?

Dict Comprehensions
-------------------

Also with dictionaries

.. code-block:: python

    new_dict = { key:value for variable in a_sequence}


same as for loop:

.. code-block:: python

    new_dict = {}
    for key in a_list:
        new_dict[key] = value



.. nextslide::

Example

.. code-block:: ipython

    In [22]: { i: "this_%i"%i for i in range(5) }
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}


(not as useful with the ``dict()``  constructor...)

===
LAB
===

List comps exercises:

:ref:`exercise_comprehensions`



Lightning Talk
----------------

.. rst-class:: medium

Anonymous functions
===================

lambda
------

.. code-block:: ipython

    In [171]: f = lambda x, y: x+y
    In [172]: f(2,3)
    Out[172]: 5

Content of function can only be an expression -- not a statement

Anyone remember what the difference is?

Called "Anonymous": it doesn't get a name.

.. nextslide::

It's a python object, it can be stored in a list or other container

.. code-block:: ipython

    In [7]: l = [lambda x, y: x+y]
    In [8]: type(l[0])
    Out[8]: function


And you can call it:

.. code-block:: ipython

    In [9]: l[0](3,4)
    Out[9]: 7

Functions as first class objects
---------------------------------

You can do that with "regular" functions too:

.. code-block:: ipython

    In [12]: def fun(x,y):
       ....:     return x+y
       ....:
    In [13]: l = [fun]
    In [14]: type(l[0])
    Out[14]: function
    In [15]: l[0](3,4)
    Out[15]: 7


A bit more about lambda
------------------------

It is very useful for specifying sorting as well:

.. code-block:: ipython

    In [55]: lst = [("Chris","Barker"), ("Fred", "Jones"), ("Zola", "Adams")]

    In [56]: lst.sort()

    In [57]: lst
    Out[57]: [('Chris', 'Barker'), ('Fred', 'Jones'), ('Zola', 'Adams')]

    In [58]: lst.sort(key=lambda x: x[1])

    In [59]: lst
    Out[59]: [('Zola', 'Adams'), ('Chris', 'Barker'), ('Fred', 'Jones')]

lambda in keyword arguments
---------------------------

.. code-block:: ipython

    In [186]: l = []
    In [187]: for i in range(3):
        l.append(lambda x, e=i: x**e)
       .....:
    In [189]: for f in l:
        print(f(3))
    1
    3
    9

Note when the keyword argument is evaluated: this turns out to be very handy!

Lab: Lambda
===========

Here's an exercise to try out some of this:

:ref:`exercise_lambda_magic`


Closures and function Currying
==============================

Defining specialized functions on the fly

Closures
--------

"Closures" and "Currying" are cool CS terms for what is really just defining functions on the fly.

you can find a "proper" definition here:

https://en.wikipedia.org/wiki/Closure_(computer_programming)

but I even have trouble following that.

So let's go straight to an example:

.. nextslide::

.. code-block:: python

    def counter(start_at=0):
        count = [start_at]
        def incr():
            count[0] += 1
            return count[0]
        return incr

What's going on here?

We have stored the ``start_at`` value in a list.

Then defined a function, ``incr`` that adds one to the value in the list, and returns that value.

[ Quiz: why is it: ``count = [start_at]``, rather than just ``count=start_at`` ]

.. nextslide::

So what type of object do you get when you call ``counter()``?

.. code-block:: ipython

    In [37]: c = counter(start_at=5)

    In [38]: type(c)
    Out[38]: function

So we get a function back -- makes sense. The ``def`` defines a function, and that function is what's getting returned.

Being a function, we can, of course, call it:

.. code-block:: ipython

    In [39]: c()
    Out[39]: 6

    In [40]: c()
    Out[40]: 7

Each time is it called, it increments the value by one.

.. nextslide::

But what happens if we call ``counter()`` multiple times?

.. code-block:: ipython

    In [41]: c1 = counter(5)

    In [42]: c2 = counter(10)

    In [43]: c1()
    Out[43]: 6

    In [44]: c2()
    Out[44]: 11

So each time ``counter()`` is called, a new function is created. And that function has its own copy of the ``count`` object. This is what makes in a "closure" -- it carries with it the scope in which is was created.

the returned ``incr`` function is a "curried" function -- a function with some parameters pre-specified.

``functools.partial``
---------------------

The ``functools`` module in the standard library provides utilities for working with functions:

https://docs.python.org/3.5/library/functools.html

Creating a curried function turns out to be common enough that the ``functools.partial`` function provides an optimized way to do it:

What functools.partial does is:

 * Makes a new version of a function with one or more arguments already filled in.
 * The new version of a function documents itself.

Example:

.. code-block:: python

    def power(base, exponent):
        """returns based raised to the give exponent"""
        return base ** exponent

Simple enough. but what if we wanted a specialized ``square`` and ``cube`` function?

We can use ``functools.partial`` to *partially* evaluate the function, giving us a specialized version:

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

Recursion
---------

You've seen functions that call other functions.

If a function calls *itself*, we call that **recursion**

Like with other functions, a call within a call establishes a *call stack*

With recursion, if you are not careful, this stack can get *very* deep.

Python has a maximum limit to how much it can recurse. This is intended to
save your machine from running out of RAM.

.. nextslide:: Recursion can be Useful

Recursion is especially useful for a particular set of problems.

For example, take the case of the *factorial* function.

In mathematics, the *factorial* of an integer is the result of multiplying that
integer by every integer smaller than it down to 1.

::

    5! == 5 * 4 * 3 * 2 * 1

We can use a recursive function nicely to model this mathematical function


``assert``
----------

Writing ``tests`` that demonstrate that your program works is an important part of learning to program.

The python ``assert`` statement is useful in writing simple tests
for your code.

.. code-block:: ipython

    In [1]: def add(n1, n2):
       ...:     return n1 + n2
       ...:

    In [2]: assert add(3, 4) == 7

    In [3]: assert add(3, 4) == 10

    ---------------------------------------------------------------------
    AssertionError                     Traceback (most recent call last)
    <ipython-input-3-6731d4ac4476> in <module>()
    ----> 1 assert add(3, 4) == 10

    AssertionError:

Lab: Fibonacci
==============

Let's write a few functions in class:

:ref:`exercise_fibonacci`



Where we've been.... 
====================



Python 100
----------

.. rst-class:: left

  Once upon a time, there was a little scripting language called Python.

  Python 100, this course, is designed to provide the basics or the core of the language.

  By the end of this course you should be able to "create something useful" with Python.



Python 200
----------

.. rst-class:: left

  Also known as Internet Programming with Python, Python 200 is designed to provide the basics of web programming.

  Here, already, you're going to run into Python language constructs that were once upon a time considered "optional."

Python 300
----------

.. rst-class:: left

  "As soon as an optional advanced language feature is used by anyone in an organization, it is no longer optional--it is effectively imposed on everyone in the organization. The same holds true for externally developed software you use in your systems--if the software’s author uses an advanced or extraneous language feature, it’s no longer entirely optional for you, because you have to understand the feature to reuse or change the code."

  "Generators, decorators, slots, properties, descriptors, metaclasses, context managers, closures, super, namespace packages, unicode, function annotations, relative imports, keyword-only arguments, class and static methods, and even obscure applications of comprehensions and operator overloading.... 

  If any person or program you need to work with uses such tools, they automatically become part of your required knowledge base too. The net effect of such over-engineering is to either escalate learning requirements radically, or foster a user base that only partially understands the tools they employ. This is obviously less than ideal for those hoping to use Python in simpler ways, and contradictory to the scripting motif."

  -- Mark Lutz on Optional Language Features

. . . and where we're going
---------------------------

.. rst-class:: left

  We've been learning to drive this car called Python.  You'll learn more about how to drive it in Python 200.

  In Python 300 we give you the tools to become a mechanic.

  In the meantime you should at least be familiar with some of these language constructs....

Where could you go from here?
=============================



Know Python's built-in functions
--------------------------------

https://docs.python.org/3/library/functions.html

Many of these should at this point be familiar.

Get to know the others.



Scan the PEPs
-------------

Python Enhancement Proposals

https://www.python.org/dev/peps/

Know what sorts of topics are discussed.  Find the ones that interest you and could assist in your work.

These will provided clarity into the sorts of problems the language designers are trying to solve, how they choose to solve them, and the tradeoffs they needed to make.  PEPs also provide hints to alternative solutions.



Scan What's New
---------------

When a new version of Python is released, scan the release notes.

https://docs.python.org/3/whatsnew/



Read the source
---------------

https://www.python.org/downloads/source/

Let's say you want to learn more about lambda or classes.  Search the code for related terms to see how the pros do it.


Contribute to a project
-----------------------

Go to github.com and search for something that interests you.

https://github.com/search?l=Python&q=python&type=Repositories&utf8=✓



Go to Meetups
-------------

http://www.meetup.com/topics/python/



Take Py200 and Py300
--------------------

Py200 -- Internet Programming in Python

http://www.pce.uw.edu/courses/internet-programming-python.html


Py300 -- Systems Development in Python

http://www.pce.uw.edu/courses/system-development-python.html



Review framing questions
========================


Readings
========



Functools
---------

https://pymotw.com/2/functools/

http://www.pydanny.com/python-partials-are-fun.html



Closures & Currying
-------------------

http://www.programiz.com/python-programming/closure

https://www.clear.rice.edu/comp130/12spring/curry/



Multi-methods in Python
-----------------------

GvR on Multi-methods

http://www.artima.com/weblogs/viewpost.jsp?thread=101605
