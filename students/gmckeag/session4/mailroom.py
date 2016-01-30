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
    print("""
            Dear {name},

            Thank you for your generous gift of ${amount}.

                 """.format(name=donor, amount=donor_dict[donor][-1]))


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

        prompt_for_donation = False

        user_input = input(prompt)

        if user_input.lower() == 'list':
            list_donors()
        elif user_input in donor_dict:
            prompt_for_donation = True
        elif user_input[0].upper() == 'Q':
            selection = user_option_dict['quit']
        else:
            prompt_for_donation = True

        if prompt_for_donation:
            selection = user_input
            if user_input not in donor_dict:
                donor_dict[user_input] = []
            donation_amount = input('Enter amount of donation $: ')
            try:
                donation_amount = int(donation_amount)
                donor_dict[user_input].append(donation_amount)
            except:
                selection = user_option_dict[0]

    return selection


def send_thank_you():
    """
    """
    selection = get_thank_you_menu_response()
    if selection != user_option_dict['quit']:
        thank_donor(selection)


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