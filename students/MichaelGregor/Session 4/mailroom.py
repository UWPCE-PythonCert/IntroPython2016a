import os
import platform


donor_list = {'Mike Singletary':[50.00, 100.00, 200.00],
                  'Mike Ditka':[300.00, 500.00, 50.00],
                  'Sweetness': [20.00, 700.00],
                  'The Fridge': [900.00, 2000.00],
                  'Dan Hampton': [3000.00]}

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
            create_new_donor(full_name)
        else:
            show_main_menu()
    elif full_name in get_donor_names():

        print("**************************************************")
        print("                      {}                         ")
        print("*                                                *")
        print("* Choose and option                              *")
        print("* 1. Add a donation                              *")
        print("* 2. Send Thank You email                        *")
        print("*                                                *")
        print("**************************************************")

        option = ''
        while not (option == '1' or option == '2'):





def create_new_donor(new_donor):

    donations = []
    print("Please enter a donation amount for {}".format(new_donor))
    donation_amount = ''

    while not donation_amount.isdigit():
        donation_amount = input("No decimals please:$")

    donation_amount = float(donation_amount)
    donations.append(donation_amount)
    donor_list.update({new_donor: donations})

    show_main_menu()

def create_report():

    print("stuff")


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

def get_donor_donations(donar_name):

    donors = get_donor_list()

    for name in donors:
        if name == donar_name:
            return donors[name]

def get_donor_list():

    global donor_list
    return donor_list

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










