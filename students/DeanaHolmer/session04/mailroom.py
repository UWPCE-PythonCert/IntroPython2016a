"""mailroom.py
   Deana Holmer
   Practice with Dictionaries, User Input and Strings"""

# one way to populate tuple-like dictionary with initial values
donors = \
    {   'Chuck': [100,200,300],
        'Mary': [50],
        'Todd': [50,100],
        'Janet': [200,300],
        'Bob': [10,20,30]
    }
# alternate method
menu = {}
menu ['1']="Send a Thank You"
menu ['2']="Create a Report"

def main_menu(menu):
    """Print main menu and return selection."""
    for option in sorted(menu.keys()):
        print ("{}: {}".format(option, menu[option]))
    return(input('Select option> '))

def donor_menu(donors):
    """Print donor menu and return selected name. Print donor list. Add new donor to list. Return name."""
    name=input("Select donor> ")
    if name.lower() == 'list':
        name=input("Select donor:  {} > ".format(sorted(donors.keys())))
    if name not in donors.keys():
        donors.setdefault(name, None)
    return(name)

def donate(donor_name, donors):
    """Get donation amount from user and add to donor dictionary. Return amount."""
    amt=""
    while not amt.isdigit():
        amt=input("Donation amount> ")
    donors[donor_name].append(int(amt))
    return(amt)

def thanks (donor_name, donation_amt):
    """Generate thank you letter for donation. Return text."""
    return ("\nDear {}.\n\tThank you for your donation of ${}. \nSincerely,\n\tUs\n".format(donor_name, donation_amt))

def report(donor_name,donations):
    """Generate donor report"""
    ttl= sum(amt for amt in donations)
    cnt= len(donations)
    avg= int(ttl/cnt)
    return "{}\t{}\t{}\t{}".format(donor_name, ttl, cnt, avg)



if __name__ == '__main__':
    """Present Main Menu and Perform Requested Actions."""
    while True:
        option=main_menu(menu)
        if option== '1':
            donor_name= donor_menu(donors)
            donation_amt=donate(donor_name, donors)
            print(thanks(donor_name, donation_amt))
        elif option=='2':
            print("Name\tTotal\tNum\tAvgAmt")
            for donor_name in donors.keys():
                print(report(donor_name, donors[donor_name]))
        else:
            break


