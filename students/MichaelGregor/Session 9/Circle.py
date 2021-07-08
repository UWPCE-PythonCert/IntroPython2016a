import math

class Circle(object):

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2

    def __repr__(self):
        return 'Circle(' + repr(self._radius) + ')'

    def __str__(self):
        return 'Circle(' + str(self._radius) + ')'

    def __add__(self, other):
        r1, r2 = self.radius, other.radius
        total = r1 + r2
        return Circle(total)

    def __eq__(self, other):
        r1, r2 = self.radius, other.radius
        if r1 == r2:
            return True
        else:
            return False

    def __gt__(self, other):
        r1, r2 = self.radius, other.radius
        if r1 > r2:
            return True
        else:
            return False

    def __lt__(self, other):
        r1, r2 = self.radius, other.radius
        if r1 < r2:
            return True
        else:
            return False

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value/2

    @property
    def area(self):
        return 2 * math.pi * self._radius

    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)


def main():

    c = Circle(10)

    print(c.radius)
    print(c.diameter)

    c.diameter = 50

    print(c.diameter)
    print(c.radius)

    c = Circle(2)
    print(c.area)

    c = Circle.from_diameter(8)

    print(c.diameter)
    print(c.radius)

    print(repr(c))
    print(str(c))

    d = eval(repr(c))

    print(d)

    c1 = Circle(4)
    c2 = Circle(2)

    print(c1)
    print(c2)

    c3 = c1+c2
    print(c3._radius)

    print(c1 == c2)

    print(c1>c2)
    print(c1<c2)

if __name__ == "__main__":
    main()


