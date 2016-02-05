.. include:: include.rst

*************************************************
Session Five: Strings, Files, Exceptions, Testing
*************************************************


Announcements
=============

Review & Questions
==================

Homework
========

Code review -- let's take a look.


Lightening talks
================

Today’s lightening talks will be from:





Strings
=======

.. rst-class:: left

Quick review: a string literal creates a string type:

.. code-block:: python

    "this is a string"

    'So is this'

    "And maybe y'all need something like this!"

    """and this also"""

.. rst-class:: left

You can also use ``str()``

.. code-block:: ipython

    In [256]: str(34)
    Out[256]: '34'

String Manipulation
-------------------

``split`` and ``join``:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']
    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'

Case Switching
--------------

.. code-block:: ipython

    In [171]: sample = 'A long string of words'
    In [172]: sample.upper()
    Out[172]: 'A LONG STRING OF WORDS'
    In [173]: sample.lower()
    Out[173]: 'a long string of words'
    In [174]: sample.swapcase()
    Out[174]: 'a LONG STRING OF WORDS'
    In [175]: sample.title()
    Out[175]: 'A Long String Of Words'

Testing
-------

.. code-block:: ipython

    In [181]: number = "12345"
    In [182]: number.isnumeric()
    Out[182]: True
    In [183]: number.isalnum()
    Out[183]: True
    In [184]: number.isalpha()
    Out[184]: False
    In [185]: fancy = "Th!$ $tr!ng h@$ $ymb0l$"
    In [186]: fancy.isalnum()
    Out[186]: False

String Literals
-----------------

Common Escape Sequences::

    \\  Backslash (\)
    \a  ASCII Bell (BEL)
    \b  ASCII Backspace (BS)
    \n  ASCII Linefeed (LF)
    \r  ASCII Carriage Return (CR)
    \t  ASCII Horizontal Tab (TAB)
    \ooo  Character with octal value ooo
    \xhh  Character with hex value hh

for example -- for tab-separted values:

.. code-block:: ipython

    In [25]: s = "these\tare\tseparated\tby\ttabs"

    In [26]: print(s)
    these   are separated    by  tabs

https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
https://docs.python.org/3/library/stdtypes.html#string-methods

Raw Strings
------------

Add an ``r`` in front of the string literal:

Escape Sequences Ignored

.. code-block:: ipython

    In [408]: print("this\nthat")
    this
    that
    In [409]: print(r"this\nthat")
    this\nthat

**Gotcha**

.. code-block:: ipython

    In [415]: r"\"
    SyntaxError: EOL while scanning string literal

(handy for regex, windows paths...)

Ordinal values
--------------

Characters in strings are stored as numeric values:

* "ASCII" values: 1-127

* Unicode values -- 1 - 1,114,111 (!!!)

To get the value:

.. code-block:: ipython

    In [109]: for i in 'Chris':
       .....:     print(ord(i), end=' ')
    67 104 114 105 115
    In [110]: for i in (67,104,114,105,115):
       .....:     print(chr(i), end='')
    Chris

(these days, stick with ASCII, or use full Unicode: more on that in a few weeks)

Building Strings
----------------

You can, but please don't do this:

.. code-block:: python

    'Hello ' + name + '!'

(I know -- we did that in the grid_printing excercise)

Do this instead:

.. code-block:: python

    'Hello {}!'.format(name)

It's much faster and safer, and easier to modify as code gets complicated.

https://docs.python.org/3/library/string.html#string-formatting

Old and New string formatting
-----------------------------

back in early python days, there was the string formatting operator: ``%``

.. code-block:: python

    " a string: %s and a number: %i "%("text", 45)

This is very similar to C-style string formatting (`sprintf`).

It's still around, and handy --- but ...

The "new" ``format()`` method is more powerful and flexible, so we'll focus on that in this class.

.. nextslide:: String Formatting

The string ``format()`` method:

.. code-block:: ipython

    In [62]: "A decimal integer is: {:d}".format(34)
    Out[62]: 'A decimal integer is: 34'

    In [63]: "a floating point is: {:f}".format(34.5)
    Out[63]: 'a floating point is: 34.500000'

    In [64]: "a string is the default: {}".format("anything")
    Out[64]: 'a string is the default: anything'

Multiple placeholders
---------------------

.. code-block:: ipython

    In [65]: "the number is {} is {}".format('five', 5)
    Out[65]: 'the number is five is 5'

    In [66]: "the first 3 numbers are {}, {}, {}".format(1,2,3)
    Out[66]: 'the first 3 numbers are 1, 2, 3'

The counts must agree:

.. code-block:: ipython

    In [67]: "string with {} formatting {}".format(1)
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-67-a079bc472aca> in <module>()
    ----> 1 "string with {} formatting {}".format(1)

    IndexError: tuple index out of range

Named placeholders
------------------

.. code-block:: ipython


    In [69]: "Hello, {name}, whaddaya know?".format(name="Joe")
    Out[69]: 'Hello, Joe, whaddaya know?'

You can use values more than once, and skip values:

.. code-block:: ipython

    In [73]: "Hi, {name}. Howzit, {name}?".format(name='Bob')
    Out[73]: 'Hi, Bob. Howzit, Bob?'

.. nextslide::

The format operator works with string variables, too:

.. code-block:: ipython

    In [80]: s = "{:d} / {:d} = {:f}"

    In [81]: a, b = 12, 3

    In [82]: s.format(a, b, a/b)
    Out[82]: '12 / 3 = 4.000000'

So you can dynamically build a format string

Complex Formatting
------------------

There is a complete syntax for specifying all sorts of options.

It's well worth your while to spend some time getting to know this
`formatting language`_. You can accomplish a great deal just with this.

.. _formatting language: https://docs.python.org/3/library/string.html#format-specification-mini-language

``input``
---------

.. rst-class:: left

For some of the exercises, you'll need to interact with a user at the
command line.

There's a nice built in function to do this - ``input``:

.. code-block:: ipython

    In [85]: fred = input('type something-->')
    type something-->I've typed something

    In [86]: print(fred)
    I've typed something

This will display a prompt to the user, allowing them to input text and
allowing you to bind that input to a symbol.

Lab: String Formatting
----------------------

Let's play with these a bit:

:ref:`exercise_string_formatting`



Files
=====

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

Lab: Files
----------

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





Exceptions
==========

A really nifty python feature -- really handy!

Another Branching structure
---------------------------

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

Exceptions Lab
--------------

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

In ``Examples/Session06/test_cigar_party.py``


Lab: Testing
------------

Pick an example from codingbat:

``http://codingbat.com``

Do a bit of test-driven development on it:

 * run something on the web site.
 * write a few tests using the examples from the site.
 * then write the function, and fix it 'till it passes the tests.

Do at least two of them.

Homework
=========

Catch up!
---------

* Finish the LABs from today

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


Material to review before next week
-----------------------------------

 * Dive into Python3: 7.2 -- 7.3
   http://www.diveintopython3.net/iterators.html#defining-classes

 * Think Pyhton: 15 -- 18
   http://www.greenteapress.com/thinkpython/html/thinkpython016.html

 * LPTHW: 40 -- 44
   http://learnpythonthehardway.org/book/ex40.html

[Note that in py3 you don't need to inherit from object]

Talk by Raymond Hettinger:

https://youtu.be/HTLu2DFOdTg

https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger
