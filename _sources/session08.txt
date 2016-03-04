

.. include:: include.rst


Session Eight: Object Oriented Programming 2
********************************************

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

Multiple inheritance: Inheriting from more than one class.

Simply provide more than one parent.

.. code-block:: python

    class Combined(Parent1, Parent2, Parent3):
        def __init__(self, something, something else):
            # some custom initialization here.
            Parent1.__init__(self, ......)
            Parent2.__init__(self, ......)
            Parent3.__init__(self, ......)
            # possibly more custom initialization

Calls to the parent class ``__init__``  are optional and case dependent.



Purpose
-------

What was the purpose behind inheritance?  

Code reuse.


What is the purpose behind multiple inheritance?  

Code reuse.


What wasn't the purpose of inheritance?

Building massive class hierarchies for their own sake.


What isn't the purpose of multiple inheritance?

Building massive class hierarchies for their own sake.


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


Two seminal articles
--------------------

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"Super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

(Both worth reading....)

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


Review framing questions
========================


Homework
========

Complete the Circle class

Complete the Sparse Array class

Refactor mailroom to use classes.



Readings
========

Python 3 Object Oriented Programming: *Dusty Phillips*

(Dusty is a local boy and co-founder of PuPPy)
