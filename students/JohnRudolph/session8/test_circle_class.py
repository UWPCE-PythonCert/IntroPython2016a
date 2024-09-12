import circle_class as cc
import pytest
from math import pi

def test_radius():
	'''
	test that radius can be set on init
	and called via get property
	'''
	radius = 4
	c = cc.Circle(radius=radius)
	assert radius == c.radius

def test_diameter():
	'''
	test that diameter is set when radius is provided
	'''
	radius = 4
	c = cc.Circle(radius=radius)
	assert radius*2 == c.diameter

def test_set_diameter():
	'''
	test that a new diameter can be set based on set property
	test that radius is reset when diameter is set
	'''
	radius = 4
	c = cc.Circle(radius=radius)
	new_diameter = 2
	c.diameter = new_diameter
	assert c.diameter == new_diameter
	assert c.radius == 1

def test_area():
	'''
	test that an area attribute is set when Circle is init
	'''
	radius = 4
	c = cc.Circle(radius=radius)
	area = (c.radius**2*pi)
	assert c.area == area

def test_area_error():
	'''
	Check if setting area raises an Attribute Error
	'''
	radius = 4
	c = cc.Circle(radius=radius)
	with pytest.raises(AttributeError):
		c.area = 2

def test_alternate_constructor():
	'''
	Check if setting area raises an Attribute Error
	'''
	diameter = 8
	c = cc.Circle(diameter = diameter)
	assert c.radius == (diameter/2)
	
def test_str_method():
	'''
	Check if __str__ method works as intended
	'''
	radius = 4
	c = cc.Circle(radius = radius)
	s = 'Circle with radius: {}'.format(radius)
	assert s == str(c)

def test_repr_method():
	'''
	Check if __str__ method works as intended
	'''
	radius = 4
	c = cc.Circle(radius=radius)
	s = 'Circle({})'.format(radius)
	d = repr(c)
	assert s == d

def test_add_method():
	'''
	Check if 2 circles can be added	
	'''
	radius = 4
	diameter = 10
	c1 = cc.Circle(radius = radius)
	c2 = cc.Circle(diameter= diameter)
	c3 = c1 + c2
	assert c3.radius == radius + diameter/2

def test_mult_method():
	'''
	Check if 2 circles can be added	
	'''
	radius = 4
	num = 3
	c1 = cc.Circle(radius = radius)
	c2 = c1*num
	assert c2.radius == radius*num

def test_gt_method():
	'''
	Check if circle1 radius greater than circle2 radius
	'''
	radius1 = 4
	radius2 = 6
	c1 = cc.Circle(radius=radius1)
	c2 = cc.Circle(radius=radius2)
	assert (c2 > c1) == True

def test_lt_method():
	'''
	Check if circle1 radius less than circle2 radius
	'''
	radius1 = 4
	radius2 = 6
	c1 = cc.Circle(radius=radius1)
	c2 = cc.Circle(radius=radius2)
	assert (c1 < c2) == True

def test_eq_method():
	'''
	Check if circle1 radius less than circle2 radius
	'''
	radius1 = 6
	radius2 = 6
	c1 = cc.Circle(radius=radius1)
	c2 = cc.Circle(radius=radius2)
	assert (c1 == c2) == True

def test_sort_method():
	'''
	Test of a list of circle objects is sortable
	'''
	c1, c2, c3 = cc.Circle(radius=4), cc.Circle(radius=7), cc.Circle(radius=2)
	circles = [c1, c2, c3]
	sort_circles = [c3, c1, c2]
	for i,n in zip(sorted(circles), sort_circles):
		assert i.radius == n.radius
	