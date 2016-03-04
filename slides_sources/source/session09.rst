

.. include:: include.rst

Session Nine: Object Oriented Programming 3
*******************************************



Announcements
=============

Lightning talk schedule

Please Upload your lightning talk materials to your student directory.

PYCON
-----

https://us.pycon.org/2016/

This class qualifies any of us to go under the student rate.

Review & Questions
==================

Questions emailed in over the week.


Homework
========

Code review -- let's take a look.



Lightning Talks
===============

| |lightning-session09a|
| |lightning-session09b|
| |lightning-session09c|
| |lightning-session09d|
| |lightning-session09e|
| |lightning-session09f|
| |lightning-session09g|
| |lightning-session09h|
| |lightning-session09i|
| |lightning-session09j|
|

Framing
=======


Static and Class Methods
========================

.. rst-class:: left build
.. container::

    You've seen how methods of a class are *bound* to an instance when it is
    created.

    And you've seen how the argument ``self`` is then automatically passed to
    the method when it is called.

    And you've seen how you can call *unbound* methods on a class object so
    long as you pass an instance of that class as the first argument.

    |

    .. rst-class:: centered

    **But what if you don't want or need an instance?**

Static Methods
--------------

A *static method* is a method that doesn't get self:

.. code-block:: ipython

    In [36]: class StaticAdder:

       ....:     @staticmethod
       ....:     def add(a, b):
       ....:         return a + b
       ....:

    In [37]: StaticAdder.add(3, 6)
    Out[37]: 9

.. rst-class:: centered

[demo: :download:`static_method.py <../../Examples/Session08/static_method.py>`]


.. nextslide:: Why?

.. rst-class:: build
.. container::

    Where are static methods useful?

    Usually they aren't.  It is often better just to write a module-level function.

    An example from the Standard Library (tarfile.py):

    .. code-block:: python

        class TarInfo:
            # ...
            @staticmethod
            def _create_payload(payload):
                """Return the string payload filled with zero bytes
                   up to the next 512 byte border.
                """
                blocks, remainder = divmod(len(payload), BLOCKSIZE)
                if remainder > 0:
                    payload += (BLOCKSIZE - remainder) * NUL
                return payload

Class Methods
-------------

A class method gets the class object, rather than an instance, as the first
argument

.. code-block:: ipython

    In [41]: class Classy:
       ....:     x = 2
       ....:     @classmethod
       ....:     def a_class_method(cls, y):
       ....:         print("in a class method: ", cls)
       ....:         return y ** cls.x
       ....:
    In [42]: Classy.a_class_method(4)
    in a class method:  <class '__main__.Classy'>
    Out[42]: 16

.. rst-class:: centered

[demo: :download:`class_method.py <../../Examples/Session08/class_method.py>`]


Why?
----

.. rst-class:: build
.. container::

    Unlike static methods, class methods are quite common.

    They have the advantage of being friendly to subclassing.

    Consider this:

    .. code-block:: ipython

        In [44]: class SubClassy(Classy):
           ....:     x = 3
           ....:

        In [45]: SubClassy.a_class_method(4)
        in a class method:  <class '__main__.SubClassy'>
        Out[45]: 64

Alternate Constructors
-----------------------

Because of this friendliness to subclassing, class methods are often used to
build alternate constructors.

Consider the case of wanting to build a dictionary with a given iterable of
keys:

.. code-block:: ipython

    In [57]: d = dict([1,2,3])
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-57-50c56a77d95f> in <module>()
    ----> 1 d = dict([1,2,3])

    TypeError: cannot convert dictionary update sequence element #0 to a sequence


.. nextslide:: ``dict.fromkeys()``

The stock constructor for a dictionary won't work this way. So the dict object
implements an alternate constructor that *can*.

