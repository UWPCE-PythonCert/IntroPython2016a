#!/usr/bin/env python 

import math

class Circle(object):

 #   radius = None
    def __init__ (self,radius):
        self.radius = float(radius)
        self.diameter = float(radius*2)



    # @property
    # def radius(self):
    #     return int(self.radius)
        
    # @radius.setter
    # def radius(self,value):
    #     print('In radius setter')
    #     self.radius = int(value)       

    @property
    def diameter(self):
        return float(self.radius*2)

    @diameter.setter
    def diameter(self,value):
        self.radius = float(value/2)

    @property
    def area(self):
        return round((math.pi*(self.radius**2)),6)

    @area.setter
    def area(self,value):
        # how to just return AttributeError? -- Step 4
        print(AttributeError)

# from_diameter() missing 1 required positional argument 'Value'  -- Step 5
    @classmethod
    def from_diameter(cls,value):
#        cls.radius = int(value/2)
        return cls(float(value/2))

    def __str__(self):
        return('Circle with radius: {}'.format(round(self.radius*2,6)))

    def __repr__(self):
        return 'Circle(diameter={})'.format(self.radius*2)

    def __add__(self,other):
        total = (self.diameter+other.diameter)/4
        return Circle(total)


    def __mul__(self,other):
        mul = self.diameter/4*other
        return Circle(mul)

    def __rmul__(self,other):
        rmul = self.diameter/4*other
        return Circle(rmul)

    def __eq__(self,other):
        return self.diameter/4 == other.diameter/4

    def __gt__(self,other):
        return self.diameter/4  > other.diameter/4

    def __lt__(self,other):
        return self.diameter/4 < other.diameter/4























