import os
import platform
import time
from operator import itemgetter


donor_list = {'Mike Singletary':[50.00, 100.00, 200.00],
                  'Mike Ditka':[300.00, 500.00, 50.00],
                  'Sweetness': [20.00, 700.00],
                  'The Fridge': [900.00, 2000.00],
                  'Dan Hampton': [3000.00]}

donor_final_report_list = {}


def show_main_menu():

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
    print("**************************************************")
    print("                      {}                         ".format(full_name))
    print("*                                                *")
    print("* Choose and option                              *")
    print("* 1. Add a donation                              *")
    print("* 2. Send Thank You email                        *")
    print("* 3. Go Back                                     *")
    print("*                                                *")
    print("**************************************************")
    option = ''
    while not (option == '1' or option == '2' or option == '3'):
        option = input(":")
    if option == '1':
        add_donor_donation(full_name)
    elif option == '2':
        send_email(full_name)
    elif option == '3':
        show_main_menu()


def create_report():

    donors = get_donor_names()

    donor_totals_list = {}

    for name in donors:
        donor_report_list = []

        total_donations = 0.0
        num_of_donations = float(len(get_donor_donations_data(name)))
        donations = get_donor_donations_data(name)

        for donation in donations:
            total_donations += donation

        average_donation = total_donations / num_of_donations
        donor_report_list.append(total_donations)
        donor_report_list.append(average_donation)
        donor_report_list.append(int(num_of_donations))

        donor_totals_list.update({name: total_donations})

        donor_final_report_list.update({name: donor_report_list})

    print("*****************************************************************")
    print("*                            DONOR REPORT                       *")
    print("*                                                               *")
    print("*  NAME                   TOTAL    NUMBER     AVERAGE           *")

    for name,value in sorted(donor_totals_list.items(), key=itemgetter(1), reverse=True):
        donor_report = get_donor_donations_data(name, final=True)
        print("   {0:22}${1:3.2f}{2:8}     ${3:.2f}".format(name, donor_report[0], donor_report[2], donor_report[1]))

    print("*                                                               *")
    print("*****************************************************************")
    input("Press Enter to continue")

    show_main_menu()


def add_donor_donation(full_name):

    donations = []
    print("Please enter a donation amount for {}".format(full_name))
    donation_amount = ''

    while not donation_amount.isdigit():
        donation_amount = input("No decimals please:$")

    donation_amount = float(donation_amount)
    donations.append(donation_amount)
    donor_list.update({full_name: donations})

    print("A ${.2f} donation has been added to {} donation history")
    time.sleep(3)

    donor_management(full_name)


def send_email(full_name):

    donations = get_donor_donations_data(full_name)
    total_donations = 0.0
    for donation in donations:
        total_donations += donation

    print("Dear {},\n".format(full_name))
    print("Thank you for you donations which have totaled up to ${:.2f}!  We greatly appreciate you generosity and you can "
          "be assured that these funds will be put to good use.\n\nIf you have any questions at all, please don't "
          "hesitate to contact me at mgregor@hahaigotyourmoney.com\n\nMichael Gregor\nDirector of Deception".format(total_donations))

    input("\n\n\nPress enter to continue")

    donor_management(full_name)


def clear_screen():

    operating_systems = platform.system()

    if operating_systems == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def get_donor_names():

    donors = get_donor_list()
    names = []

    for name in donors:
        names.append(name)

    return names


def get_donor_donations_data(donar_name, final=False):

    if final == True:
        donors = get_final_report_list()
    else:
        donors = get_donor_list()

    for name in donors:
        if name == donar_name:
            return donors[name]


def get_donor_list():

    global donor_list
    return donor_list


def get_final_report_list():

    global donor_final_report_list
    return donor_final_report_list


def show_donor_list():

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

    show_main_menu()


if __name__ == "__main__":
        main()










