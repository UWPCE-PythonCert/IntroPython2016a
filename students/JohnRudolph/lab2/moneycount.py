
def moneycount(p, n, d, q):
	#get total cash input based on int entered for each coin type
	totalcash = .01 * p + n *.05 + d * .10 + q * .25
	if totalcash == 1:
		print('You have won the game')
	elif totalcash < 1: print('Your total change is less than a dollar')
	else: print('Your total change is greater than a dollar')

#ask for input - make sure an int is enetered for each coin type
try:
	p = int(input('# of pennies: '))
	n = int(input('# of nickels: '))
	d = int(input('# of dimes: '))
	q = int(input('# of quarters: '))
	
	moneycount(p, n, d, q)

except:
	print('You did not enter that value as an integer! Try again')