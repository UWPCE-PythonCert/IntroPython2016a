# Deana Holmer
# UWPCE Python 2016 Winter
# "fizzbuzz.py" due 1/21/2016
# In this exercise we count from 1-100, printing "fizz"
# instead of number for multiples of 3,
# "buzz" instead of number for multiples of 5
# and "fizzbuzz" instead of number for multiples of 3 and 5

import os
os.chdir('C:\\Documents\\Python\\python35src\\UWPython1\\week2')

fizznum = 3
buzznum = 5
for i in range(1, 101):
    if i % (fizznum * buzznum) == 0:
        print("fizzbuzz")
    elif i % fizznum == 0:
        print("fizz")
    elif i % buzznum == 0:
        print("buzz")
    else:
        print(i)
