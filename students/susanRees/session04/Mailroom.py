# list 5 donors, amounts donated (1-3 donations each).
donors = {"ender wiggin": [100, 150, 50], "bill wilson": [25, 50], "oliver queen": [1000, 2500, 500], "buffy summers": [25], "adrienne rich": [300, 50, 250]}

# Sending a Thank You
# user selects ‘Send a Thank You’, prompt for a Full Name.
def thank():
    while True:
        fullName = input('Please input the full name of the donor you wish to thank.  To see a list of donors, type "list".')
        fullName = str.lower(fullName)
# user types ‘list’, show them a list of the donor names and re-prompt
        if fullName == "list":
            for key in sorted(donors.items()):
                print("{}".format(key))
# user types a name not in the list, add that name and use it.
        elif fullName not in donors:
            donors.update({fullName})
            print("This is a new donor, who has now been added to the donor list.")
# user types a name in the list, use it.
# once name selected, prompt for a donation amount.
        else:
# Verify that the amount is in fact a number, if not re-prompt.
            while True:
                amount = input('Please input the amount of the donation.')
                if amount != int(amount):
                    print("Please input a valid number")
                else:
# Once amount given, add amount to donation history of user.
                    donors[fullName].update({amount})
                    break
            break

# use string formatting to compose an email thanking the donor
# Print email to terminal and return to original prompt.

# Creating a Report
# If user selects ‘Create a Report’

# Print list of donors, sorted by total donation amount.
#            for key, value in sorted(donors.items()):
#                print("{} : {}".format(key, value))
# Donor Name, total donated, number donations, avg donation as value in row.
# Using string formatting, format the output rows
# should be tabular (values in each column should align with above and below)
# After printing this report, return to the original prompt.
# At any point, user should be able to quit and return to original prompt.
# From original prompt, user should be able to quit the script cleanly

# Guidelines
# First, factor your script into separate functions.
# each tasks can be accomplished by a series of steps.
# Write functions for individual steps and call them.
# Second, use loops to control the logical flow
# Interactive programs are a classic use-case for the while loop.
# Of course, input() will be useful here.
# Put the functions into the script at the top.
# Put your main interaction into an if __name__ == '__main__' block.
# Finally, use only functions and data types Learned so far.

# Next steps
# Update mailroom with dicts and exceptions
# Text and files and dicts, and...
# Coding Kata 14 - Dave Thomas
# http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
# and in this doc:
# Kata Fourteen: Tom Swift Under Milk Wood
# and on github here
# http://uwpce-pythoncert.github.io/IntroToPython/exercises/kata_fourteen.html
# Use The Adventures of Sherlock Holmes as input:
# ./exercises/sherlock.txt
# and on github here:
# http://uwpce-pythoncert.github.io/IntroToPython/_downloads/sherlock.txt
# This is intentionally open-ended and underspecified.
# There are many interesting decisions to make.
# Experiment with different lengths for the lookup key.
# (3 words, 4 words, 3 letters, etc)

# prompt the user to ‘Send a Thank You’ or ‘Create a Report’
while True:
    selection = input('To send a thank you letter, type "thank".  To create a report, type "report".'  'To exit, type "exit".')
    selection = str.lower(selection)
    if selection == "thank":
        thank()
        break
    elif selection == "report":
        print("report funtion placeholder")
        break
    elif selection == "exit":
        exit()
    else:
        print('Invalid selection.  Please type "thank" or "report".')
