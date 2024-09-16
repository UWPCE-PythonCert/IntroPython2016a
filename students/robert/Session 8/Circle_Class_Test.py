#!/usr/bin/env python 


from Circle_Class import Circle

import pytest

from math import pi


import unittest
#from Circle_Class import Circle

def test_init():
    Circle(3)

def test_radius():
    c = Circle(3)
    assert c.radius == 3



# class Test():

#     def setUp(self):
#         pass

#     def TestCase(self):
#         c = Circle(4)
#         self.assertEqual(c.radius,float(4))


# if __name__ == '__main__':
#     unittest.main()

