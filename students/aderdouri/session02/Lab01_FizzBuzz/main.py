# 
# Date: Wednesday 20 January 2016
# File name: main.py
# Version: 1 
# Author: Abderrazak DERDOURI
# Course: PYTHON 100 A: Programming In Python  
#
# Description: FizzBuzz test
#
# 



import sys
from FizzBuzz import FizzBuzz

def main():

    print("-------------------------------")
    print("play FizzBuzz")
    print("-------------------------------")

    playFizzBuzz = True
    while playFizzBuzz:
        try:
            input_var = input("Please enter a natural number <q to quit>: ")
            if ("q"==input_var):
                playFizzBuzz = False
            else:
                FizzBuzz(int(input_var))
        except ValueError:
            print("Invalid entry")

    playFizzBuzz = True

if __name__ == "__main__":
    sys.exit(int(main() or 0))