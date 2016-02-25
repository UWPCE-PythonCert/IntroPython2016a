

.. include:: include.rst


Session Eight: Object Oriented Programming
******************************************

Object Oriented Programming continued...


Announcements
=============


Review & Questions
==================


Homework
========

Code review -- let's take a look.



Homework Notes:
---------------

``**kwargs`` will always define a ``kwargs`` dict: it just may be empty.

And there is no need to check if it's empty before trying to loop through it.

.. code-block:: python

    if self.attributes != {}:
        for key, value in self.attributes.items():
            self.atts += ' {}="{}"'.format(key, value)

no need for ``!= {}`` -- an empty dict is "Falsey"

**but** no need for that check at all. If the dict (or ist, or tuple) is
empty, then the loop is a do-nothing operation:

* notes on Duck Typing: :ref:`exercise_html_renderer` and  code review

* anyone stuck that wants to work through your code?


Lightning Talks
===============

| |lightning-session08a|
| |lightning-session08b|
| |lightning-session08c|
| |lightning-session08d|
| |lightning-session08e|
|


Framing
=======


Multiple Inheritance
====================

Multiple inheritance: Inheriting from more than one class

Simply provide more than one parent.

.. code-block:: python

    class Combined(Super1, Super2, Super3):
        def __init__(self, something, something else):
            # some custom initialization here.
            Super1.__init__(self, ......)
            Super2.__init__(self, ......)
            Super3.__init__(self, ......)
            # possibly more custom initialization

(calls to the super class ``__init__``  are optional -- case dependent)



Python's Multiple Inheritance Model
-----------------------------------

Cooperative Multiple Inheritance

Emphasis on cooperative!

* Play by the rules and everybody benefits (parents, descendants).
* Play by the rules and nobody gets hurt (yourself, mostly).
* We're all adults here.

What could go wrong?



The Diamond Problem
-------------------

With Python "new style" classes everything is descended from 'object'.  Thus, the moment you invoke multiple inheritance you have the diamond problem.

https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem



``super()``
-----------

``super()``: use it to call a superclass method, rather than explicitly calling the unbound method on the superclass.

instead of:

.. code-block:: python

    class A(B):
        def __init__(self, *args, **kwargs)
            B.__init__(self, *argw, **kwargs)
            ...

You can do:

.. code-block:: python

    class A(B):
        def __init__(self, *args, **kwargs)
            super().__init__(*argw, **kwargs)
            ...

MRO: Method Resolution Order
----------------------------

.. code-block:: python

    class Combined(Super1, Super2, Super3)

Attributes are located bottom-to-top, left-to-right

* Is it an instance attribute ?
* Is it a class attribute ?
* Is it a superclass attribute ?

  - Is  it an attribute of the left-most superclass?
  - Is  it an attribute of the next superclass?
  - and so on up the hierarchy...

* Is it a super-superclass attribute ?
* ... also left to right ...

http://python-history.blogspot.com/2010/06/method-resolution-order.html

Super's Superpowers
-------------------

It works out -- dynamically at runtime -- which classes are in the delegation order.

Do not be afraid.  And be very afraid.



Dependency Injection
--------------------

Super() is the right way to do dependency injection.

https://en.wikipedia.org/wiki/Dependency_injection

Compare with Monkey Patching as done in other languages.

https://en.wikipedia.org/wiki/Monkey_patch



Argument Passing
----------------

Remember that super does not only delegate to your superclass, it delegates to any class in the MRO.

Therefore you must be prepared to call any other class's method in the hierarchy and be prepared to be called from any other class's method.

The general rule is to pass all arguments you received on to the super function.  If classes can take differing arguments, accept *args and **kwargs.


Caveats
-------

Caution: There are some subtle differences with multiple inheritance.

You can use explicit calling to ensure that the 'right' method is called.


Two seminal articles
--------------------

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"Super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

(Both worth reading....)

Mix-ins
-------

So why would you want to do this? One reason:  *mixins*

Provides a subset of expected functionality in a re-usable package.

Huh? this is why --

Hierarchies are not always simple:

* Animal

  * Mammal

    * GiveBirth()

  * Bird

    * LayEggs()

Where do you put a Platypus?

Real World Example: `FloatCanvas`_

.. _FloatCanvas: https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L485

Composition
===========



Composition vs Inheritance
--------------------------

Composition does virtually the same thing as multiple inheritance, in the sense that it allows your class to reuse the functionality of other classes.

With inheritance you are thinking in terms of 'is-a' relationships.

With composition you are thinking in terms of 'has-a' relationships.

Composition is more explicit than inheritance and it avoids the complexity of super().  It of course also gains nothing from super()'s superpowers.


