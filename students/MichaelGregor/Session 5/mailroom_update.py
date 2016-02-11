import os
import platform
from operator import itemgetter

# Create global dictionaries so that multiple methods can used them for data flow control

donor_list = {'Mike Singletary':[50.00, 100.00, 200.00],
                  'Mike Ditka':[300.00, 500.00, 50.00],
                  'Sweetness': [20.00, 700.00],
                  'The Fridge': [900.00, 2000.00],
                  'Dan Hampton': [3000.00]}

donor_final_report_list = {}

ap = os.path.abspath('mailroom_update')


def show_main_menu():
    """
    Shows the main menu and is the beginning of the control flow

    :return: None
    """

    menu_option = ''

    while not (menu_option == '1' or menu_option == '2' or menu_option == '3'):
        clear_screen()

        print("**************************************************")
        print("**************************************************")
        print("*                                                *")
        print("*                 THE MAILROOM                   *")
        print("*                                                *")
        print("**************************************************")
        print("*                                                *")
        print("* What would you like to do today?               *")
        print("* 1. Send a Thank you                            *")
        print("* 2. Create a Report                             *")
        print("* 3. Exit Program                                *")
        print("*                                                *")
        print("**************************************************")
        print("**************************************************")
        menu_option = input(":")

    if menu_option == '1':
        send_thank_you()
    elif menu_option == '2':
        create_report()
    else:
        print("Thank you for using The Mailroom!")


def send_thank_you():
    """
    Launches the Send Thank You control flow. Use to list the current donors available or create a new donor.

    :return:  None
    """

    full_name = input("Please provide the full name: ")

    if full_name == "list":
        show_donor_list()

    elif full_name not in get_donor_names():

        create_new_name = ''

        while not (create_new_name == '1' or create_new_name == '2'):

            print(("{} is not in the current list of donors\n Do you wish to create a new donor?".format(full_name)))
            print("1. Yes")
            print("2. No")
            create_new_name = input(":")

        if create_new_name == '1':
            add_donor_donation(full_name)
        else:
            show_main_menu()
    elif full_name in get_donor_names():

        donor_management(full_name)


def donor_management(full_name):
    """
    This function is used to Add donations to a specific donor and to trigger the final thank you email.

    :param full_name: The name of the donor who we are adding a donation to or sending email
    :type full_name: String
    :return: None
    """

    option = ''

    while not (option == '1' or option == '2' or option == '3'):

        clear_screen()
        print("**************************************************")
        print("                {}                         ".format(full_name))
        print("*                                                *")
        print("* Choose and option                              *")
        print("* 1. Add a donation                              *")
        print("* 2. Send Thank You email                        *")
        print("* 3. Go Back                                     *")
        print("*                                                *")
        print("**************************************************")
        option = input(":")

    if option == '1':
        add_donor_donation(full_name)
    elif option == '2':
        send_email(full_name)
    elif option == '3':
        show_main_menu()


def create_report():
    """
    This prints a report of all the donors, their total donation amount, number of donations, and average

    :return:
    """

    clear_screen()

    donors = get_donor_names()

    donor_totals_list = {}

    for name in donors:                                                 # We need to get each donor and start to collect
        donor_report_list = []                                          # data to build the report.

        total_donations = 0.0
        num_of_donations = float(len(get_donor_donations_data(name)))
        donations = get_donor_donations_data(name)

        for donation in donations:                                      # All the donor donations are in List format so
            total_donations += donation                                 # so we have to iterate through each donation
                                                                        # and total them together.
        average_donation = total_donations / num_of_donations
        donor_report_list.append(total_donations)                       # Here we begin to build a new Dictionary object
        donor_report_list.append(average_donation)                      # to hold the data we need for the final report.
        donor_report_list.append(int(num_of_donations))

        donor_totals_list.update({name: total_donations})               # We create a new totals dictionary object so
                                                                        # so we can use it later to sort the report by
        donor_final_report_list.update({name: donor_report_list})       # total amount of donations.

    print("*****************************************************************")
    print("*                        DONOR REPORT                           *")
    print("*                                                               *")
    print("   {0:20}     {1:7} {2:9}{3:5}".format("NAME", "TOTAL", "NUMBER", "AVERAGE"))


    # Woot, my only stack overflow answer in this program.  So we are sorting each name in the dictionary by the
    # donor_totals_list.  This will by default sort smallest to largest.  The 'reverse=True' statement allows the
    # us to sort the names by the donation total largest to smallest.  We then iterate through each name, gather a
    # the donor report which is a List item pulled from the global donor_final_report_list and format the output in
    # the print statement.

    for name,value in sorted(donor_totals_list.items(), key=itemgetter(1), reverse=True):
        donor_report = get_donor_donations_data(name, final=True)
        print("   {0:20}  ${1:9} {2:7}  ${3:.2f}".format(name, donor_report[0], donor_report[2], donor_report[1]))

    print("*                                                               *")
    print("*****************************************************************")
    input("Press Enter to continue")

    show_main_menu()


