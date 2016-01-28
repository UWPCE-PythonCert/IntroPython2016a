#!/usr/bin/python
import sys

def main():
	total = 0
	p = int(input("Enter the number of pennies:  "))
	n = int(input("Enter the number of nickels:  "))
	d = int(input("Enter the number of dimes:  "))
	q = int(input("Enter the number of quarters:  "))

	total = p + (n*5) + (d*10) + (q*25)
	if total == 100:
		print ("Congratulations you Won !")
	elif total < 100:
		print ("Sorry , amount you entered is less than 1 dollor")
	else:
		print ("Sorry , amount you entered is more than 1 dollor")
main()
