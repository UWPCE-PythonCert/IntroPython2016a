'''______________________________________________________
Mike Newton
newton33@uw.edu
Intro To Python 100A
University of Washington, Winter 2016
Last Updated:  18 January 2016
Python Version 3.5.1

FizzBuzz
Write a function to print out the numbers from 1 to n, 
but replace numbers divisible by 3 with "Fizz", numbers divisible 
by 5 with "Buzz". Numbers divisible by both factors should display "FizzBuzz.

The function should be named FizzBuzz and be able to accept a natural 
number as argument.
______________________________________________________'''

#Explain to the user what the script will accomplish
print("This script will accept a user defined natural number and count to that"
	"number starting at 1.  If the number is divisible by 3 'Fizz' will be displayed."
	"If the number is divisble by 5, 'Buzz' will be displayed.  If the number by both 3 and 5,"
	"'FizzBuzz' will be displayed\n")

#Ask user to input an integer
while True:
	try:
		N = int(input("Please enter an integer value of N that you would like to count to:  "))
		break
	#If user doesn't input an integer value, prompt them to try again
	except ValueError:
		print("That wasn't an integer!  Try again...")

for i in range(1,N+1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 3 == 0:
        print("Buzz")
    else:
        print(i)
