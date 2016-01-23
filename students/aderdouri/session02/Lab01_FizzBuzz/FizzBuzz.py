# 
# Date: Wednesday 20 January 2016
# File name: FizzBuzz.py
# Version: 1 
# Author: Abderrazak DERDOURI
# Course: PYTHON 100 A: Programming In Python  
#
# Description: Week 2 Lab#1 FizzBuzz
#
# Write a function to print out the numbers from 1 to n, but replace numbers divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz". 
# Numbers divisible by both factors should display "FizzBuzz".
# The function should be named FizzBuzz and be able to accept a natural number as argument.
#


def FizzBuzz(n):
    for i in range(1, n+1):
        if (0==i%3 and 0==i%5):
            print ("FizzBuzz")
        elif (0==i%3):
            print ("Fizz")
        elif (0==i%5):
            print ("Buzz")
        else:
            print (i)
