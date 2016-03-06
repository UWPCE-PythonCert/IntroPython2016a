#!/usr/bin/env python

"""
pytest example of a parameterized test

NOTE: there is a failure in here! can you fix it? #b3 - i think this should be no space between thisthat result:
#"this that" to change to "thisthat"

"""
import pytest


# a (really simple) function to test
def add(a, b):
    """
    returns the sum of a and b
    """
    return a + b

# now some test data:

test_data = [((2, 3), 5),
             ((-3, 2), -1),
             ((2, 0.5), 2.5),
             (("this", "that"), "thisthat"),
             (([1, 2, 3], [6, 7, 8]), [1, 2, 3, 6, 7, 8]),
             ]


@pytest.mark.parametrize(("input", "result"), test_data)
def test_add(input, result):
    assert add(*input) == result
