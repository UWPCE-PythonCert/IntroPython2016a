.. include:: include.rst

*************************************************
Session Five: Exceptions, Testing, Comprehensions
*************************************************


=============
Announcements
=============



================
Review/Questions
================


Homework
--------

Let's take a look.


================
Topics for Today
================



Lightning Talks
---------------------

.. rst-class:: medium




Review of Previous Class
------------------------

  * Dictionaries
  * Sets
  * File processing, etc.

.. nextslide::

.. rst-class:: center large

  How many of you finished ALL the homework?

.. nextslide::

.. rst-class:: center large

  Sorry about that!

.. nextslide::

.. rst-class:: medium

    * That was a lot.

.. rst-class:: medium

.. rst-class:: build

    * But it's all good stuff.

    * I'll take time to go over it in class.



=====================
Dictionaries and Sets
=====================

Dictionary
----------
Python calls it a ``dict``

Other languages call it:

  * dictionary
  * associative array
  * map
  * hash table
  * hash
  * key-value pair


Dictionary Constructors
-----------------------
.. code-block:: python

    >>> {'key1': 3, 'key2': 5}
    {'key1': 3, 'key2': 5}

    >>> dict([('key1', 3),('key2', 5)])
    {'key1': 3, 'key2': 5}

    >>> dict(key1=3, key2= 5)
    {'key1': 3, 'key2': 5}

    >>> d = {}
    >>> d['key1'] = 3
    >>> d['key2'] = 5
    >>> d
    {'key1': 3, 'key2': 5}

Dictionary Indexing
-------------------
::

    >>> d = {'name': 'Brian', 'score': 42}

    >>> d['score']
    42

    >>> d = {1: 'one', 0: 'zero'}

    >>> d[0]
    'zero'

    >>> d['non-existing key']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'non-existing key'


.. nextslide::

Keys can be any immutable:

  * number
  * string
  * tuple

.. code-block:: ipython

    In [325]: d[3] = 'string'
    In [326]: d[3.14] = 'pi'
    In [327]: d['pi'] = 3.14
    In [328]: d[ (1,2,3) ] = 'a tuple key'
    In [329]: d[ [1,2,3] ] = 'a list key'
       TypeError: unhashable type: 'list'


Actually -- any "hashable" type.


.. nextslide:: Hashing

Hash functions convert arbitrarily large data to a small proxy (usually int)

Always return the same proxy for the same input

MD5, SHA, etc

Dictionaries hash the key to an integer proxy and use it to find the key and value.

Key lookup is efficient because the hash function leads directly to a bucket with very few keys (often just one)

What would happen if the proxy changed after storing a key?

Hashability requires immutability

Key lookup is very efficient

Same average time regardless of size


.. nextslide:: Dictionary indexing


Note: Python name look-ups are implemented with dict -- it's highly optimized

Key to value:

 * lookup is one way

Value to key:

 * requires visiting the whole dict

If you need to check dict values often, create another dict or set

(up to you to keep them in sync)


Dictionary Ordering (not)
-------------------------


Dictionaries have no defined order

.. code-block:: ipython

    In [352]: d = {'one':1, 'two':2, 'three':3}
    In [353]: d
    Out[353]: {'one': 1, 'three': 3, 'two': 2}
    In [354]: d.keys()
    Out[354]: dict_keys(['three', 'two', 'one'])

Dictionary Iterating
--------------------

``for``  iterates over the keys

.. code-block:: ipython

    In [15]: d = {'name': 'Brian', 'score': 42}

    In [16]: for x in d:
        print(x)
       ....:
    score
    name


(note the different order...)

dict keys and values
--------------------

.. code-block:: ipython

    In [20]: d = {'name': 'Brian', 'score': 42}

    In [21]: d.keys()
    Out[21]: dict_keys(['score', 'name'])

    In [22]: d.values()
    Out[22]: dict_values([42, 'Brian'])

    In [23]: d.items()
    Out[23]: dict_items([('score', 42), ('name', 'Brian')])


dict keys and values
--------------------

Iterating on everything

.. code-block:: ipython

    In [26]: d = {'name': 'Brian', 'score': 42}

    In [27]: for k, v in d.items():
        print("%s: %s" % (k,v))
       ....:
    score: 42
    name: Brian


Dictionary Performance
-----------------------

  * indexing is fast and constant time: O(1)

  * ``x in s`` constant time: O(1)

  * visiting all is proportional to n: O(n)

  * inserting is constant time: O(1)

  * deleting is constant time: O(1)


 http://wiki.python.org/moin/TimeComplexity


