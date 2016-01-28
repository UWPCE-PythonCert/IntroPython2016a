
def show_main_menu():
    ''' Present the menu to find out what the user wants to do. '''
    ''' Returns an int giving the menu item selected. '''
    while True:
        print("")
        print("MAIN MENU")
        print("(1) Send a Thank You")
        print("(2) Print Report")
        print("(3) Exit")
        choice = input("Choice --> ")
        try:
            choice = int(choice)
            if choice not in [1, 2, 3]:
                print("Invalid selection. Please try again.")
            else:
                break
        except:
                print("Invalid selection. Please try again.")
        finally:
            pass
    return choice


def print_donors(donor_list):
    ''' Prints a list of the donors to the screen
    :param donor_list: List object containing donor first name, last name, and list of donation amounts
    :return: Nothing
    '''
    print("")
    for idx, donor in enumerate(donor_list):
        print("DONOR: {0:3}  NAME: {1:20}  AMOUNTS: {2}". format(idx, donor[0], str(donor[1])))


def is_donor_in_list(donor_list, full_name):
    ''' Checks if the donor, given by the string full_name, is in the donor_list.
    :param donor_list: List object containing donors full name and list of donation amounts
    :return: True if donor in list, otherwise, false.
    '''
    found = False
    for donor in donor_list:
        if full_name == donor[0]:
            found = True
            break
    return found


def find_donor_idx(donor_list, full_name):
    ''' CHecks if the donor, given by the string full_name, is in the donor_list and returns its index if it is.
    :param donor_list: List object containing donors full name and list of donatino amounts
    :param full_name: Donors full name as a string.
    :return: Integer index giving the location of the donor in donor_list
    '''
    found_at_idx = None
    for idx, donor in enumerate(donor_list):
        if donor[0] == full_name:
            found_at_idx = idx
            break
    return found_at_idx


def thank(donor_list):
    ''' Carries out the tasks necessary to enter, possibly create a new donor,
        add a donation amount to the donor, and create a thank-you letter.
    :param donor_list: List object containing donor first name, last name, and list of donation amounts
    :return: Nothing
    '''
    while True:
        print("")
        full_name = input("[Full Name|'list'|'back'] --> ")
        if full_name == "list":
            print_donors(donors)
            continue
        elif full_name == "back":
            break

        # Adding a donation and printing a thank-you.
        # First check if the donor is in the list already, if not add them.
        if not(is_donor_in_list(donors, full_name)):
            donor_list.append([full_name, []])

        # Get the donation amount...
        while True:
            amnt = input("Donation amount --> ")
            try:
                amnt = int(amnt)
                break
            except:
                print("Invalid donation amount. Please try again. Input only numbers")
            finally:
                pass
        # Find the donor entry in the donor list and append the donation amount
        donor_entry_idx = find_donor_idx(donor_list, full_name)
        donor_entry = donor_list[donor_entry_idx]
        donor_entry[1].append(amnt)

        # Compose thank-you message and print to the terminal
        msg = ("\n"
               "Dear {0}, \n"
               "\n"
               "Thank you for your generous donation of ${1}.\n"
               "Trundle and Biffs all over the world will benefit from your kindness\n"
               "\n"
               "Yours Truely,\n"
               "  Bing Flaherty")
        print(msg.format(full_name, amnt))



def report(donor_list):
    '''Compute number of donations, total donation amount and average donation amount for each user.
       and print results in tabular format to the screen.
    '''
    report_table = []
    for donor in donor_list:
        total_donations = 0
        for amnt in donor[1]:
            total_donations += amnt
        avg_donations = round(total_donations / len(donor[1]), 2)
        report_table.append([donor[0], total_donations, avg_donations])

    # Sort the list by total donation amount
    report_table.sort(key=report_table_sort_by_total_donation_amount_fn, reverse=True)

    # Print sorted donor list to screen
    print("")
    print("-"*80)
    print("{0:20} |  {1:>20} |  {2:>20}".format("NAME", "TOTAL DONATIONS", "AVG DONATION"))
    print("-"*80)
    for donor in report_table:
        print("{0:20} | ${1:>20,.2f} | ${2:>20,.2f}". format(donor[0],
                                                             donor[1],
                                                             donor[2]))
    print("-"*80)


def report_table_sort_by_total_donation_amount_fn(item):
    ''' Returns the second item from the list item given to it
    :param item: A list item
    :return: The second item from the list item
    '''
    return item[1]




if __name__ == "__main__":

    # Print program banner
    print("----------------")
    print("--- Mailroom ---")
    print("----------------")

    # Populate the starting donors database
    donors = list()
    donors.append(["Steve Robertson", [100, 50]])
    donors.append(["Jane Iverson", [10]])
    donors.append(["Pac Liquor", [1000, 5000]])
    donors.append(["Anita Henchman", [10, 25, 75]])
    donors.append(["Zack Wing", [25, 100, 250]])

    # Main kernel of program
    while True:
        choice = show_main_menu()
        if choice in [1]:
            thank(donors)
        elif choice in [2]:
            report(donors)
        else:
            exit()
