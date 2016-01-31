#Brennen Bounds
#Python: Rick Riehle Hsi-Kai Yang
#Jan 20,2016


#Staring LISTS***

# This is program to determine whether a mix of coins can make EXACTLY one dollar.
# Your program should prompt users to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar,
# the program should congratulate users for winning the game.
# Otherwise, the program should display a message indicating whether the amount entered
#  was more than or less than a dollar.


'''variables:
coin = placeholder
answer = receipt of coin value from def


'''

#money = value of all of the change
#ttlanswer = money variable rounded to 2 decimals'''

coinlist=[]
coincount=[]

count = 0

import math


#routine to collect the number of coins from a user for a coin type


def get_quantity(coin = .5):
    count = 0

    while type(coin) != int:
        try:
            coin = int(input("\tType how many you have here:"))

        except (TypeError, ValueError) as e:
            print ("Your entry: ", e, " is not a positive whole number.  Please enter a positive whole number.")
            coin = .5
            count +=1
            if count == 5:
                print("Sorry, your entry was not a whole number.  Let's quit the game.  Good bye?")
                quit()
        if coin < 0:
            print("Really?  I don't think you have negative coins.  You need to enter a positive whole number.  Try this coin again.")
            coin = .5
    return coin



#Welcome
print ("\n\t\tWelcome Money Player! \n\n This challenge will determine if your spare change \n "
       "equals one dollar exactly -- or not. Ready....?  Let's try!")
print ("\n\nYou can tell me the number of each coin type you have, "
       "and I will test the value to see how close you are to 1 dollar.")


# get coin quantities from user
print("I will ask you what quantity of coins you have for each coin type: penny, nickel, dime and quarter.")
coinlist = ["pennies","nickles","dimes","quarters"]
coincount = [0,0,0,0]

length = len(coinlist)

for i in range(length): #this value needs to be a number
    print("\n")
    print("\tOk, how many" ,  coinlist[i], "do you have?" )
    answer = get_quantity()
    print("\t\tThanks - got it.  You had ", answer, coinlist[i],".")
    coincount[i] = answer

# calculate total value and limit to 2 decimals

money = (coincount[0]*.01) + (coincount[1]*.05) + (coincount[2] * .10) + (coincount[3]*.25)
ttlanswer = math.ceil(money * 100) / 100

# share results with user

if ttlanswer == 1.00:
    print("\n\tCongratulations you hit EXACTLY $1.00 on the nose!!")
elif ttlanswer > 1.00:
    print("\n\tYour change totals to: $", ttlanswer, ".  It is $", (ttlanswer - int(1)), "over one dollar.")
elif ttlanswer < 1.00:
    print("\n\tYour change totals to: $", ttlanswer, ".  It is $", (int(1) - ttlanswer), "under one dollar.")
else:
    print("\n\tI don't think this worked right.  Tell my programmer to take a look under the hood.  Thanks, goodbye.")