An example
----------

.. code-block:: python

    class Other(object):

        def __init__(self):
            print("Other __init__()")


    class MyComposedClass(object):
    """ I inherit from object """

        def __init__(self):
            self.other = Other()  # I contain Other()

Remember: 'has-a' not 'is-a'



Properties
==========

https://en.wikipedia.org/wiki/Property_%28programming%29#Python


Attributes are clear and concise
--------------------------------

.. rst-class:: left
.. container::

    One of the strengths of Python is lack of clutter.

    .. code-block:: ipython

        In [5]: class C:
                def __init__(self):
                        self.x = 5
        In [6]: c = C()
        In [7]: c.x
        Out[7]: 5
        In [8]: c.x = 8
        In [9]: c.x
        Out[9]: 8


And we want to maintain this clarity.

Getter and Setters
------------------

But what if you need to add behavior later?

.. rst-class:: build

* do some calculation
* check data validity
* keep things in sync


.. nextslide::

.. code-block:: ipython

    In [5]: class C:
       ...:     def __init__(self):
       ...:         self.x = 5
       ...:     def get_x(self):
       ...:         return self.x
       ...:     def set_x(self, x):
       ...:         self.x = x
       ...:
    In [6]: c = C()
    In [7]: c.get_x()
    Out[7]: 5
    In [8]: c.set_x(8)
    In [9]: c.get_x()
    Out[9]: 8


This is verbose -- `Java`_?

.. _Java: http://dirtsimple.org/2004/12/python-is-not-java.html

Properties
----------

.. code-block:: ipython

    class C:
        _x = None
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, value):
            self._x = value

    In [28]: c = C()
    In [30]: c.x = 5
    In [31]: print(c.x)
    5

Now the interface is like simple attribute access!

Decorators
----------

What's up with the "@" symbols?

Those are "decorations" it is a syntax for wrapping functions up with something special.

We will cover decorators in detail in another part of the program, but for now just copy the syntax.

.. code-block:: python

    @property
    def x(self):

means: make a property called x with this as the "getter".

.. code-block:: python

    @x.setter
    def x(self, value):

means: make the "setter" of the 'x' property this new function

Read Only Attributes
--------------------

You do not need to define a setter. If you don't, you get a "read only" attribute:

.. code-block:: ipython

    In [11]: class D():
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     @property
       ....:     def getx(self):
       ....:     """I am read only"""
       ....:         return self._x
       ....:
    In [12]: d = D()
    In [13]: d.x
    Out[13]: 5
    In [14]: d.x = 6
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-14-c83386d97be3> in <module>()
    ----> 1 d.x = 6
    AttributeError: can't set attribute

Deleters
---------

If you want to do something special when a property is deleted, you can define a deleter as well:

.. code-block:: ipython

    In [11]: class D():
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     @property
       ....:     def x(self):
       ....:         return self._x
       ....:     @x.deleter
       ....:     def x(self):
       ....:         del self._x

If you leave this out, the property can't be deleted, which is usually
what you want.

.. rst-class:: centered

[demo: :download:`properties_example.py <../../Examples/Session08/properties_example.py>`]

LAB: Properties, class methods, special methods
===============================================

Let's use some of this to build a nice class to represent a Circle.

For now, Let's do steps 1-4 of:

:ref:`exercise_circle_class`


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
-------------------------------

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

Code Structure, Modules, and Namespaces
=======================================

.. rst-class:: center large

How to get what you want when you want it.

Code Structure
--------------

In Python, the structure of your code is determined by whitespace.

How you *indent* your code determines how it is structured

::

    block statement:
        some code body
        some more code body
        another block statement:
            code body in
            that block

The colon that terminates a block statement is also important...

.. nextslide:: One-liners

You can put a one-liner after the colon:

.. code-block:: ipython

    In [167]: x = 12
    In [168]: if x > 4: print(x)
    12

But this should only be done if it makes your code **more** readable.


.. nextslide:: Spaces vs. Tabs

Whitespace is important in Python.

An indent *could* be:

* Any number of spaces
* A tab
* A mix of tabs and spaces:

If you want anyone to take you seriously as a Python developer:

.. rst-class:: centered

**Always use four spaces -- really!**

`(PEP 8)`_

.. _(PEP 8): http://legacy.python.org/dev/peps/pep-0008/


.. nextslide:: Spaces Elsewhere

Other than indenting -- space doesn't matter, technically.

.. code-block:: python

    x = 3*4+12/func(x,y,z)
    x = 3*4 + 12 /   func (x,   y, z)

But you should strive for proper style.  Read `PEP 8`_ and install a linter in
your editor.

