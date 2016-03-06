import math

class Circle:
    color = "red"


    def __init__(self,diameter):
        self.diameter = diameter
        self.area = self.get_area(diameter)

    def grow(self,factor=2):
        self.diameter = self.diameter * factor
        return self.diameter

    def get_area(self,diameter):
        self.area = math.pi *(diameter/2)**2
        return self.area

class Point:
    color = "red"
    size = 4

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_color(self):
        return self.color


#p1 = Point (3,4)
#print (p1.x, p1.get_color())

c1= Circle(4)

print("diameter:  ",c1.diameter)
print("area:  ",c1.area)

print("c1 growth  ", c1.grow(5))
print("c1 new diameter: ", c1.diameter)
#c1=Circle(c1.diameter)
print("area:  ,",c1.get_area(c1.diameter))

if isinstance(c1,Circle):
    print("true {}, is a {}".format(c1,Circle))