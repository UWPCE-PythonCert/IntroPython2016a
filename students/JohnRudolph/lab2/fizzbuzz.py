#createe fizzbuzz function
def fizzbuzz(start, stop):
	#need to +1 to stop in order to print last number
	for i in range(start, stop +1):
		#set string to null
		str = ''
		if i % 3 !=0 and i % 5 != 0: print(i)
		else:
			if (i % 3) == 0: str = 'Fizz'
			if (i % 5) == 0: str = str + 'Buzz'
			print(str)

#make sure input is entered as an integer
try:
	stop = int(input('Input last integer in range: '))
	fizzbuzz(1, stop)
except:
	print('You did not enter that value as an integer! Try again')
