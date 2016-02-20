# Mailroom Lab
# Student: Chi Kin Ho
# Date: Thursday, January 28, 2016


def display_menu():

    """
        Display the menu of 3 actions: (1) Send a Thank You, (2) Create a Report, or (3) Quit.  If the user
        enters an action other than 1, 2, or 3, the program will prompt him/her to enter an action again
        until the correct action is entered.

        :return: 1, 2 or 3 which corresponds to each of the above three actions.
    """

    # Repeatedly display a menu of 3 actions until the user enters the correct action.
    while True:
        print('\nMenu of 3 Actions')
        print('\t1. Send a Thank You')
        print('\t2. Create a Report')
        print('\t3. Quit')
        action = input('Enter an action: ')

        if action == '1' or action == '2' or action == '3':
            return int(action) # action is correct
        else:
            print('Invalid input.  Please enter either 1, 2 or 3')


def send_a_thank_you(donors_dict):

    while True:
        name = input("Enter the donor's name: " )
        if name == 'list':
            # Display the list of donors' names.
            for donor_name in sorted(donors_dict):
                print(donor_name)
        else:

            # Prompt the user for a donation amount.
            donation_amount = input("Enter a donation amount: $")
            while True:
                try:

                    float(donation_amount)
                except:
                    # Re-prompt the user for a donation amount.
                    donation_amount = input("Enter a donation amount: $")
                else:
                    break

            # Round the donation amount to 2 decimal places.
            donation_amount = round(float(donation_amount), 2)

            # Round the donation ammount to 2 decimal places.
            donation_amount = round(donation_amount, 2)
            if name in donors_dict: # The donor's name is already in the dictionary.
                # Update the donor's record.
                history_of_donations = donors_dict[name]
                history_of_donations[0] += donation_amount # total donated
                history_of_donations[1] += 1 # number of donations
                history_of_donations[2] = round(history_of_donations[0] / history_of_donations[1], 2) # average
            else: # New donor
                # Add the new donor's name and the donation amount to the dictionary.
                donors_dict[name] = [donation_amount, 1, donation_amount]
            # Compose an e-mail thanking the donor for his/her generous donation, and print
            # it on the terminal.
            print('Thank you, {}, for your generous donation!'.format(name))

            # The sending of a thank-you is completed!
            return donors_dict


def create_a_report(donors_dict):
    # Create an inverse dictionary so that it can be sorted by the total donated.
    inverse_dictionary = invert_donor_dictionary(donors_dict)
    for total_donated in sorted(inverse_dictionary):
        donor_lists = inverse_dictionary[total_donated]
        # Display each donor's history of donations.
        for donor in donor_lists:
            print('{:10} {:10.2f} {:10} {:10.2f}'.format(donor[0], donor[1], donor[2], donor[3]))


def invert_donor_dictionary(donors_dict):
    # Create an inverse dictionary so that it can be sorted by the total donated before creating a report.
    inverse_dictionary = dict()

    for donor_name in donors_dict:
        # Get the history of donations of a given donor's name.
        history_of_donations = donors_dict[donor_name]
        # Get the total donated.
        total_donated = history_of_donations[0]
        # Get the number of donations.
        number_of_donations = history_of_donations[1]
        # Get the average amount of donations.
        average_donation = history_of_donations[2]

        # Check whether or not the total donated is already in the inverse_dictionary.
        if total_donated not in inverse_dictionary:
            # If not, add it to the inverse dictionary.
            inverse_dictionary[total_donated] = list()
            inverse_dictionary[total_donated].append([donor_name, total_donated, number_of_donations, average_donation])
        else:
            # Otherwise, append it to the inverse dictionary.
            inverse_dictionary[total_donated].append([donor_name, total_donated, number_of_donations, average_donation])

    return inverse_dictionary


if __name__ == '__main__':
    # Declare a dictionary that stores a list of donor names and the history of the
    # total donated, the number of donations and the average donation amount.
    donors_dict = dict()

    # Populate the dictionary with 5 donors with between 1 and 3 donations each.
    donors_dict['David'] = [99.00, 3, 33.0]
    donors_dict['Bill'] = [20.00, 2, 10.00]
    donors_dict['Andrea'] = [15.00, 2, 7.50]
    donors_dict['Alison'] = [80.00, 1, 80.0]
    donors_dict['Ryan'] = [10.00, 2, 5.00]

    action = display_menu()
    while True:

        if action == 1: # Send a Thank You
            donors_dict = send_a_thank_you(donors_dict)

        elif action == 2: # Create a Report
            create_a_report(donors_dict)

        else: # action == 3 -- Quit
            break

        # Display the menu again and prompt the user for an action.
        action = display_menu()


