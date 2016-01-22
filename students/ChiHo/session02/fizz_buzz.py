# Week 2 - Lab #1: FizzBuzz
# Date: Saturday, January 16, 2016
# Student: Chi Kin Ho


def FizzBuzz(n):

    """
       This function takes a natural number, n.
       It prints out the numbers from 1 to n, but it replaces numbers
       divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz".
       Numbers divisible by both factors should display "FizzBuzz".
    """

    message = ''
    for i in range(n):
        is_divisible = False
        if (i+1) % 3 == 0: # divisible by 3
            message += 'Fizz'
            is_divisible = True
        if (i+1) % 5 == 0: # divisible by 5
            message += 'Buzz'
            is_divisible = True
        if not is_divisible: # not divisible by 3 and/or 5
            message += str(i+1)
    # Display the new message on the screen.
    print(message)


# Test Case 1: n = 1
FizzBuzz(1)
# Test Case 2: n = 3
FizzBuzz(3)
# Test case 3: n = 5
FizzBuzz(5)
# Test case 4: n = 10
FizzBuzz(10)
# Test case 5: n = 16
FizzBuzz(16)