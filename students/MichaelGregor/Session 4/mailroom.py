import os
import platform



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

    return menu_option

def send_thank_you():

    names = get_donor_names()





def create_report():

    print("stuff")


def clear_screen():

    operating_systems = platform.system()

    if operating_systems == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def get_donor_names():
    option = ''
    donors = get_donor_list()
    names = []

    for values in donors:
        donor_name = donors[values]['full_name']
        names.append(donor_name)



def get_donor_list():
    donor_list = {'donor1':{'full_name':'Mike Singletary', 'donations': [50.00, 100.00, 200.00]},
                  'donor2':{'full_name':'Mike Ditka', 'donations': [300.00, 500.00, 50.00]},
                  'donor3':{'full_name':'Sweetness', 'donations': [20.00, 700.00]},
                  'donor4':{'full_name':'The Fridge', 'donations': [900.00, 2000.00]},
                  'donor5':{'full_name':'Dan Hampton', 'donations': [3000.00]}}

    return donor_list

def show_donor_list():

    donor_list = get_donor_list()

    print(donor_list.values())


def main():

    menu_option = show_main_menu()

    if menu_option == '1':
        send_thank_you()
    elif menu_option == '2':
        create_report()
    else:
        print("Thank you for using the Mailroom.")



if __name__ == "__main__":
        main()










