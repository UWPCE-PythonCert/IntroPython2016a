# Week 2 - Lab #1: FizzBuzz
# Date: Thursday, January 28, 2016
# Student: Chi Kin Ho


def fizz_buzz(n):

    """
       This function takes a natural number, n.
       It prints out the numbers from 1 to n, but it replaces numbers
       divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz".
       Numbers divisible by both factors should display "FizzBuzz".
    """

    for i in range(1, n+1):

        if i % 3 == 0:
            if i % 5 == 0: # divisible by 3 and 5
                print('FizzBuzz')
            else: # divisible by 3 only
                print('Fizz')
        elif i % 5 == 0: # divisible by 5 only
            print('Buzz')
        else: # neither divisible by 3 nor divisible by 5
            print(i)

if __name__ == '__main__':
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