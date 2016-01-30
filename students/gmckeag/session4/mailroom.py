#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

user_option_dict = {0: 'Unknown', 1: 'Send Thank You', 2: "Create Report", 'quit': 'quit', 'list': 'List donor names'}

donor_dict = {'Fred Barnes': [200, 550, 125],
              'Mary Jane': [2500, 25],
              'Eric Idol': [400000, 250, 1],
              'Lucy Love': [25, 25],
              'Mr Trump': [1]
              }


def get_top_level_menu_response():
    """
    """
    prompt = """
    ** Mailroom Menu Options **

    Select from the following:
    1 --- Send a thank you
    2 --- Create a report
    Q --- To quit
    > Enter 1, 2 or Q : """

    selection = user_option_dict[0]
    while selection == user_option_dict[0]:

        user_input = input(prompt)

        if user_input == '1':
            selection = user_option_dict[1]
        elif user_input == '2':
            selection = user_option_dict[2]
        elif user_input[0].upper() == 'Q':
            selection = user_option_dict['quit']
        else:
            selection = user_option_dict[0]
            print('    Unrecognized input, please try again\n')

        print('\n    You selected: {}\n'.format(selection))

    return selection


def thank_donor(donor):
    """
    """
    print("    Thank donor: {}".format(donor))


def list_donors():
    """
    """
    print('\n    Donors')
    print('    -------------------')
    for donor in donor_dict:
        print('    {:16s}'.format(donor))


def get_thank_you_menu_response():
    """
    """
    prompt = """
    ** Send Thank You Menu Options **

    Enter one of the following:
    To send thank you ....... Enter: donor's full name
    To list donors .......... Enter: list
    To return to top menu ... Enter: Q
    > Enter:  """

    selection = user_option_dict[0]
    while selection == user_option_dict[0]:

        user_input = input(prompt)

        if user_input.lower() == 'list':
            list_donors()
            promt_for_donation = False
        elif user_input in donor_dict:
            thank_donor(user_input)
            prompt_for_donation = True
        elif user_input[0].upper() == 'Q':
            selection = user_option_dict['quit']
        else:
            prompt_for_donation = True

        if prompt_for_donation:
            if user_input not in donar_dict:
                donar_dict[user_input] = []
            donation_amount = input('Enter amount of donation $: ')
            try:
                donation_amount = int(donation_amount)
                donar_dict[user_input].append(donation_amount)
            except:
                selection = user_option_dict[0]

    return selection


def send_thank_you():
    """
    """
    get_thank_you_menu_response()


def display_donor_report():
    """
    """
    donor_list = []
    for donor in donor_dict:
        donor_list.append((donor, sum(donor_dict[donor])))

    donor_list = sorted(donor_list, key=itemgetter(1), reverse=True)

    print("        Name             $ Total    Donations      $ Average")
    print("    --------------------------------------------------------")

    for record in donor_list:
        donor = record[0]
        print("    {name:16s}  {total:10,.2f}           {count:2}     {avg:10,.2f}".format(
                name=donor,
                count=len(donor_dict[donor]),
                avg=sum(donor_dict[donor]) / float(len(donor_dict[donor])),
                total=sum(donor_dict[donor])))


def main():
    """
    mailroom
    """
# ----------------------------------------------------------------------------------------------------------------------
# Mailroom
# A complete program
# Using basic data types and logic for a full program
#
# Goal:
# You work in the mail room at a local charity. Part of your job is to write incredibly boring,
# repetitive emails thanking your donors for their generous gifts. You are tired of doing this over
# an over again, so yo’ve decided to let Python help you out of a jam.
#
# The program
# Write a small command-line script called mailroom.py. This script should be executable. The script should
# accomplish the following goals:
#
# It should have a data structure that holds a list of your donors and a history of the amounts they have
# donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
#
# The script should prompt the user (you) to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
# Sending a Thank You
# If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
# If the user types ‘list’, show them a list of the donor names and re-prompt
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
#
# Once a name has been selected, prompt for a donation amount.
# Verify that the amount is in fact a number, and re-prompt if it isn’t.
# Once an amount has been given, add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation.
# Print the email to the terminal and return to the original prompt.
# It is fine to forget new donors once the script quits running.
#
# Creating a Report
# If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation amount as values in each row.
# Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values
# in each column should align with those above and below)
#
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly
# Guidelines
# First, factor your script into separate functions. Each of the above tasks can be accomplished by a series of steps.
# Write discreet functions that accomplish individual steps and call them.
#
# Second, use loops to control the logical flow of your program. Interactive programs are a classic use-case for
# the while loop.
#
# Of course, input() will be useful here.
#
# Put the functions you write into the script at the top.
#
# Put your main interaction into an if __name__ == '__main__' block.
#
# Finally, use only functions and the basic Python data types you’ve learned about so far. There is no need
# to go any farther than that for this assignment.
#
# Submission
# As always, put the new file in your student directory and git add it to your repo early. Make frequent
# commits with good, clear messages about what you are doing and why. When you are done, push your changes
# and make a pull request.
# ----------------------------------------------------------------------------------------------------------------------
#
    done = False
    while not done:
        user_selection = get_top_level_menu_response()
        if user_selection == user_option_dict['quit']:
            done = True
        elif user_selection == user_option_dict[1]:
            send_thank_you()
        elif user_selection == user_option_dict[2]:
            display_donor_report()


if __name__ == "__main__":
    main()
