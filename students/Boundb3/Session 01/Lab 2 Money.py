#Brennen Bounds
#Python: Rick Riehle Hsi-Kai Yang
#Jan 20,2016


# This is program to determine whether a mix of coins can make EXACTLY one dollar.
# Your program should prompt users to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar,
# the program should congratulate users for winning the game.
# Otherwise, the program should display a message indicating whether the amount entered
#  was more than or less than a dollar.


'''variables:
coin = placeholder
answer = receipt of coin value from def
p = penny
n = nickel
d = dime
q = quarter
money = value of all of the change
ttlanswer = money variable rounded to 2 decimals'''



import math

#routine to collect the number of coins from a user for a coin type


def get_quantity(coin = .5):
    count = 0
    coin = .05
    while type(coin) != int:
        try:
            coin = int(input("\tHow many (of these types of coin) do you have?"))

        except (TypeError, ValueError) as e:
            print ("Your entry: ", e, " is not a positive whole number.  Please enter a positive whole number.")
            count +=1
            if count > 5:
                print("Sorry, your entry does not match.  Let's quit the game")
                break
        if coin < 0:
            print("Really?  I don't think you have negative coins.  You need to enter a positive whole number.  Try this coin again.")
            get_quantity()
    return coin



#Welcome
print ("\n\t\tWelcome Money Player! \n\n This challenge will determine if your spare change \n "
       "equals one dollar exactly -- or not. Ready....?  Let's try!")
print ("\n\nYou can tell me the number of each coin type you have, "
       "and I will test the value to see how close you are to 1 dollar.")


# get coin quantities from user
print("I will ask you what quantity of coins you have for each coin type: penny, nickel, dime and quarter.")
for i in range (4):
    print("\n")
    if i == 0:
        print("\tLet's start with pennies.")
    if i == 1:
        print("\tOk, next, lets think nickels.")
    if i == 2:
        print("\tOk, next, how about dimes?")
    if i == 3:
        print("\tOk, and lastly, quarters.")

    answer = get_quantity()
    print("\t\tThanks - got it.  You had ", answer, "of those coins.")

# assign value to the coin quantity

    if i == 0:
        p = answer
    if i == 1:
        n = answer
    if i== 2:
        d = answer
    if i == 3:
        q = answer

# calculate total value and limit to 2 decimals

money = (p*.01) + (n*.05) + (d * .10) + (q*.25)
ttlanswer = math.ceil(money*100)/100

# share results with user

if money == 1.00:
    print("\n\tCongratulations you hit 1.00 Dollar on the nose!!")
elif money > 1.00:
    print("\n\tYour change totals to: $", ttlanswer, ".  It is $", (ttlanswer - int(1)), "over one dollar.")
elif money < 1.00:
    print("\n\tYour change totals to: $", ttlanswer, ".  It is $", (int(1) - ttlanswer), "under one dollar.")
else:
    print("\n\tI don't think this worked right.  Tell my programmer to take a look under the hood.  Thanks, goodbye.")