def add_donor_donation(full_name):
    """
    This adds a donation amount to a specific donor.

    :param full_name: Name of the donor that we are adding a donation too.
    :type full_name: String
    :return: Donor name (full_name)
    """

    donations = get_donor_donations_data(full_name)
    print("Please enter a donation amount for {}".format(full_name))
    donation_amount = ''

    while not donation_amount.isdigit():                                # Check to make sure the donation amount is a
        donation_amount = input("No decimals please:$")                 # a integer number as a string to prevent
                                                                        # weird data being entered.
    donation_amount = float(donation_amount)                            # We then cast it as a float before we add it
    donations.append(donation_amount)                                   # to the donor's donations for easy math later.
    donor_list.update({full_name: donations})

    print("A ${:.2f} donation has been added to {}'s donation history".format(donation_amount, full_name))
    input("Press Enter to continue")

    donor_management(full_name)


def send_email(full_name):
    """
    Formats an email and prints it to the screen.

    :param full_name: Donor Name
    :type full_name: String
    :return: Donor Name (full_name)
    """

    donations = get_donor_donations_data(full_name)
    total_donations = 0.0
    for donation in donations:
        total_donations += donation

    header = ("Dear {},\n".format(full_name))
    body = ("Thank you for your donations which have totaled up to ${:.2f}!  We greatly appreciate your generosity and you can "
            "be assured that these funds will be put to good use.\n\nIf you have any questions at all, please don't "
          "hesitate to contact me at mgregor@hahaigotyourmoney.com\n\nMichael Gregor\nDirector of Deception".format(total_donations))

    input("File written to disk.\nPress enter to continue")

    f = open('{}_Letter.txt'.format(full_name), 'w+')
    f.write(header + '\n')
    f.write(body + '\n')
    f.close()

    donor_management(full_name)


def clear_screen():
    """
    Determines what operating system is currently running and executes the applicable command line argument to clear
    the screen.

    :return: None
    """

    operating_systems = platform.system()

    if operating_systems == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def get_donor_names():
    """
    Iterates through our donor list and returns the names (i.e. the Keys for the donor dictionary objects)

    :return: Donor names as a List object (names)
    """

    donors = get_donor_list()
    names = []

    for name in donors:
        names.append(name)

    return names


def get_donor_donations_data(donar_name, final=False):
    """
    Gets the donation data for a particular donor.

    :param donar_name: Donor name
    :type donar_name: String
    :param final: Checks to see if we are getting data for the final report
    :type final: Bool

    :return: Returns the List Object inside the applicable donor dictionary (donor[name])
    """

    if final == True:
        donors = get_final_report_list()
    else:
        donors = get_donor_list()

    for name in donors:
        if name == donar_name:
            return donors[name]


def get_donor_list():
    """
    Gets the global donor list

    :return: Dictionary Object of Donors and their donations (donor_list)
    """

    global donor_list
    return donor_list


def get_final_report_list():
    """
    Gets the global donor final report

    :return:  Dictionary Object of Donors and their total donation amount, number of donations, and average
              donation (donor_final_report_list)
    """

    global donor_final_report_list
    return donor_final_report_list


def show_donor_list():
    """
    Show the list of donor names

    :return: None
    """

    clear_screen()

    names = get_donor_names()

    print("**************************************************")
    print("*                                                *")
    print("*                   DONORS                       *")
    print("*                                                *")
    for name in names:
        print("                  {}                          ".format(name))
    print("*                                                *")
    print("**************************************************")

    send_thank_you()


def main():
    """
    Launches Program

    :return: None
    """

    show_main_menu()


if __name__ == "__main__":
        main()










