# 
# Date: Wednesday 20 January 2016
# File name: main.py
# Version: 1 
# Author: Abderrazak DERDOURI
# Course: PYTHON 100 A: Programming In Python  
#
# Description: MoneyCounting test
#
# 


import sys
from MoneyCounting import MoneyCounting

def main():

    print("-------------------------------")
    print("play MoneyCounting")
    print("-------------------------------")

    playMoneyCounting = True
    while playMoneyCounting:
        try:
            pennies = input("Please enter the number of pennies <q to quit>: ")
            if ("q"==pennies):
                break            
            intPennies = int(pennies)

            nickels = input("Please enter the number of nickels <q to quit>: ")
            if ("q"==nickels):
                break
            intNickels = int(nickels)

            dimes = input("Please enter the number of dimes <q to quit>: ")
            if ("q"==dimes):
                break
            intDimes = int(dimes)

            quarters = input("Please enter the number of quarters <q to quit>: ")
            if ("q"==quarters):
                break

            intQuarters = int(quarters)
            MoneyCounting(int(pennies), int(nickels), int(dimes), int(quarters))

        except ValueError:
            print("Invalid entry")

    playMoneyCounting = True

if __name__ == "__main__":
    sys.exit(int(main() or 0))
