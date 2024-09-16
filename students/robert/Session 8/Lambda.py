#!/usr/bin/env python 

# Using Lambda

def function_builder(n):

    l = []

    for i in range(n):
        l.append(lambda x, e=i: x + e)

    return l

# Using List Comprehensions

def function_builder(n):

    l = [lambda x, e=i: x+e for i in range(n)]

    return l