Other dict operations:
----------------------

See them all here:

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

Is it in there?

.. code-block:: ipython

  In [5]: d
  Out[5]: {'that': 7, 'this': 5}

  In [6]: 'that' in d
  Out[6]: True

  In [7]: 'this' not in d
  Out[7]: False

Containment is on the keys.

.. nextslide::

Getting something: (like indexing)

.. code-block:: ipython

  In [9]: d.get('this')
  Out[9]: 5

But you can specify a default

.. code-block:: ipython

  In [11]: d.get('something', 'a default')
  Out[11]: 'a default'

Never raises an Exception (default default is None)

.. nextslide::

iterating

.. code-block:: ipython

  In [13]: for item in d:
     ....:     print(item)
     ....:
  this
  that

which is equivalent to, but faster than:

.. code-block:: ipython

  In [15]: for key in d.keys():
      print(key)
     ....:
  this
  that

.. nextslide::

but to get values, must specify you want values:

.. code-block:: ipython

  In [16]: for val in d.values():
      print(val)
     ....:
  5
  7


.. nextslide::

"Popping": getting the value while removing it

pop out a particular key

.. code-block:: ipython

  In [19]: d.pop('this')
  Out[19]: 5

  In [20]: d
  Out[20]: {'that': 7}

pop out an arbitrary key, value pair

.. code-block:: ipython

  In [23]: d.popitem()
  Out[23]: ('that', 7)

  In [24]: d
  Out[24]: {}

.. nextslide::

This one is handy:

``setdefault(key[, default])``

gets the value if it's there, sets it if it's not

.. code-block:: ipython

  In [27]: d.setdefault('something', 'a value')
  Out[27]: 'a value'

  In [28]: d
  Out[28]: {'something': 'a value'}


.. nextslide::

Assignment maintains link to the original dict

.. code-block:: ipython

  In [47]: d
  Out[47]: {'something': 'a value'}

  In [48]: item_view = d

  In [49]: d['something else'] = 'another value'

  In [50]: item_view
  Out[50]: {'something': 'a value', 'something else': 'another value'}


.. nextslide::

Use explicit copy method to get a copy

.. code-block:: ipython

  In [51] item_copy = d.copy()

  In [52]: d['another thing'] = 'different value'

  In [53]: d
  Out[53]:
  {'another thing': 'different value',
   'something': 'a value',
   'something else': 'another value'}

   In [54]: item_copy
   Out[54]: {'something': 'a value', 'something else': 'another value'}


Sets
-----

``set``  is an unordered collection of distinct values

Essentially a dict with only keys

Set Constructors

.. code-block:: ipython

    >>> set()
    set()

    >>> set([1, 2, 3])
    {1, 2, 3}

    >>> {1, 2, 3}
    {1, 2, 3}

    >>> s = set()

    >>> s.update([1, 2, 3])
    >>> s
    {1, 2, 3}


Set Properties
---------------

``Set``  members must be hashable

Like dictionary keys -- and for same reason (efficient lookup)

No indexing (unordered)

.. code-block:: ipython

    >>> s[1]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing


Set Methods
-----------

