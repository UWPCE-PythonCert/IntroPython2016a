

.. include:: include.rst

Session Seven: Object Oriented Programming
******************************************


Announcements
=============

Review & Questions
==================

Homework Review
===============

Code review -- let's take a look.



Homework Review: Trapezoid
--------------------------

Did you all get a trapedzoidal rule function working?

Anyone get the "passing through of arguments"?

How about the adaptive solutions?

Notes on Floating point
-----------------------

Did anyone look at the isclose() function?

How to make a range of numbers in floating point?

Anyone do something like this?:

.. code-block:: python

  s = []
  x = a
  while x <= b:
      s.append(x)
      x += delta_x

  -- see my solution.

Some notes about FP issues:

https://docs.python.org/3.5/tutorial/floatingpoint.html


Lightning Talks
===============

| |lightning-session07a|
| |lightning-session07b|
| |lightning-session07c|
| |lightning-session07d|
| |lightning-session07e|
|

Framing
=======

In the Beginning there was the GOTO.

And in fact, there wasn't even that.



Programming Paradigms
=====================

https://en.wikipedia.org/wiki/Programming_paradigm



Software Design
---------------

Good software design is about code re-use, clean separation of concerns,
refactorability, testability, etc...

OO can help with all that, but:
  * It doesn't guarantee it
  * It can get in the way

What is Object Oriented Programming?

|
    "Objects can be thought of as wrapping their data
    within a set of functions designed to ensure that
    the data are used appropriately, and to assist in
    that use"

|

http://en.wikipedia.org/wiki/Object-oriented_programming


.. nextslide::

Even simpler:

"Objects are data and the functions that act on them in one place."

This is the core of "encapsulation"


The Dominant Model
------------------

OO is the dominant model for the past couple decades, but it is not the only model, and languages such as Python increasingly mix and blend among models.

Object Oriented Concepts
------------------------

.. rst-class:: medium centered

.. container::

  Classes

  Instances or Objects

  Encapsulation

  Class and instance attributes

  Subclassing

  Overriding methods

  Operator Overloading

  Polymorphism

  Dynamic Dispatch

  

  

Definitions
-----------

class
  A category of objects: particular data and behavior: A "circle" (same as a type in python)

instance
  A particular object of a class: a specific circle

object
  The general case of a instance -- really any value (in Python anyway)

attribute
  Something that belongs to an object (or class): generally thought of
  as a variable, or single object, as opposed to a ...

method
  A function that belongs to a class

Python and OO
-------------

Is Python a "True" Object-Oriented Language?

What are its strengths and weaknesses vis-a-vis OO?

It does not support full encapsulation, i.e., it does not require classes,  etc.


.. nextslide::

Folks can't even agree on what OO "really" means

See: The Quarks of Object-Oriented Development

  - Deborah J. Armstrong

http://agp.hx0.ru/oop/quarks.pdf


.. nextslide::

Think in terms of what makes sense for your project
 -- not any one paradigm of software design.


.. nextslide::

OO Buzzwords

  * data abstraction
  * encapsulation
  * modularity
  * polymorphism
  * inheritance

Python provides for all of this, though it doesn't enforce or require any of it.

Python's roots
--------------

|  C
|  C with Classes (aka C++)
|  Modula2
|


You can do OO in C
------------------

Which today is not considered an OO Language.

See the GTK+ project.

OO languages give you some handy tools to make it easier (and safer):

  * polymorphism (duck typing gives you this)
  * inheritance

You will need to understand OO
------------------------------

- It's a good idea for a lot of problems

- You'll need to work with OO packages

(Even a fair bit of the standard library is Object Oriented)

Python Classes
==============


.. rst-class:: left

    The ``class``  statement

    ``class``  creates a new type object:

    .. code-block:: ipython

        In [4]: class C:
            pass
           ...:
        In [5]: type(C)
        Out[5]: type

    A class is a type -- interesting!

    It is created when the statement is run -- much like ``def``

A simple class

About the simplest class you can write

.. code-block:: python

    >>> class Point:
    ...     x = 1
    ...     y = 2
    >>> Point
    <class __main__.Point at 0x2bf928>
    >>> Point.x
    1
    >>> p = Point()
    >>> p
    <__main__.Point instance at 0x2de918>
    >>> p.x
    1

