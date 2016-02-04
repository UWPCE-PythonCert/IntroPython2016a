"""
#-------------------------------------------------#
# Title: Mailroom - Week3 assignment
# Dev:   BBounds
# Date:  January 28 2016
#Class: Python 2016a
Instructor: Rick Riehle / TA: Summer Rae
#-------------------------------------------------#


Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts
they have donated. This structure should be populated at first with at least five donors, with
between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 2 actions:
 ‘Send a Thank You’ or ‘Create a Report’.

Sending a Thank You
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
If the user types ‘list’, show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isn’t.
Once an amount has been given, add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation.
Print the email to the terminal and return to the original prompt.
It is fine to forget new donors once the script quits running.

Creating a Report
If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular
(values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly
"""

if __name__ == "__main__":
    print("hi there")
else:
    raise Exception("This file was not created to be imported")

