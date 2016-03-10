import math

class Circle(object):

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)


    def __init__(self, radius):
        self.r = radius


    @property
    def radius(self):
        return self.r

    @radius.setter
    def radius(self, val):
        self.r = val


    @property
    def diameter(self):
        return 2 * self.r


    @diameter.setter
    def diameter(self, val):
        self.r = val / 2


    @property
    def area(self):
        return 2 * math.pi * self.r

    def __repr__(self):
        return 'Circle({})'.format(self.r)

    def __str__(self):
        return 'Circle with radius: {:6f}'.format(self.r)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.r + other.r)
        else:
            raise ValueError("The other parameter must be a circle type")

    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.r += other.r
            return self
        else:
            raise ValueError("The other parameter must be a circle type")

    def __radd__(self, other):
        return self.__add__(other)


    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.r * other)
        else:
            raise ValueError("The other parameter must be an int")

    def __imul__(self, other):
        if isinstance(other, int):
            self.r *= other
            return self
        else:
            raise ValueError("The other parameter must be an int")


    def __rmul__(self, other):
        return self.__mul__(other)


    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.r > other.r
        else:
            raise ValueError("The other parameter must be a circle type")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.r == other.r
        else:
            raise ValueError("The other parameter must be a circle type")
