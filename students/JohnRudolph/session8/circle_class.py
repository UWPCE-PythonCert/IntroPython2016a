#!/usr/bin/env python
from math import pi

######################################################
##############    CIRCLE CLASS EXERCISE ##############
######################################################

class Circle(object):
	'''
	Defines a circle object which takes
	A radius or diameter as an input
	And performs some operations
	'''

	#init takes radius or diameter as an input
	def __init__(self, **kwargs):
		if [x for x in kwargs if x not in ['radius', 'diameter']]:
			raise AttributeError('radius or diameter is required')
		#if radius then set radius
		if 'radius' in kwargs:
			self._radius = kwargs['radius']
		#if diameter then set radius
		if'diameter' in kwargs:
			self._radius = kwargs['diameter']/2

	@property
	def radius(self):
		return self._radius

	@property
	def diameter(self):
		return self.radius*2

	@property
	def area(self):
		return self._radius**2*pi

	@radius.setter
	def radius(self, radius):
		self._radius = radius

	@diameter.setter
	def diameter(self, diameter):
		self._radius = diameter/2

	def __repr__(self):
		return 'Circle({})'.format(self.radius)

	def __str__(self):
		return 'Circle with radius: {}'.format(self.radius)
	#set __add__ method to create new circle class with added radius values
	def __add__(self, other):
		add_radius= self.radius + other.radius
		return Circle(radius= add_radius)
	#set __mul__ method to create new circle class with multiplied radius
	def __mul__(self, num):
		return Circle(radius=(self.radius*num))
	#set comparison operators
	def __gt__(self, other):
		return self.radius > other.radius

	def __lt__(self, other):
		return self.radius < other.radius

	def __eq__(self, other):
		return self.radius == other.radius
