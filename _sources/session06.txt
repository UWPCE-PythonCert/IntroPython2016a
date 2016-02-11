

.. include:: include.rst

Session Six: Exceptions, Testing and Advanced Argument Passing
**************************************************************



Announcements
=============

Review & Questions
==================

Homework
========

Code review -- let's take a look.


Lightning talks
===============

| |lightning-session06a|
| |lightning-session06b|
| |lightning-session06c|
| |lightning-session06d|
| |lightning-session06e|
|


Framing
=======

You've just started a new job, or you've inherited a project as a contractor.  Your task is to migrate a system from Python 2.something to Python 3.something.  All of the frameworks and major libraries in the system are years behind current versions.  There are thousands of lines of code spread across dozens of modules.  And you're moving from Oracle to Postgres.  What do you do?

You are the CTO of a new big data company.  Your CEO wants you to open the your Python API so that third-party developers, your clients, can supply their own functions to crunch data on your systems.  What do you do?



Exceptions
==========

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")

Exceptions
----------

Use Exceptions, rather than your own tests:

Don't do this:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)   # never called if file missing

It will almost always work -- but the almost will drive you crazy

.. nextslide::

Example from homework

.. code-block:: python

    if num_in.isdigit():
        num_in = int(num_in)

but -- ``int(num_in)`` will only work if the string can be converted to an integer.

So you can do

.. code-block:: python

    try:
        num_in = int(num_in)
    except ValueError:
        print("Input must be an integer, try again.")

Or let the Exception be raised....


.. nextslide:: EAFP


"it's Easier to Ask Forgiveness than Permission"

 -- Grace Hopper


http://www.youtube.com/watch?v=AZDWveIdqjY

(PyCon talk by Alex Martelli)

.. nextslide:: Do you catch all Exceptions?

For simple scripts, let exceptions happen.

Only handle the exception if the code can and will do something about it.

(much better debugging info when an error does occur)

Exceptions -- finally
---------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")
    finally:
        do_some_clean-up

The ``finally:``  clause will always run

Exceptions -- else
-------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError:
        print("couldn't open missing.txt")
    else:
        process(f) # only called if there was no exception

Advantage:

you know where the Exception came from

Exceptions -- using them
------------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError as the_error:
        print(the_error)
        the_error.extra_info = "some more information"
        raise

Particularly useful if you catch more than one exception:

.. code-block:: python

    except (IOError, BufferError, OSError) as the_error:
        do_something_with (the_error)

Raising Exceptions
-------------------

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("b can not be zero")
        else:
            return a / b


when you call it:

.. code-block:: ipython

    In [515]: divide (12,0)
    ZeroDivisionError: b can not be zero

Built in Exceptions
-------------------

You can create your own custom exceptions

But...

.. code-block:: python

    exp = \
     [name for name in dir(__builtin__) if "Error" in name]
    len(exp)
    32


For the most part, you can/should use a built in one

.. nextslide::

Choose the best match you can for the built in Exception you raise.

