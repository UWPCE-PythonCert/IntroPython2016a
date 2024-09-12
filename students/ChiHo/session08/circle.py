# Student: Chi Kin Ho
# Date: Wednesday, March 2, 2016

import math


class Circle(object):

    def __init__(self, the_radius):
        # Keep track of the radius of the circle.
        self._radius = the_radius
        # Calculate the diameter of the circle.
        self._diameter = self._radius * 2

    # alternate constructor
    @classmethod
    def from_diameter(cls, the_diameter):
        return cls(the_diameter / 2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, the_radius):
        if the_radius is not None:
            # Update the radius.
            self._radius = the_radius
            # Update the diameter.
            self._diameter = self._radius * 2

    @property
    def diameter(self):
        return self._diameter

    # Set the diameter of the circle and update its radius.
    @diameter.setter
    def diameter(self, the_diameter):
        if the_diameter is not None:
            # Update the diameter.
            self._diameter = the_diameter
            # Update the radius.
            self._radius = self._diameter / 2

    @property
    def area(self): # area property
        # Return the area of the circle: pi * radius * radius
        return math.pi * self._radius * self._radius

    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __str__(self):
        return 'Circle({})'.format(self._radius)

    # + operator overloading
    def __add__(self, other):
        return Circle(self._radius + other.radius)

    # augmented assignment operator += overloading
    def __iadd__(self, other):
        self = self + other
        return self

    # * operator overloading
    def __mul__(self, other):
        return Circle(self._radius * other)

    # augmented assignment operator *= overloading
    def __imul__(self, other):
        self = self * other
        return self

    # reflected numerics for the * operator overloading
    def __rmul__(self, other):
        return self * other

    # > operator overloading
    def __lt__(self, other):
        return self._radius < other.radius

    # >= operator overloading
    def __le__(self, other):
        return self._radius <= other.radius

    # > operator overloading
    def __gt__(self, other):
        return self._radius > other.radius

    # >= operator overloading
    def __ge__(self, other):
        return self._radius >= other.radius

    # == operator overloading
    def __eq__(self, other):
        return self._radius == other.radius

# Steps 1, 2, 3, and 3:

c = Circle(4)
print(c.radius)
print(c.diameter)
print(c.area)

# Step 5

c = Circle.from_diameter(20)
print(c.diameter)
print(c.radius)

# Step 6

print(repr(c))
d = eval(repr(c))
print(d)
print(c)

# Step 7

c1 = Circle(2)
c2 = Circle(4)
print(c1 + c2)
print(c2 * 3)
print(3 * c2)

# Step 8:

print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
c3 = Circle(4)
print(c2 == c3)

circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
print(circles)
circles.sort()
print(circles)


# Step 8: Optional Features

print(3 * c2 == c2 * 3)

a_circle = Circle(4)
another_circle = Circle(9)
a_circle += another_circle
print(a_circle)
print(another_circle)

a_circle = Circle(4)
a_circle *= 2
print(a_circle)