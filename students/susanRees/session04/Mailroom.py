# list 5 donors, amounts donated (1-3 donations each).
donors = {"ender wiggin": [100, 150, 50], "bill wilson": [25, 50], "oliver queen": [1000, 2500, 500], "buffy summers": [25], "adrienne rich": [300, 50, 250]}

# Sending a Thank You
# user selects ‘Send a Thank You’, prompt for a Full Name.
def thank():
    while True:
        fullName = input('Please input the full name of the donor you wish to thank.  To see a list of donors, type "list".  To return to the main menu, type "main"')
        fullName = str.lower(fullName)
# user types ‘list’, show them a list of the donor names and re-prompt
        if fullName == "list":
            for key in sorted(donors.items()):
                print("{}".format(key))
# At any point, user should be able to quit and return to original prompt.
        elif fullName == "main":
            print("I don't actually know how to return you to the main menu.  Um.  Pick something else?")
# user types a name not in the list, add that name and use it.
        elif fullName not in donors:
            donors[fullName] = []
            print("This is a new donor, who has now been added to the donor list.")
# user types a name in the list, use it.
# once name selected, prompt for a donation amount.
        else:
# Verify that the amount is in fact a number, if not re-prompt.
            while True:
                amount = input('Please input the amount of the donation.')
                try:
                    amount = int(amount)
                except ValueError:
                    print("Please input a valid number")
                else:
# Once amount given, add amount to donation history of user.
                    donors[fullName].append(amount)
                    print("This donation has been added to the donor record.")
                    print("Please find your thank you letter printed below.")
# use string formatting to compose an email thanking the donor
# Print email to terminal and return to original prompt.
                    print("\nDear {},\n\tThank you for your generous support!  Your donation of ${} will go a long way towards saving the world one gay at a time. \n\tSincerely,\n\t\tGay City\n".format(str.title(fullName), amount))
                    break
            break

# Creating a Report
# If user selects ‘Create a Report’
# Print list of donors, sorted by total donation amount.
# Donor Name, total donated, number donations, avg donation as value in row.
# Using string formatting, format the output rows
# should be tabular (values in each column should align with above and below)
def report():
    for key, values in (donors.items()):
        totalDonated = sum(values)
        numDonations = len(key)
        avgDonation = int(totalDonated/numDonations)
    for key in sorted(donors.items()):
        print("{}\t{}\t{}\t{}".format(key, totalDonated, numDonations, avgDonation))
# After printing this report, return to the original prompt.

if __name__ == '__main__':
# prompt the user to ‘Send a Thank You’ or ‘Create a Report’
    while True:
        selection = input('To send a thank you letter, type "thank".  To create a report, type "report".'  'To exit, type "exit".')
        selection = str.lower(selection)
        if selection == "thank":
            thank()
            break
        elif selection == "report":
            report()
        elif selection == "exit":
            exit()
        else:
            print('Invalid selection.  Please type "thank" or "report".')

# Guidelines
# First, factor your script into separate functions. CHECK
# each tasks can be accomplished by a series of steps. CHECK
# Write functions for individual steps and call them. CHECK
# Second, use loops to control the logical flow. CHECK
# Interactive programs are a classic use-case for the while loop. CHECK
# Of course, input() will be useful here. CHECK
# Put the functions into the script at the top.
# Put your main interaction into an if __name__ == '__main__' block. CHECK
# Finally, use only functions and data types Learned so far. CHECK
# At any point, user should be able to quit and return to original prompt. CHECK
# From original prompt, user should be able to quit the script cleanly CHECK

# Next steps
# Update mailroom with dicts and exceptions CHECK
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