Example (from last week's exercises)::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise ValueError

Is it the *value* or the input the problem here?

Nope: the *type* is the problem::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise TypeError

but should you be checking type anyway? (EAFP)

Lab: Exceptions
---------------

A number of you already did this -- so do it at home if you haven't

:ref:`exercise_exceptions_lab`





Testing
=======

.. rst-class:: build left
.. container::

    You've already seen some a very basic testing strategy.

    You've written some tests using that strategy.

    These tests were pretty basic, and a bit awkward in places (testing error
    conditions in particular).

    .. rst-class:: centered

    **It gets better**

Test Runners
------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.

.. rst-class:: build

* They are run only when the file is executed
* They are always run when the file is executed
* You can't do anything else when the file is executed without running tests.

.. rst-class:: build
.. container::

    This is not optimal.

    Python provides testing systems to help.

Standard Library: ``unittest``
-------------------------------

The original testing system in Python.

``import unittest``

More or less a port of ``Junit`` from Java

A bit verbose: you have to write classes & methods

(And we haven't covered that yet!)

Using ``unittest``
-------------------

You write subclasses of the ``unittest.TestCase`` class:

.. code-block:: python

    # in test.py
    import unittest

    class MyTests(unittest.TestCase):
        def test_tautology(self):
            self.assertEquals(1, 1)

Then you run the tests by using the ``main`` function from the ``unittest``
module:

.. code-block:: python

    # in test.py
    if __name__ == '__main__':
        unittest.main()

.. nextslide:: Testing Your Code

This way, you can write your code in one file and test it from another:

.. code-block:: python

    # in my_mod.py
    def my_func(val1, val2):
        return val1 * val2

    # in test_my_mod.py
    import unittest
    from my_mod import my_func

    class MyFuncTestCase(unittest.TestCase):
        def test_my_func(self):
            test_vals = (2, 3)
            expected = reduce(lambda x, y: x * y, test_vals)
            actual = my_func(*test_vals)
            self.assertEquals(expected, actual)

    if __name__ == '__main__':
        unittest.main()

.. nextslide:: Advantages of ``unittest``

.. rst-class:: build
.. container::

    The ``unittest`` module is pretty full featured

    It comes with the standard Python distribution, no installation required.

    It provides a wide variety of assertions for testing all sorts of situations.

    It allows for a setup and tear down workflow both before and after all tests and before and after each test.

    It's well known and well understood.

.. nextslide:: Disadvantages:

.. rst-class:: build
.. container::


    It's Object Oriented, and quite heavy.

      - modeled after Java's ``junit`` and it shows...

    It uses the framework design pattern, so knowing how to use the features
    means learning what to override.

    Needing to override means you have to be cautious.

    Test discovery is both inflexible and brittle.

    And there is no built-in parameterized testing.

Other Options
-------------

There are several other options for running tests in Python.

* `Nose`: https://nose.readthedocs.org/

* `pytest`: http://pytest.org/latest/

* ... And many frameworks supply their own test runners

Both are very capable and widely used. I have a personal preference for pytest -- so we'll use it for this class

Installing ``pytest``
---------------------

The first step is to install the package:

.. code-block:: bash

    $ python3 -m pip install pytest

Once this is complete, you should have a ``py.test`` command you can run
at the command line:

.. code-block:: bash

    $ py.test

If you have any tests in your repository, that will find and run them.

.. rst-class:: build
.. container::

    **Do you?**

Pre-existing Tests
------------------

Let's take a look at some examples.

``IntroToPython\Examples\Session05``

`` $ py.test``

You can also run py.test on a particular test file:

``py.test test_this.py``

The results you should have seen when you ran ``py.test`` above come
partly from these files.

Let's take a few minutes to look these files over.

.. nextslide:: What's Happening Here.

When you run the ``py.test`` command, ``pytest`` starts in your current
working directory and searches the filesystem for things that might be tests.

It follows some simple rules:

.. rst-class:: build

* Any python file that starts with ``test_`` or ``_test`` is imported.
* Any functions in them that start with ``test_`` are run as tests.
* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.


.. nextslide:: pytest

This test running framework is simple, flexible and configurable.

`Read the documentation`_ for more information.

.. _Read the documentation: http://pytest.org/latest/getting-started.html#getstarted

.. nextslide:: Test Driven Development

What we've just done here is the first step in what is called **Test Driven
Development**.

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run our tests is a goad to us to write
the code that fixes these tests.

Let's do that next!

Test Driven development demo
----------------------------

In ``Examples/Session05/test_cigar_party.py``


Lab: Testing
------------

Pick an example from codingbat:

``http://codingbat.com``

Do a bit of test-driven development on it:

 * run something on the web site.
 * write a few tests using the examples from the site.
 * then write the function, and fix it 'till it passes the tests.

Do at least two of them.

Advanced Argument Passing
=========================

Calling a function
------------------

Python functions are objects, so if you don't call them, you don't get an error, you just get the function object, usually not what you want::

        elif donor_name.lower == "exit":

This is comparing the string ``lower`` method to the string "exit" and they are never going to be equal!

That should be::

    elif donor_name.lower() == "exit":

This is actually a pretty common typo -- keep an eye out for it when you get strange errors, or something just doesn't seem to be getting triggered.


Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x=0, y=0, z=0):
            print(x,y,z)
       .....:
    In [152]: fun(1,2,3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(z=3, y=2)
    0 2 3


.. nextslide::


A Common Idiom:

.. code-block:: python

    def fun(x, y=None):
        if y is None:
            do_something_different
        go_on_here


.. nextslide::

Can set defaults to variables

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4


.. nextslide::

Defaults are evaluated when the function is defined

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4
    In [159]: y = 6
    In [160]: fun()
    x is: 4

This is a **very** important point -- I will repeat it!

Function arguments in variables
-------------------------------

function arguments are really just

* a tuple (positional arguments)
* a dict (keyword arguments)

.. code-block:: python

    def f(x, y, w=0, h=0):
        print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))

    position = (3,4)
    size = {'h': 10, 'w': 20}

    >>> f(*position, **size)
    position: 3, 4 -- shape: 20, 10

Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    def f(*args, **kwargs):
        print("the positional arguments are:", args)
        print("the keyword arguments are:", kwargs)

    In [389]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the keyword arguments are: {'this': 5, 'that': 7}

This can be very powerful...

Passing a dict to str.format()
-------------------------------

Now that you know that keyword args are really a dict,
you know how this nifty trick works:

The string ``format()`` method takes keyword arguments:

.. code-block:: ipython

    In [24]: "My name is {first} {last}".format(last="Barker", first="Chris")
    Out[24]: 'My name is Chris Barker'

Build a dict of the keys and values:

.. code-block:: ipython

    In [25]: d = {"last":"Barker", "first":"Chris"}

And pass to ``format()``with ``**``

.. code-block:: ipython

    In [26]: "My name is {first} {last}".format(**d)
    Out[26]: 'My name is Chris Barker'

Lab: Keyword Arguments
----------------------

.. rst-class:: medium

  keyword arguments:

* Write a function that has four optional parameters (with defaults):

  - fore_color
  - back_color
  - link_color
  - visited_color

* Have it print the colors (use strings for the colors)
* Call it with a couple different parameters set
* Have it pull the parameters out with ``*args, **kwargs``
  - and print those



Switch/case
-----------

Python does not have a switch/case statement.  Why not?

https://www.python.org/dev/peps/pep-3103/

What to use instead of "switch-case"?

switch-case
-----------

A number of languages have a "switch-case" construct::

    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };

How do you say this in Python?

``if-elif`` chains
------------------

The obvious way to say it is a chain of ``elif`` statements:

.. code-block:: python

    if argument ==  0:
        return "zero"
    elif argument == 1:
        return "one"
    elif argument == 2:
        return "two"
    else:
        return "nothing"

And there is nothing wrong with that, but....

Dict as switch
--------------

The ``elif`` chain is neither elegant nor efficient. There are a number of ways to say it in python -- but one elegant one is to use a dict:

.. code-block:: python

    arg_dict = {0:"zero", 1:"one", 2: "two"}
        dict.get(argument, "nothing")

Simple, elegant and fast.

You can do a dispatch table by putting functions as the value.

Example: Chris' mailroom2 solution.




Lab: Functions as objects
-------------------------

Let's use some of this ability to use functions as objects for something useful:

:ref:`exercise_trapezoidal_rule`

Review framing questions
========================


Homework
========

Finish the Labs
