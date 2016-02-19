# determine whether a mix of coins can make EXACTLY one dollar.
# prompt users to enter the number of pennies, nickels, dimes, and quarters
# If the total value of the coins entered is equal to one dollar, congrat users
# Else display a message saying if amount entered was more or less than dollar
print("Let's play a game where I don't tell you the rules. Doesn\'t that sound fun?")

print("Please enter a number for pennies")
num_pennies = input()

print("Please enter a number for nickels")
num_nickels = input()

print("Please enter a number for dimes")
num_dimes = input()

print("Please enter a number for quarters")
num_quarters = input()

quarters = int(num_quarters) * 25
dimes = int(num_dimes) * 10
nickels = int(num_nickels) * 5
pennies = int(num_pennies) * 1

change = (quarters + dimes + nickels + pennies)

if (int(change) == 100):
    print("Congratulations!  The Price is Right! You win at life!")
elif (int(change) > 100):
    print("You are a loser.  Hint: You bid over the Right Price")
else:
    print("You are a loser.  Hint: You bid under the Right Price")
