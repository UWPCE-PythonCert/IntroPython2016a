
#create function
def moneycount(p, n, d, q):
	#get total cash input
	totalcash = .01 * p + n *.05 + d * .10 + q * .25
	if totalcash == 1:
		print('You have won the game')
	elif totalcash < 1: print('Your total change is less than a dollar')
	else: print('Your total change is greater than a dollar')

#ask for input - use float for decimals
try:
	p = int(input('# of pennies: '))
	n = int(input('# of nickels: '))
	d = int(input('# of dimes: '))
	q = int(input('# of quarters: '))
	
	#run function
	moneycount(p, n, d, q)

except:
	print('You did not enter that value as an integer! Try again')