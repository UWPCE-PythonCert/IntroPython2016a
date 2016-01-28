def enterACoin (coinName):
	numberOfCoins = input("Enter the number of "+coinName+":")
	try: 
	    int(numberOfCoins)
	    return int(numberOfCoins)
	except:
		print("Please enter an integer")
		return enterACoin(coinName)

def isADollar(pennies, nickels, dimes, quarters):
	value = pennies*.01+nickels*.05+dimes*.1+quarters*.25
	return value

input("Try to enter a combination of coins that equals exactly $1. Press Enter to continue:")

pennies = enterACoin("Pennies")
nickels = enterACoin("Nickels")
dimes = enterACoin("Dimes")
quarters = enterACoin("Quarters")

value = isADollar(pennies=pennies, nickels = nickels, dimes = dimes, quarters = quarters)

if(value == 1.0):
	print("Congratualations, you win!")
elif(value > 1.0):
	print("That adds up to "+str(value)+" which is greater than a dollar. You lost!")
elif(value < 1.0):
	print("That adds up to "+str(value)+" which is less than a dollar. You lost!")