.. code-block:: ipython

    >> s = set([1])
    >>> s.pop() # an arbitrary member
    1
    >>> s.pop()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'pop from an empty set'
    >>> s = set([1, 2, 3])
    >>> s.remove(2)
    >>> s.remove(2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 2

.. nextslide::

All the "set" operations from math class...

.. code-block:: python

    s.isdisjoint(other)

    s.issubset(other)

    s.union(other, ...)

    s.intersection(other, ...)

    s.difference(other, ...)

    s.symmetric_difference( other, ...)

Frozen Set
----------

Another kind of set: ``frozenset``

immutable -- for use as a key in a dict
(or another set...)

.. code-block:: python

    >>> fs = frozenset((3,8,5))
    >>> fs.add(9)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'frozenset' object has no attribute 'add'


LAB: Dictionaries and Sets lab
==============================

Have some fun with dictionaries and sets!

:ref:`exercise_dict_lab`


Lightning Talk
--------------

|
| 
|


========================
File Reading and Writing
========================

Files
-----

Text Files

.. code-block:: python

    f = open('secrets.txt')
    secret_data = f.read()
    f.close()

``secret_data`` is a string

NOTE: these days, you probably need to use Unicode for text -- we'll get to that next week

.. nextslide::

Binary Files

.. code-block:: python

    f = open('secrets.bin', 'rb')
    secret_data = f.read()
    f.close()

``secret_data`` is a byte string

(with arbitrary bytes in it -- well, not arbitrary -- whatever is in the file.)

(See the ``struct``  module to unpack binary data )


.. nextslide::


File Opening Modes

.. code-block:: python

    f = open('secrets.txt', [mode])
    'r', 'w', 'a'
    'rb', 'wb', 'ab'
    r+, w+, a+
    r+b, w+b, a+b


These follow the Unix conventions, and aren't all that well documented
in the Python docs. But these BSD docs make it pretty clear:

http://www.manpagez.com/man/3/fopen/

**Gotcha** -- 'w' modes always clear the file

.. nextslide:: Text File Notes

Text is default

  * Newlines are translated: ``\r\n -> \n``
  *   -- reading and writing!
  * Use \*nix-style in your code: ``\n``


Gotcha:

  * no difference between text and binary on \*nix
  * breaks on Windows


File Reading
------------

Reading part of a file

.. code-block:: python

    header_size = 4096
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

.. nextslide::


Common Idioms

.. code-block:: python

    for line in open('secrets.txt'):
        print(line)

(the file object is an iterator!)

.. code-block:: python

    f = open('secrets.txt')
    while True:
        line = f.readline()
        if not line:
            break
        do_something_with_line()

.. nextslide::

We will learn more about the keyword with later, but for now, just understand
the syntax and the advantage over the try-finally block:

.. code-block:: python

 with open('workfile', 'r') as f:
     read_data = f.read()
 f.closed
 True


File Writing
------------

.. code-block:: python

    outfile = open('output.txt', 'w')
    for i in range(10):
        outfile.write("this is line: %i\n"%i)
    outfile.close()

    with open('output.txt', 'w'):
        for i in range(10):
           f.write("this is line: %i\n"%i)


File Methods
------------

Commonly Used Methods

.. code-block:: python

    f.read() f.readline()  f.readlines()

    f.write(str) f.writelines(seq)

    f.seek(offset)   f.tell() # for binary files, mostly

    f.close()

StringIO
--------

.. code-block:: python

    In [417]: import io
    In [420]: f = io.StringIO()
    In [421]: f.write("somestuff")
    In [422]: f.seek(0)
    In [423]: f.read()
    Out[423]: 'somestuff'
    Out[424]: stuff = f.getvalue()
    Out[425]: f.close()

(handy for testing file handling code...)

There is also cStringIO -- a bit faster.

.. code-block:: python

    from cStringIO import StringIO

=====================
Paths and Directories
=====================

Paths
-----

Paths are generally handled with simple strings (or Unicode strings)

Relative paths:

.. code-block:: python

    'secret.txt'
    './secret.txt'

Absolute paths:

.. code-block:: python

    '/home/chris/secret.txt'


Either work with ``open()`` , etc.

(working directory only makes sense with command-line programs...)

os module
----------

.. code-block:: python

    os.getcwd()
    os.chdir(path)
    os.path.abspath()
    os.path.relpath()


.. nextslide:: os.path module

.. code-block:: python

    os.path.split()
    os.path.splitext()
    os.path.basename()
    os.path.dirname()
    os.path.join()


(all platform independent)

.. nextslide:: directories

.. code-block:: python

    os.listdir()
    os.mkdir()
    os.walk()

(higher level stuff in ``shutil``  module)

pathlib
-------

``pathlib`` is a package for handling paths in an OO way:

http://pathlib.readthedocs.org/en/pep428/

All the stuff in os.path and more:

.. code-block:: ipython

    In [64]: import pathlib
    In [65]: pth = pathlib.Path('./')
    In [66]: pth.is_dir()
    Out[66]: True
    In [67]: pth.absolute()
    Out[67]: PosixPath('/Users/Chris/PythonStuff/UWPCE/IntroPython2015')
    In [68]: for f in pth.iterdir():
                 print(f)
    junk2.txt
    junkfile.txt
    ...

===
LAB
===

Files Lab: If there is time.

Files Lab
---------

In the class repo, in:

``Examples\students.txt``

You will find the list I generated of all the students in the class, and
what programming languages they have used in the past.

Write a little script that reads that file, and generates a list of all
the languages that have been used.

Extra credit: keep track of how many students specified each language.

If you've got git set up right, ``git pull upstream master`` should update
your repo. Otherwise, you can get it from gitHub:

``https://github.com/UWPCE-PythonCert/IntroPython2015/blob/master/Examples/students.txt``



Homework review
---------------

Homework Questions?

My Solutions to all the exercises in the class repo in:

``Solutions/Session04``

A few tidbits ....

Sorting stuff in dictionaries:
-------------------------------

dicts aren't sorted, so what if you want to do something in a sorted way?

The "standard" way:

.. code-block:: python

  for key in sorted(d.keys()):
      ...

Other options:

.. code-block:: python

    collections.OrderedDict

Also other nifty stuff in the ``collections`` module:

https://docs.python.org/3.5/library/collections.html


PEP 8 reminder
--------------

PEP 8 (Python Enhancement Proposal 8): https://www.python.org/dev/peps/pep-0008/

Is the "official" style guide for Python code.

Strictly speaking, you only need to follow it for code in the standard library.

But style matters -- consistent style makes your code easier to read and understand.

So **follow PEP 8**

*Exception* -- if you have a company style guide follow that instead.

try the "pep8" module on your code::

  $ python3 -m pip install pep8
  $ pep8 my_python_file

(demo)

Naming things...
----------------

It matters what names you give your variables.

Python has rules about what it *allows*

PEP8 has rules for style: capitalization, and underscores and all that.

But you still get to decide within those rules.

So use names that make sense to the reader.

Naming Guidelines
-----------------

Only use single-letter names for things with limited scope: indexes and teh like:

.. code-block:: python

    for i, item in enumerate(a_sequence):
        do_something(i, item)

**Don't** use a name like "item", when there is a meaning to what the item is:

.. code-block:: python

    for name in all_the_names:
        do_something_with(name)

Use plurals for collections of things:

.. code-block:: python

    names = ['Fred', 'George', ...]

.. nextslide::

**Do** re-use names when the use is essentially the same, and you don't need the old one:

.. code-block:: python

    line = line.strip()
    line = line.replace(",", " ")
    ....

Here's a nice talk about naming:

http://pyvideo.org/video/3792/name-things-once-0


Code Review
------------

.. rst-class:: center medium

Anyone stuck or confused that's willing to volunteer for a live code review?

My Solutions
-------------

Anyone look at my solutions?

(yeah, not much time for that...)

Anything in particular you'd like me to go over?

==========
Exceptions
==========

A really nifty python feature -- really handy!

Exceptions
----------

Another Branching structure:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")

Exceptions
----------
Never Do this:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except:
        print "couldn't open missing.txt"


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

===
LAB
===

Exceptions Lab:

A number of you already did this -- so do it at home if you haven't

:ref:`exercise_exceptions_lab`


Lightning Talks
----------------

.. rst-class:: medium




============================
List and Dict Comprehensions
============================

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

(demo)

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


(demo)

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




=======
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

* ... (many frameworks supply their own test runners)

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

[demo]

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

===
LAB
===

Pick an example from codingbat:

``http://codingbat.com``

Do a bit of test-driven development on it:

 * run something on the web site.
 * write a few tests using the examples from the site.
 * then write the function, and fix it 'till it passes the tests.

Do at least two of these...

=========
Homework
=========

Catch up!
---------


* Finish the LABs from today
  - Exceptions lab

* Catch up from last week.

  - Add Exception handling to mailroom
  - and add some tests
  - and list (and dict, and set) comprehensions...

* If you've done all that -- check out the collections module:

  - https://docs.python.org/3.5/library/collections.html
  - here's a good overview: https://pymotw.com/3/collections/


Paths and File Processing
--------------------------

* write a program which prints the full path to all files in the current
  directory, one per line

* write a program which copies a file from a source, to a destination
  (without using shutil, or the OS copy command)

  - advanced: make it work for any size file: i.e. don't read the entire
    contents of the file into memory at once.

  - Note that if you want it to do any kind of file, you need to open the files in binary mode:
    ``open(filename, 'rb')`` (or ``'wb'`` for writing.)

* update mailroom from last week to:

  - Use dicts where appropriate
  - Write a full set of letters to everyone to individual files on disk
  - See if you can use a dict to switch between the users selections
  - Try to use a dict and the .format() method to do the letter as one
    big template -- rather than building up a big string in parts.


====================================
Material to review before next week:
====================================

 * Dive into Python3: 7.2 -- 7.3
   http://www.diveintopython3.net/iterators.html#defining-classes

 * Think Pyhton: 15 -- 18
   http://www.greenteapress.com/thinkpython/html/thinkpython016.html

 * LPTHW: 40 -- 44
   http://learnpythonthehardway.org/book/ex40.html

[note that in py3 you dont need to inherit from object]

Talk by Raymond Hettinger:

https://youtu.be/HTLu2DFOdTg

https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger
