#!/usr/bin/python
for i in range(1,101):
    if i%3==0: # can you simplify this using 'OR' and 'AND' ? 
        if i%5==0:
            print ("FizzBuzz")
        else:
            print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print(i)