.. code-block:: python

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
        If not specified, the value defaults to None.
        '''
        self = cls()
        for key in iterable:
            self[key] = value
        return self

(this is actually from the OrderedDict implementation in ``collections.py``)

See also datetime.datetime.now(), etc....

.. nextslide:: Curious?

Properties, Static Methods and Class Methods are powerful features of Python's
OO model.

They are implemented using an underlying structure called *descriptors*

`Here is a low level look`_ at how the descriptor protocol works.

The cool part is that this mechanism is available to you, the programmer, as
well.

.. _Here is a low level look: https://docs.python.org/2/howto/descriptor.html


For the Circle Lab: use a class method to make an alternate constructor that takes
the diameter instead.


Special Methods & Protocols
===========================

.. rst-class:: left
.. container::

    Special methods (also called *magic* methods) are the secret sauce to Python's Duck typing.

    Defining the appropriate special methods in your classes is how you make your class act like standard classes.

What's in a Name?
-----------------

We've seen at least one special method so far::

    __init__

It's all in the double underscores...

Pronounced "dunder" (or "under-under")

try: ``dir(2)``  or ``dir(list)``

Generally Useful Special Methods
--------------------------------

Most classes should at least have these special methods:

``object.__str__``:
  Called by the str() built-in function and by the print function to compute
  the *informal* string representation of an object.

``object.__repr__``:
  Called by the repr() built-in function to compute the *official* string representation of an object.

  (ideally: ``eval( repr(something) ) == something``)


Protocols
----------

.. rst-class:: build
.. container::

    The set of special methods needed to emulate a particular type of Python object is called a *protocol*.

    Your classes can "become" like Python built-in classes by implementing the methods in a given protocol.

    Remember, these are more *guidelines* than laws.  Implement what you need.

The Numerics Protocol
---------------------

Do you want your class to behave like a number? Implement these methods:

.. code-block:: python

    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)

The Container Protocol
----------------------

Want to make a container type? Here's what you need:

.. code-block:: python

    object.__len__(self)
    object.__getitem__(self, key)
    object.__setitem__(self, key, value)
    object.__delitem__(self, key)
    object.__iter__(self)
    object.__reversed__(self)
    object.__contains__(self, item)
    object.__getslice__(self, i, j)
    object.__setslice__(self, i, j, sequence)
    object.__delslice__(self, i, j)

An Example
----------

Each of these methods supports a common Python operation.

For example, to make '+' work with a sequence type in a vector-like fashion,
implement ``__add__``:

.. code-block:: python

    def __add__(self, v):
        """return the element-wise vector sum of self and v
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])

.. rst-class:: centered

[a more complete example may be seen :download:`here <../../Examples/Session08/vector.py>`]

Protocols in Summary
--------------------

Use special methods when you want your class to act like a "standard" class in some way.

Look up the special methods you need and define them.

There's more to read about the details of implementing these methods:

* https://docs.python.org/3.5/reference/datamodel.html#special-method-names
* http://www.rafekettler.com/magicmethods.html

LAB: Properties, class methods, special methods continued
=========================================================

Let's complete our Circle class:

Steps 5-8 of:

:ref:`exercise_circle_class`


Emulating Standard types
=========================

.. rst-class:: medium

  Making your classes behave like the built-ins

Callable classes
-----------------

We've been using functions a lot:

.. code-block:: python

    def my_fun(something):
        do_something
        ...
        return something

And then we can call it:

.. code-block:: python

    result = my_fun(some_arguments)

.. nextslide::

But what if we need to store some data to know how to evaluate that function?

Example: a function that computes a quadratic function:

.. math::

    y = a x^2 + bx + c

You could pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

But what if you are using the same a, b, and c numerous times?

Or what if you need to pass this in to something
(like map) that requires a function that takes a single argument?

"Callables"
-----------

Various places in python expect a "callable" -- something that you can
call like a function:

.. code-block:: python

    a_result = something(some_arguments)

"something" in this case is often a function, but can be anything else
that is "callable".

What have we been introduced to recently that is "callable", but not a
function object?

Custom callable objects
------------------------

The trick is one of Python's "magic methods"

.. code-block:: python

    __call__(*args, **kwargs)

If you define a ``__call__`` method in your class, it will be used when
code "calls" an instance of your class:

.. code-block:: python

    class Callable:
        def __init__(self, .....)
            some_initilization
        def __call__(self, some_parameters)

Then you can do:

.. code-block:: python

    callable_instance = Callable(some_arguments)

    result = callable_instance(some_arguments)

Writing your own sequence type
------------------------------

Python has a handful of nifty sequence types built in:

 * lists
 * tuples
 * strings
 * ...

But what if you need a sequence that isn't built in?

A Sparse array
--------------

Example: Sparse Array

Sometimes we have data sets that are "sparse" -- i.e. most of the values are zero.

So you may not want to store a huge bunch of zeros.

But you do want the array to look like a regular old sequence.

So how do you do that?

The Sequence protocol
----------------------

You can make your class look like a regular python sequence by defining
the set of special methods you need:

https://docs.python.org/3/reference/datamodel.html#emulating-container-types

and

http://www.rafekettler.com/magicmethods.html#sequence

The key ones are:

+-------------------+-----------------------+
|  ``__len__``      | for ``len(sequence)`` |
+-------------------+-----------------------+
|  ``__getitem__``  | for  ``x = seq[i]``   |
+-------------------+-----------------------+
|  ``__setitem__``  | for ``seq[i] = x``    |
+-------------------+-----------------------+
|  ``__delitem__``  | for ``del seq[i]``    |
+-------------------+-----------------------+
|  ``__contains__`` | for ``x in seq``      |
+-------------------+-----------------------+

LAB: Callables & Sparse Arrays
------------------------------

Callables
---------

Write a class for a quadratic equation.

* The initializer for that class should take the parameters: ``a, b, c``

* It should store those parameters as attributes.

* The resulting instance should evaluate the function when called, and return the result:


.. code-block:: python

    my_quad = Quadratic(a=2, b=3, c=1)

    my_quad(0)

Sparse Array
------------

Write a class for a sparse array:

:ref:`exercise_sparse_array`

Review framing questions
========================


Homework
========

Finish up the labs.

Bring your questions to office hours.


Readings
========

Descriptors
-----------

Hettinger on Descriptors

https://docs.python.org/2/howto/descriptor.html