.. _PEP 8: http://legacy.python.org/dev/peps/pep-0008/

Modules and Packages
--------------------

Python is all about *namespaces* --  the "dots"

``name.another_name``

The "dot" indicates that you are looking for a name in the *namespace* of the
given object. It could be:

* name in a module
* module in a package
* attribute of an object
* method of an object


.. nextslide:: Modules

A module is simply a namespace.

It might be a single file, or it could be a collection of files that define a
shared API.

To a first approximation, you can think of the files you write that end in
``.py`` as modules.

.. nextslide:: Packages

A package is a module with other modules in it.

On a filesystem, this is represented as a directory that contains one or more
``.py`` files, one of which **must** be called ``__init__.py``.

When you have a package, you can import the package, or any of the modules
inside it.

.. nextslide:: importing modules

.. code-block:: python

    import modulename
    from modulename import this, that
    import modulename as a_new_name
    from modulename import this as that


importing from packages
-----------------------

.. code-block:: python

    import packagename.modulename
    from packagename.modulename import this, that
    from package import modulename

http://effbot.org/zone/import-confusion.htm

.. nextslide::

.. code-block:: python

    from modulename import *

.. rst-class:: centered large

**Don't do this!**

import
------

When you import a module, or a symbol from a module, the Python code is
*compiled* to **bytecode**.

The result is a ``module.pyc`` file.

Then after compiling, all the code in the module is run **at the module scope**.

For this reason, it is good to avoid module-scope statements that have global
side-effects.

Re-import
----------

The code in a module is NOT re-run when imported again

It must be explicitly reloaded to be re-run

.. code-block:: python

    import modulename
    reload(modulename)

.. ifslides::

    .. rst-class:: centered

    (demo)


.. nextslide:: Running a Module

In addition to importing modules, you can run them.

There are a few ways to do this:

.. rst-class:: build

* ``$ python hello.py``   -- must be in current working directory
* ``$ python -m hello``   -- any module on PYTHONPATH anywhere on the system
* ``$ ./hello.py``        -- put ``#!/usr/env/python``  at top of module (Unix)
* ``In [149]: run hello.py``     -- at the IPython prompt -- running a module brings its names into the interactive namespace


.. nextslide:: Running a Module

Like importing, running a module executes all statements at the module level.

But there's an important difference.

When you *import* a module, the value of the symbol ``__name__`` in the module
is the same as the filename.

When you *run* a module, the value of the symbol ``__name__`` is ``__main__``.

This allows you to create blocks of code that are executed *only when you run a module*

.. code-block:: python

    if __name__ == '__main__':
        # Do something interesting here
        # It will only happen when the module is run

.. nextslide:: "main" blocks

This is useful in a number of cases.

You can put code here that lets your module be a utility *script*

You can put code here that demonstrates the functions contained in your module

You can put code here that proves that your module works.


Import Interactions
-------------------

Let's experiment with importing different ways:

.. code-block:: ipython

    In [3]: import math

    In [4]: math.<TAB>
    math.acos       math.degrees    math.fsum       math.pi
    math.acosh      math.e          math.gamma      math.pow
    math.asin       math.erf        math.hypot      math.radians
    math.asinh      math.erfc       math.isinf      math.sin
    math.atan       math.exp        math.isnan      math.sinh
    math.atan2      math.expm1      math.ldexp      math.sqrt
    math.atanh      math.fabs       math.lgamma     math.tan
    math.ceil       math.factorial  math.log        math.tanh
    math.copysign   math.floor      math.log10      math.trunc
    math.cos        math.fmod       math.log1p
    math.cosh       math.frexp      math.modf

.. nextslide::

.. code-block:: ipython

    In [6]: math.sqrt(4)
    Out[6]: 2.0
    In [7]: import math as m
    In [8]: m.sqrt(4)
    Out[8]: 2.0
    In [9]: from math import sqrt
    In [10]: sqrt(4)
    Out[10]: 2.0


.. nextslide::

Experiment with importing different ways:

.. code-block:: python

    import sys
    print sys.path
    import os
    print os.path

You wouldn't want to import * those!

  -- check out

.. code-block:: python

    os.path.split('/foo/bar/baz.txt')
    os.path.join('/foo/bar', 'baz.txt')

Review framing questions
========================


Homework
========

.. rst-class:: left

  Complete the Circle class

  Complete the Sparse Array class

  Decide what you are going to do for your project, and send me a simple proposal. Get started if you can.

  Good book:

  Python 3 Object Oriented Programming: *Dusty Phillips*

  (Dusty is a local boy and co-founder of PuPPy)


Readings
========
