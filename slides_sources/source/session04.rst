.. include:: include.rst

*************************************************
Session Four: Exceptions, Testing, Comprehensions
*************************************************



Announcements
=============



Review/Questions
================


Homework
--------

Let's take a look.


Topics for Today
================



Lightning Talks
---------------------

.. rst-class:: medium

  Chi Ho

  Tom Gaffney

  Anybody else ready?  I'll be asking for volunteers at the end of class.



Lists and Mutable Sequence Methods
==================================

.. rst-class:: left

In addition to all the methods supported by sequences we've seen above, mutable sequences (the List), have a number of other methods that are
used to change the list.

You can find all these in the Standard Library Documentation:

https://docs.python.org/3/library/stdtypes.html#typesseq-mutable

Assignment
-----------

You've already seen changing a single element of a list by assignment.

Pretty much the same as "arrays" in most languages:

.. code-block:: ipython

    In [100]: list = [1, 2, 3]
    In [101]: list[2] = 10
    In [102]: list
    Out[102]: [1, 2, 10]


Growing the List
----------------

``.append()``, ``.insert()``, ``.extend()``

.. code-block:: ipython

    In [74]: food = ['spam', 'eggs', 'ham']
    In [75]: food.append('sushi')
    In [76]: food
    Out[76]: ['spam', 'eggs', 'ham', 'sushi']
    In [77]: food.insert(0, 'beans')
    In [78]: food
    Out[78]: ['beans', 'spam', 'eggs', 'ham', 'sushi']
    In [79]: food.extend(['bread', 'water'])
    In [80]: food
    Out[80]: ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']


.. nextslide:: More on Extend

You can pass any sequence to ``.extend()``:

.. code-block:: ipython

    In [85]: food
    Out[85]: ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']
    In [86]: food.extend('spaghetti')
    In [87]: food
    Out[87]:
    ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water',
     's', 'p', 'a', 'g', 'h', 'e', 't', 't', 'i']


Shrinking the List
------------------

``.pop()``, ``.remove()``

.. code-block:: ipython

    In [203]: food = ['spam', 'eggs', 'ham', 'toast']
    In [204]: food.pop()
    Out[204]: 'toast'
    In [205]: food.pop(0)
    Out[205]: 'spam'
    In [206]: food
    Out[206]: ['eggs', 'ham']
    In [207]: food.remove('ham')
    In [208]: food
    Out[208]: ['eggs']

.. nextslide:: Removing Chunks of a List

You can also delete *slices* of a list with the ``del`` keyword:

.. code-block:: ipython

    In [92]: nums = range(10)
    In [93]: nums
    Out[93]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [94]: del nums[1:6:2]
    In [95]: nums
    Out[95]: [0, 2, 4, 6, 7, 8, 9]
    In [96]: del nums[-3:]
    In [97]: nums
    Out[97]: [0, 2, 4, 6]


Copying Lists
-------------

You can make copies of part of a list using *slicing*:

.. code-block:: ipython

    In [227]: food = ['spam', 'eggs', 'ham', 'sushi']
    In [228]: some_food = food[1:3]
    In [229]: some_food[1] = 'bacon'
    In [230]: food
    Out[230]: ['spam', 'eggs', 'ham', 'sushi']
    In [231]: some_food
    Out[231]: ['eggs', 'bacon']

If you provide *no* arguments to the slice, it makes a copy of the entire list:

.. code-block:: ipython

    In [232]: food
    Out[232]: ['spam', 'eggs', 'ham', 'sushi']
    In [233]: food2 = food[:]
    In [234]: food is food2
    Out[234]: False


.. nextslide:: Shallow Copies

The copy of a list made this way is a *shallow copy*.

The list is itself a new object, but the objects it contains are not.

*Mutable* objects in the list can be mutated in both copies:

.. code-block:: ipython

    In [249]: food = ['spam', ['eggs', 'ham']]
    In [251]: food_copy = food[:]
    In [252]: food[1].pop()
    Out[252]: 'ham'
    In [253]: food
    Out[253]: ['spam', ['eggs']]
    In [256]: food.pop(0)
    Out[256]: 'spam'
    In [257]: food
    Out[257]: [['eggs']]
    In [258]: food_copy
    Out[258]: ['spam', ['eggs']]


.. nextslide:: Copies Solve Problems

