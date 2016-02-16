# Write a program that prints the numbers from 1 to 100 inclusive.
# for multiples of three print “Fizz” instead of number
# For multiples of five print “Buzz”.
# multiples of both three and five print “FizzBuzz”

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
