#!/usr/bin/env python3

n = int(input('Please enter a number: '))

if n > 0: # could you also use a 'while n > 0' here? 
    for i in range(1,n+1): # or could you use the range function to specify numbers between 1 and 100? 
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if len(s) > 0: # what if i is divisible by both 3 and 5, for example 15? 
            print(s)
        else:
            print(i)
else:
    print('Sorry, but "{}" is not a natural number!'.format(n))

