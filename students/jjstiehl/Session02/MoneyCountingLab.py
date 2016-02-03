'''
Author: Julie Stiehl
Lab: Money Counting
Assigment:
Write a program to determine whether a mix of coins can make EXACTLY one dollar.
Your program should prompt users to enter the number of pennies, nickels, dimes, and quarters.
If the total value of the coins entered is equal to one dollar, the program should congratulate users for winning the game.
Otherwise, the program should display a message indicating whether the amount entered was more than or less than a dollar.
'''

#get input from user
print("Please enter the number of pennies, nickles, dimes, and quarters to make a dollar.""")
numPenny = int(input("Pennies:"))
numNickle= int(input("Nickles:"))
numDime = int(input("Dimes:"))
numQuarter = int(input("Quarters:"))

#calculate total amounts
totalPenny = numPenny * .01
totalNickle = numNickle * .05
totalDime = numDime * .1
totalQuarter = numQuarter * .25

outcome = totalPenny + totalNickle + totalDime + totalQuarter

#identify if answer is correct or not
if outcome == 1:
    print("You won the game!")
elif outcome < 1:
    print("Too low. Try again.")
elif outcome > 1:
    print("Too high. Try again.")
else:
    print("Start over.")