Consider this common pattern:

.. code-block:: python

    for x in somelist:
        if should_be_removed(x):
            somelist.remove(x)

This looks benign enough, but changing a list while you are iterating over it can be the cause of some pernicious bugs.

.. nextslide:: The Problem

For example:

.. code-block:: ipython

    In [27]: l = list(range(10))
    In [28]: l
    Out[28]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [29]: for item in l:
       ....:     l.remove(item)
       ....:
    
.. nextslide:: Was this what you expected?

For example:

.. code-block:: ipython

    In [27]: l = list(range(10))
    In [28]: l
    Out[28]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [29]: for item in l:
       ....:     l.remove(item)
       ....:
    In [30]: l
    Out[30]: [1, 3, 5, 7, 9]

.. nextslide:: The Solution

Iterate over a copy, and mutate the original:

.. code-block:: ipython

    In [33]: l = list(range(10))

    In [34]: for item in l[:]:
       ....:     l.remove(item)
       ....:
    In [35]: l
    Out[35]: []


.. nextslide:: Just Say It, Already

Okay, so we've done this a bunch already, but let's state it out loud.

You can iterate over a sequence.

.. code-block:: python

    for element in sequence:
        do_something(element)

which is what we mean when we say a sequence is an "iterable".

Again, we'll touch more on this in a short while, but first a few more words about Lists and Tuples.


Miscellaneous List Methods
--------------------------


These methods change a list in place and are not available on immutable sequence types.

``.reverse()``

.. code-block:: ipython

    In [129]: food = ['spam', 'eggs', 'ham']
    In [130]: food.reverse()
    In [131]: food
    Out[131]: ['ham', 'eggs', 'spam']

``.sort()``

.. code-block:: ipython

    In [132]: food.sort()
    In [133]: food
    Out[133]: ['eggs', 'ham', 'spam']

Because these methods mutate the list in place, they have a return value of ``None``


.. nextslide:: Custom Sorting

``.sort()`` can take an optional ``key`` parameter.

It should be a function that takes one parameter (list items one at a time) and returns something that can be used for sorting:

.. code-block:: ipython

    In [137]: def third_letter(string):
       .....:     return string[2]
       .....:
    In [138]: food.sort(key=third_letter)
    In [139]: food
    Out[139]: ['spam', 'eggs', 'ham']



List Performance
----------------

.. rst-class:: build

* indexing is fast and constant time: O(1)
* ``x in l`` is proportional to n: O(n)
* visiting all is proportional to n: O(n)
* operating on the end of list is fast and constant time: O(1)

  * append(), pop()

* operating on the front (or middle) of the list depends on n: O(n)

  * ``pop(0)``, ``insert(0, v)``
  * But, reversing is fast. ``Also, collections.deque``

 http://wiki.python.org/moin/TimeComplexity


Choosing Lists or Tuples
------------------------

Here are a few guidelines on when to choose a list or a tuple:

* If it needs to mutable: list

* If it needs to be immutable: tuple

  * (safety when passing to a function)

Otherwise ... taste and convention


Convention
-----------


Lists are Collections (homogeneous):
-- contain values of the same type
-- simplifies iterating, sorting, etc

tuples are mixed types:
-- Group multiple values into one logical thing
-- Kind of like simple C structs.


Other Considerations
--------------------

.. rst-class:: build

* Do the same operation to each element?

  * list

* Small collection of values which make a single logical item?

  * tuple

* To document that these values won't change?

  * tuple

* Build it iteratively?

  * list

* Transform, filter, etc?

  * list


More Documentation
------------------

For more information, read the list docs:

https://docs.python.org/3.5/library/stdtypes.html#mutable-sequence-types

(actually any mutable sequence....)


List Lab
---------

Let's play a bit with Python lists...

:ref:`exercise_list_lab`



Lightning Talk
==============

.. rst-class:: center large

Chi Ho



Iteration
=========

.. rst-class:: build

Repetition, Repetition, Repetition, Repe...


For Loops
---------

We've seen simple iteration over a sequence with ``for ... in``:

.. code-block:: ipython

    In [170]: for x in "a string":
       .....:         print(x)
       .....:
    a
    s
    t
    r
    i
    n
    g


.. nextslide:: No Indexing Required

