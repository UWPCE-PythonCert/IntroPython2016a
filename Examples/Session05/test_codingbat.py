#!/usr/bin/env python

"""
test file for codingbat module

This version can be run with nose or py.test
"""

from codingbat import sleep_in
from codingbat import sumdouble


def test_false_false():
    assert sleep_in(False, False) is True


def test_true_false():
    assert not (sleep_in(True, False)) is True


def test_false_true():
    assert sleep_in(False, True) is True


def test_true_true():
    assert sleep_in(True, True) is True


def test_sumdouble1():
    assert sumdouble(1, 2) == 3


def test_sumdouble2():
    assert sumdouble(3, 2) == 5


def test_sumdouble3():
    assert sumdouble(2, 2) == 8
