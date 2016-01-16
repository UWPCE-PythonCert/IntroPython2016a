#!/usr/bin/env python3

total = 0

print("Please input the number of...")

pennies = int(input(" " * 4 + "pennies: "))
total += pennies

nickels = int(input(" " * 4 + "nickels: "))
total += nickels * 5

dimes = int(input(" " * 4 + "dimes: "))
total += dimes * 10

quarters = int(input(" " * 4 + "quarters: "))
total += quarters * 25

if total == 100:
    print("Congratulations! You have exactly $1!")
elif total > 100:
    print("Sorry, you have too many coins to make exactly $1")
else:
    print("Sorry, you only have {}¢".format(total))


