from circle import Circle
import math
import pytest

def test_get_radius():
    c = Circle(5)
    assert c.radius == 5

def test_get_diameter():
    c = Circle(4)
    assert c.diameter == 2*4

def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_get_area():
    c = Circle(2)
    assert c.area == 2 * math.pi * 2

def test_set_area():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 42

def test_create_with_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_repr():
    c = Circle(4)
    assert c.__repr__() == 'Circle(4)'

def test_str():
    c = Circle(4)
    assert c.__str__() == "Circle with radius: 4.000000"

def test_add_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    return c.radius == 4

def test_mult_circles0():
    c = Circle(2)
    c *= 3
    return c.radius == Circle(12).radius

def test_mult_circles1():
    c = Circle(2)
    return (3 * c) == Circle(12)

def test_gt():
    c1 = Circle(2)
    c2 = Circle(4)
    assert not (c1 > c2)

def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 < c2)

def test_eq0():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 != c2)

def test_eq0():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c2 == c3)

def test_sort_circles():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles.__repr__() == "[Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]"

def test_reflected_numerics():
    a_circle = Circle(2)
    assert (a_circle * 3) == (3 * a_circle)

def test_augmented_add():
    a_circle = Circle(2)
    another_circle = Circle(4)
    a_circle += another_circle
    assert a_circle.r == 6

def test_augmented_mult():
    a_circle = Circle(4)
    a_circle *= 2
    assert a_circle.r == 8


