#!/usr/bin/env python3

# Initial Account Information:
donor_records = {
    'Scrooge McDuck': [
        1000.00,
        2050.00,
        2500.00
    ],
    'Thurston Howell, III': [
        100.00,
        250.00,
        300.00
    ],
    'Ri¢hie Ri¢h': [
        10000.00,
        50000.00,
    ],
    'Montgomery Brewster': [
        40000000.00,
    ],
    'Jed Clampett': [
        1000000.00,
    ],
    'C. Montgomery Burns': [
        0.10,
        0.25,
        0.05,
    ],
}

def send_thank_you(name, amount):
    """Prints out Thank You notes to donors"""
    print("Dear, {}".format(name))
    print("Thank you so much for your donation of ${}!".format(amount))
    print("We very much appreciate all the support.")

def create_report(accounts):
    """Prints out a report of all the donations in the database"""

    donations = []

    # Sum all the donations in all the accounts to sort donation amounts
    for key in accounts:
        donations.append(sum(accounts[key]))

    # Sort the accounts from least generous to most
    donations.sort()

    # Print Headers
    print("{:20}{:16}{:21}{:16}".format("Name", "Donations", "Ave. Amt.", "Total"))
    print("{:20}{:16}{:21}{:16}".format("----", "---------", "---------", "-----"))

    # Iterate backwards through the sorted list
    for i in donations[::-1]:
        for key in accounts:
            # Print accounts associated with the sorted amounts
            # Fix: Assumes no two donors donated the exact amount
            if i == sum(accounts[key]):
                print("{:20}{:4d}        ${:12.2f}    ${:12.2f}".format(key, len(accounts[key]), sum(accounts[key]) / len(accounts[key]), i))

if __name__ == '__main__':
    """Only run this if the script is called directly"""
    is_working = True
    while is_working:
        print("Welcome!  Would you like to:")
        print("(S)end a Thank You?")
        print("(C)reate a Report?")
        print("E(x)it program.")
        option = input("Type 's' for send, and 'c' for create: ")
        if option.lower() == 's':
            is_thanking = True
            while is_thanking:
                name = input("Enter the full name of the person to thank, or type 'list': ")
                if name == 'list':
                    print("List of donors:")
                    for donor in donor_records.keys():
                        print("    {}".format(donor))
                else:
                    if name not in donor_records:
                        donor_records[name] = []
                    verifying_deposit = True
                    while verifying_deposit:
                        donation = input("Enter a donation amount: ")
                        try:
                            float(donation)
                            verifying_deposit = False
                        except ValueError:
                            print("Sorry, you entered an invalid amount.")

                    donor_records[name].append(float(donation))
                    send_thank_you(name, donation)
                    is_thanking = False

        elif option.lower() == 'c':
            create_report(donor_records)
        elif option.lower() == 'x':
            is_working = False
        else:
            print("Sorry, I didn't undertsand your input.")
            print("Please try again...")

    print("Have a nice day!")


