#Brennen Bounds
#Python: Rick Riehle Hsi-Kai Yang
#Jan 20,2016


#Staring DICTIONARY - but order of access to ask the values is random!!***

# This is program to determine whether a mix of coins can make EXACTLY one dollar.
# Your program should prompt users to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar,
# the program should congratulate users for winning the game.
# Otherwise, the program should display a message indicating whether the amount entered
#  was more than or less than a dollar.


'''variables:
coin = local placeholder in def
answer = receipt of coin value from def

'''

#money = value of all of the change
#ttlanswer = money variable rounded to 2 decimals'''

#coindict={} a dictionary to hold the 4 types of coins and their quantity (default value of zero for each key)

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
        print(locals())
    return coin



#Welcome
print ("\n\t\tWelcome Money Player! \n\n This challenge will determine if your spare change \n "
       "equals one dollar exactly -- or not. Ready....?  Let's try!")
print ("\n\nYou can tell me the number of each coin type you have, "
       "and I will test the value to see how close you are to 1 dollar.")


print("I will ask you what quantity of coins you have for each coin type: penny, nickel, dime and quarter.")


# set coin types and establish default quantities
coindict = {"pennies": 0 ,"nickles": 0,"dimes": 0,"quarters": 0}


# collect coin quantites from user *** note a dictionary will produce question in a random order --
#   so be careful to watch the coin type in the question

for i in coindict: # this will be a random key value out of the total number of items in the dictionary
    print("\n")
    print("\tOk, how many" ,  i, "do you have?" ) #and "i" here is actually the name of the dictionary key
    answer = get_quantity()
    print("\t\tThanks - got it.  You had ", answer, i,".")
    coindict[i] = answer # condict[i] is the key name, and we are assigning a new value (to replace 0)to that key here

# calculate total value and limit to 2 decimals
# use a dictionary format to call the value of the dictionary key pair by calling the dictionary key

money = (coindict.get("pennies") * .01) + (coindict.get("nickles") * .05) + (coindict.get("dimes") *.10) + (coindict.get("quarters") *.25)
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