Basic Structure of a class
--------------------------

.. code-block:: python

    class Point:
    # everything defined in here is in the class namespace

        def __init__(self, x, y):
            self.x = x
            self.y = y

    ## create an instance of the class
    p = Point(3,4)

    ## access the attributes
    print("p.x is:", p.x)
    print("p.y is:", p.y)


see: ``Examples/Session07/simple_classes.py``

The Initializer
---------------

The ``__init__``  special method is called when a new instance of a class is created.

You can use it to do any set-up you need

.. code-block:: python

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


It gets the arguments passed when you call the class object:

.. code-block:: python

    Point(x, y)

Self
----

What is this ``self`` thing?

The instance of the class is passed as the first parameter for every method.

"``self``" is only a convention -- but you DO want to use it.

.. code-block:: python

    class Point:
        def a_function(self, x, y):
    ...

Does this look familiar from C-style procedural programming?


.. nextslide::

Anything assigned to a ``self.``  attribute is kept in the instance
name space -- ``self`` *is* the instance.

That's where all the instance-specific data is.

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        def __init__(self, x, y):
            self.x = x
            self.y = y

Class Attributes
----------------

Anything assigned in the class scope is a class attribute -- every
instance of the class shares the same one.

Note: the methods defined by ``def`` are class attributes as well.

The class is one namespace, the instance is another.

.. code-block:: python

    class Point:
        size = 4
        color= "red"
    ...
        def get_color():
            return self.color
    >>> p3.get_color()
     'red'

class attributes are accessed with ``self``  also.


Typical methods
---------------

.. code-block:: python

    class Circle:
        color = "red"

        def __init__(self, diameter):
            self.diameter = diameter

        def grow(self, factor=2):
            self.diameter = self.diameter * factor


Methods take some parameters, manipulate the attributes in ``self``.

They may or may not return something useful.


Arity Gotcha
------------

.. code-block:: python

    ...
        def grow(self, factor=2):
            self.diameter = self.diameter * factor
    ...
    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

Huh???? I only gave 2

``self`` is implicitly passed in for you by python.

Functions (methods) are First Class
-----------------------------------

.. rst-class:: center

    Note that in python, functions are first class objects, so a method *is* an attribute


LAB: Classes
------------

Let's say you need to render some html...

The goal is to build a set of classes that render an html
page.

We'll start with a single class, then add some sub-classes
to specialize the behavior

Details in:

:ref:`exercise_html_renderer`

Do Step 1. in class and then wait to do the rest until after discussing Subclassing and Inheritance.



Subclassing & Inheritance
=========================

Inheritance
-----------

In object-oriented programming (OOP), inheritance is a way to reuse code
of existing objects, or to establish a subtype from an existing object.

Objects are defined by classes, classes can inherit attributes and behavior
from pre-existing classes called base classes or super classes.

The resulting classes are known as derived classes or subclasses.

(http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29)

Subclassing
-----------

A subclass "inherits" all the attributes (methods, etc) of the parent class.

You can then change ("override") some or all of the attributes to change the behavior.

You can also add new attributes to extend the behavior.

The simplest subclass in Python:

.. code-block:: python

    class A_subclass(The_superclass):
        pass

``A_subclass``  now has exactly the same behavior as ``The_superclass``

Overriding attributes
---------------------

Overriding is as simple as creating a new attribute with the same name:

.. code-block:: python

    class Circle:
        color = "red"

    ...

    class NewCircle(Circle):
        color = "blue"
    >>> nc = NewCircle
    >>> print(nc.color)
    blue


all the ``self``  instances will have the new attribute.

Overriding methods
------------------

Same thing, but with methods (remember, a method *is* an attribute in python)

.. code-block:: python

    class Circle:
    ...
        def grow(self, factor=2):
            """grows the circle's diameter by factor"""
            self.diameter = self.diameter * factor
    ...

    class NewCircle(Circle):
    ...
        def grow(self, factor=2):
            """grows the area by factor..."""
            self.diameter = self.diameter * math.sqrt(2)


all the instances will have the new method

.. nextslide::

Here's a program design suggestion:

Whenever you override a method, the interface of the new method should be the same as the old.  It should take the same parameters, return the same type, and obey the same preconditions and postconditions.

