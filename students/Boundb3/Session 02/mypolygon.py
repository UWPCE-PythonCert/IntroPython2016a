
import turtle
bob = turtle.Turtle()
alice = turtle.Turtle()


def rectangle(t,length,width):

    for i in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)
    print(bob)
    turtle.mainloop()

def mypolygon(t,sides,length):
    angle = 360 /sides
    t.fd(length/8)
    for i in range(sides):
        t.fd(length)
        t.lt(angle)
    print(alice)
    turtle.mainloop()


def mycircle(t,radius,sides):
    t.fd(radius)
    for i in range(sides):
        t.fd(radius*3/2)
        t.lt(360/sides)
    print(alice)
    turtle.mainloop()


import math


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)



def circle(t,r):
    circumference = 2*math.pi*r
    n=50
    length = circumference/n
    polygon(t,n,length)




#rectangle(bob,100,25)
#mycircle(alice,10,30)
#polygon(bob,7,70)
circle(bob,40)