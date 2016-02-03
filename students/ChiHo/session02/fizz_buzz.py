# Week 2 - Lab #1: FizzBuzz
# Date: Saturday, January 16, 2016
# Student: Chi Kin Ho


def fizz_buzz(n):

    """
       This function takes a natural number, n.
       It prints out the numbers from 1 to n, but it replaces numbers
       divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz".
       Numbers divisible by both factors should display "FizzBuzz".
    """

    message = '' # can you simplify this by just using a print statement for each if/elif/else statement? 
    for i in range(1, n+1):
        is_divisible = False
        # you need to add logic here, similar to below, for when i is disivible by 3 AND by 5 :) 
        if i % 3 == 0: # divisible by 3 
            message += 'Fizz\n'
            is_divisible = True
        if i % 5 == 0: # divisible by 5      # any difference if you use if/elif/else instead of three if statments? 
            message += 'Buzz\n'
            is_divisible = True
        if not is_divisible: # not divisible by 3 and/or 5
            message += str(i) + '\n'
    # Display the new message on the screen.
    print(message)


# Test Case 1: n = 1
fizz_buzz(1)
# Test Case 2: n = 3
fizz_buzz(3)
# Test case 3: n = 5
fizz_buzz(5)
# Test case 4: n = 10
fizz_buzz(10)
# Test case 5: n = 16
fizz_buzz(16)