Contrast this with other languages, where you must build and use an ``index``:

.. code-block:: javascript

    for(var i = 0; i < arr.length; i++) {
        var value = arr[i];
        alert(i + ") " + value);

If you *do* need an index, you can use ``enumerate``:

.. code-block:: ipython

    In [140]: for idx, letter in enumerate('Python'):
       .....:     print(idx, letter, end=' ')
       .....:
    0 P 1 y 2 t 3 h 4 o 5 n


``range`` and ``for`` Loops
---------------------------

The ``range`` builtin is useful for looping a known number of times:

.. code-block:: ipython

    In [171]: for i in range(5):
       .....:     print(i)
       .....:
    0
    1
    2
    3
    4

But you don't really need to do anything at all with ``i``

.. nextslide::

In fact, it's a common convension to make this clear with a "nothing" name:

.. code-block:: ipython

    In [21]: for __ in range(5):
       ....:     print("*")
       ....:
    *
    *
    *
    *
    *


.. nextslide:: No Namespace

Be alert that a loop does not create a local namespace:

.. code-block:: ipython

    In [172]: x = 10
    In [173]: for x in range(3):
       .....:     pass
       .....:
    In [174]: x
    Out[174]: 2


.. nextslide:: Loop Control

Sometimes you want to interrupt or alter the flow of control through a loop.

Loops can be controlled in two ways, with ``break`` and ``continue``


.. nextslide:: Break

The ``break`` keyword will cause a loop to immediately terminate:

.. code-block:: ipython

    In [141]: for i in range(101):
       .....:     print(i)
       .....:     if i > 50:
       .....:         break
       .....:
    0 1 2 3 4 5... 46 47 48 49 50 51

.. nextslide:: Continue

The ``continue`` keyword will skip later statements in the loop block, but
allow iteration to continue:

.. code-block:: ipython

    In [143]: for in in range(101):
       .....:     if i > 50:
       .....:         break
       .....:     if i < 25:
       .....:         continue
       .....:     print(i, end=' ')
       .....:
       25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

.. nextslide:: else

For loops can also take an optional ``else`` block.

Executed only when the loop exits normally (not via break):

.. code-block:: ipython

    In [147]: for x in range(10):
       .....:     if x == 11:
       .....:         break
       .....: else:
       .....:     print('finished')
    finished
    In [148]: for x in range(10):
       .....:     if x == 5:
       .....:         print(x)
       .....:         break
       .....: else:
       .....:     print('finished')
    5

This is a really nice unique Python feature!


While Loops
-----------

The ``while`` keyword is for when you don't know how many loops you need.

It continues to execute the body until condition is not ``True``::

    while a_condition:
       some_code
       in_the_body

.. nextslide:: ``while`` vs. ``for``

``while``  is more general than ``for``

-- you can always express ``for`` as ``while``, but not always vice-versa.

``while``  is more error-prone -- requires some care to terminate

loop body must make progress, so condition can become ``False``

potential error -- infinite loops:

.. code-block:: python

    i = 0;
    while i < 5:
        print(i)


.. nextslide:: Terminating a while Loop

Use ``break``:

.. code-block:: ipython

    In [150]: while True:
       .....:     i += 1
       .....:     if i > 10:
       .....:         break
       .....:     print(i)
       .....:
    1 2 3 4 5 6 7 8 9 10

.. nextslide:: Terminating a while Loop

Set a flag:

.. code-block:: ipython

    In [156]: import random
    In [157]: keep_going = True
    In [158]: while keep_going:
       .....:     num = random.choice(range(5))
       .....:     print(num)
       .....:     if num == 3:
       .....:         keep_going = False
       .....:
    3

.. nextslide:: Terminating a While Loop

Use a condition:

.. code-block:: ipython

    In [161]: while i < 10:
       .....:     i += random.choice(range(4))
       .....:     print(i)
       .....:
    0 0 2 3 4 6 8 8 8 9 12


Similarities
------------

Both ``for`` and ``while`` loops can use ``break`` and ``continue`` for
internal flow control.

Both ``for`` and ``while`` loops can have an optional ``else`` block

In both loops, the statements in the ``else`` block are only executed if the
loop terminates normally (no ``break``)


String Features
================

.. rst-class:: center large

  Fun with Strings

Strings
---------

A string literal creates a string type

(we've seen this already...)

::

    "this is a string"

    'So is this'

    """and this also"""

You can also use ``str()``

.. code-block:: ipython

    In [256]: str(34)
    Out[256]: '34'



String Methods
--------------

String objects have a lot of methods.

Here are just a few:

String Manipulations
---------------------

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
--------

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
-----------------

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


Multiple placeholders:
-----------------------

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


Named placeholders:
-------------------

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


One Last Trick
---------------

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


String Formatting LAB
---------------------

Let's play with these a bit:

:ref:`exercise_string_formatting`


Dictionaries and Sets
=====================

Handy hints for/from Homework
-----------------------------

.. rst-class:: mlarge

  You almost never need to loop through the indexes of a sequence

nifty for loop tricks
---------------------

**tuple unpacking:**

remember this?

.. code-block:: python

    x, y = 3, 4

You can do that in a for loop, also:

.. code-block:: ipython

  In [4]: l = [(1, 2), (3, 4), (5, 6)]

  In [5]: for i, j in l:
              print("i:%i, j:%i"%(i, j))

  i:1, j:2
  i:3, j:4
  i:5, j:6

(Mailroom example)


Looping through two loops at once:
----------------------------------

.. rst-class:: mlarge

  ``zip``

.. code-block:: ipython

    In [10]: l1 = [1, 2, 3]

    In [11]: l2 = [3, 4, 5]

    In [12]: for i, j in zip(l1, l2):
       ....:     print("i:%i, j:%i"%(i, j))
       ....:
    i:1, j:3
    i:2, j:4
    i:3, j:5

Can be more than two:

.. code-block:: python

  for i, j, k, l in zip(l1, l2, l3, l4):


Need the index and the item?
----------------------------

.. rst-class:: mlarge

  ``enumerate``

.. code-block:: ipython

    In [2]: l = ['this', 'that', 'the other']

    In [3]: for i, item in enumerate(l):
       ...:     print("the %ith item is: %s"%(i, item))
       ...:
    the 0th item is: this
    the 1th item is: that
    the 2th item is: the other



Homework Comments
-----------------

Building up a long string.

The obvious thing to do is something like::

  msg = ""
  for piece in list_of_stuff:
      msg += piece

But: strings are immutable -- python needs to create a new string each time you add a piece -- not efficient::

   msg = []
   for piece in list_of_stuff:
       msg.append(piece)
   " ".join(msg)

appending to lists is efficient -- and so is the join() method of strings.

.. nextslide::

.. rst-class:: center mlarge

You can put a mutable item in an immutable object!

(demo)

.. nextslide:: A couple small things:

|
| Use string formatting
|
| The ``sum()`` function
|
| Deleting from list (list_lab)
|

.. nextslide::

What is ``assert`` for?

Testing -- NOT for issues expected to happen operationally::

    assert m >= 0

in operational code should be::

    if m < 0:
        raise ValueError

I'll cover next week ...

(Asserts get ignored if optimization is turned on!)



A little warm up
================


Fun with strings
------------------

* Rewrite: ``the first 3 numbers are: %i, %i, %i"%(1,2,3)``

    - for an arbitrary number of numbers...



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
====


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
------------------------------


Have some fun with dictionaries and sets!

:ref:`exercise_dict_lab`


Lightning Talk
==============

.. rst-class:: center large

Tom Gaffney


Homework
========


Recommended Reading:
---------------------
  * Dive Into Python: Chapt. 13,14


Assignments:
-------------

 * Finish lab exercises
 * Coding kata: trigrams
 * Paths and files
 * Update mailroom with dicts and exceptions


Text and files and dicts, and...
---------------------------------

* Coding Kata 14 - Dave Thomas

    http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

    and in this doc:

    :doc:`./exercises/kata_fourteen`

    and on github here

    http://uwpce-pythoncert.github.io/IntroToPython/exercises/kata_fourteen.html

.. nextslide::

* Use The Adventures of Sherlock Holmes as input:

    :download:`./exercises/sherlock.txt`

    and on github here:

    http://uwpce-pythoncert.github.io/IntroToPython/_downloads/sherlock.txt

* This is intentionally open-ended and underspecified. There are many interesting decisions to make.

* Experiment with different lengths for the lookup key. (3 words, 4 words, 3 letters, etc)