If you obey this rule, you will find that any function designed to work with an instance of a superclass, like a Deck, will also work with instances of subclasses like a Hand or PokerHand.  If you violate this rule, your code will collapse like (sorry) a house of cards.


More on Subclassing
===================

Overriding \_\_init\_\_
-----------------------

``__init__`` common method to override

You often need to call the super class ``__init__``  as well

.. code-block:: python

    class Circle:
        color = "red"
        def __init__(self, diameter):
            self.diameter = diameter
    ...
    class CircleR(Circle):
        def __init__(self, radius):
            diameter = radius*2
            Circle.__init__(self, diameter)


exception to: "don't change the method signature" rule.

More subclassing
----------------

You can also call the superclass' other methods:

.. code-block:: python

    class Circle:
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2


    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)

There is nothing special about ``__init__``  except that it gets called
automatically when you instantiate an instance.

When to Subclass
----------------

"Is a" relationship: Subclass/inheritance

"Has a" relationship: Composition

.. nextslide::

"Is a" vs "Has a"

You may have a class that needs to accumulate an arbitrary number of objects.

A list can do that -- so should you subclass list?

Ask yourself:

-- **Is** your class a list (with some extra functionality)?

or

-- Does you class **have** a list?

You only want to subclass list if your class could be used anywhere a list can be used.

Attribute resolution order
--------------------------

When you access an attribute:

``an_instance.something``

Python looks for it in this order:

  * Is it an instance attribute ?
  * Is it a class attribute ?
  * Is it a superclass attribute ?
  * Is it a super-superclass attribute ?
  * ...


It can get more complicated...

https://www.python.org/download/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html

What are Python classes, really?
--------------------------------

Putting aside the OO theory...

Python classes are:

  * Namespaces

    * One for the class object
    * One for each instance

  * Attribute resolution order
  * Auto tacking-on of ``self`` when methods are called


That's about it -- really!

Type-Based dispatch
-------------------

You'll see code that looks like this:

.. code-block:: python

      if isinstance(other, A_Class):
          Do_something_with_other
      else:
          Do_something_else


Usually better to use "duck typing" (polymorphism)

But when it's called for:

    * ``isinstance()``
    * ``issubclass()``

.. nextslide::

GvR: "Five Minute Multi- methods in Python":

http://www.artima.com/weblogs/viewpost.jsp?thread=101605

https://www.python.org/download/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html

LAB: Subclassing & Inheritance
------------------------------

.. rst-class:: left medium

    * html renderer: let's see how much more we can do!

:ref:`exercise_html_renderer`


Now we have a base class, and we can:

* Subclass overriding class attributes
* Subclass overriding a method
* Subclass overriding the ``__init__``

These are the core OO approaches

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

``super()``
-----------

``super()``: use it to call a superclass method, rather than explicitly calling
the unbound method on the superclass.

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

.. nextslide:: Caveats

Caution: There are some subtle differences with multiple inheritance.

You can use explicit calling to ensure that the 'right' method is called.

.. rst-class:: medium

    **Background**

Two seminal articles about ``super()``:

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

(Both worth reading....)

Mix-ins
-------

So why would you want to do this? One reason:  *mixins*

Provides an subset of expected functionality in a re-usable package.

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

Subclassing vs Composition
==========================


Composition
-----------



Review framing questions
========================

Think about OO in Python:

Think about what makes sense for your code:

* Code re-use
* Clean APIs
* ...

Don't be a slave to what OO is *supposed* to look like.

Let OO work for you, not *create* work for you


Homework
========

Complete labs.


Readings
========


The Art of Subclassing
----------------------

The Art of Subclassing by *Raymond Hettinger*

http://pyvideo.org/video/879/the-art-of-subclassing

The most salient points from that video are as follows:

* **Subclassing is not for Specialization**

* **Classes and subclassing are for code re-use -- not creating taxonomies**

* **Bear in mind that the subclass is in charge**


Stop Writing Classes
--------------------

Stop Writing Classes by *Jack Diederich*

http://pyvideo.org/video/880/stop-writing-classes

"If your class has only two methods -- and one of them is ``__init__``
-- you don't need a class"


Python Class Toolkit
--------------------

Python Class Toolkit by *Raymond Hettinger*

https://youtu.be/HTLu2DFOdTg

https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger

