from quadratic import Quadratic as quad


def test_quad0():
    my_quad = quad(a=2, b=3, c=1)
    assert my_quad(0) == 1

def test_quad1():
    my_quad = quad(a=2, b=3, c=1)
    assert my_quad(1) == 6

def test_quad2():
    my_quad = quad(a=2, b=3, c=1)
    assert my_quad(2) == 15

def test_quad3():
    my_quad = quad(a=2, b=3, c=1)
    assert my_quad(3) == 28


