#!/usr/bin/python
import sys
def FizzBuzz(n):
	for i in range(1,n+1):
		if i%3 == 0 and i%5 ==0:
			print "FizBuzz"
		elif i%3 == 0:
			print "Fizz"
		elif i%5 == 0:
			print "Buzz"
		else:
			print i

if __name__ == "__main__":
	if(len(sys.argv) != 2) :
		print "Please enter one and only one number as parameter"
	        exit()
	try:
		num = int(sys.argv[1])
	except ValueError:
		print ("Parameter should be a number")	
		exit()
	num = int(sys.argv[1])
	if num < 0:
		print "Number should be positive number"
		exit()
        FizzBuzz(num)
