# 
# Date: Wednesday 20 January 2016
# File name: MoneyCounting.py
# Version: 1 
# Author: Abderrazak DERDOURI
# Course: PYTHON 100 A: Programming In Python  
#
# Description: Week 2 Lab#2 Money Counting
#
# Write a program to determine whether a mix of coins can make EXACTLY one dollar. 
# Your program should prompt users to enter the number of pennies, nickels, dimes, and quarters. 
# If the total value of the coins entered is equal to one dollar, the program should congratulate users for winning the game. 
# Otherwise, the program should display a message indicating whether the amount entered was more than or less than a dollar.
# 


def MoneyCounting(pennies, nickels, dimes, quarters):
    amount = 0.01*pennies + 0.05*nickels + 0.1*dimes + 0.25*quarters
    if(1==amount):
        print ("Congratulation you are the winner")
    elif (1>amount):
        print ("Amount less than one dollar: ", amount)
    elif (1<amount):
        print ("Amount more than one dollar: ", amount)