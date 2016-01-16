#!/usr/bin/env python3

n = int(input('Please enter a number: '))

if n > 0:
    for i in range(1,n+1):
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if len(s) > 0:
            print(s)
        else:
            print(i)
else:
    print('Sorry, but "{}" is not a natural number!'.format(n))

