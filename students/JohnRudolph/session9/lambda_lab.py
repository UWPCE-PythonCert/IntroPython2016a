#!/usr/bin/env python
def increment_function(n): return lambda x: x + n

def function_builder(n):
	return[increment_function(x) for x in range(n)]

f_list = function_builder(5)
for i in f_list:
	print(i(2))
