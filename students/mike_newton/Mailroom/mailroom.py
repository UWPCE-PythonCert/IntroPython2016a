'''______________________________________________________
Mike Newton
newton33@uw.edu
Intro To Python 100A
University of Washington, Winter 2016
Last Updated:  02 February 2016
Python Version 3.5.1

Mailroom Exercise
http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/mailroom.html

______________________________________________________'''


#------------ Introduction -------------------
#Explain to the user what the script will accomplish
print("This script will read in a file containing data describing the frequency and amount of donations provided"
      " by specific individuals.  If the file does not exist, you will be prompted to enter donor information in'"
      " order to create the list.  You will then be allowed to edit this data or send a Thank You email to '"
      "each donor.\n\n" "You may type the word 'quit' at any time to exit the program.\n")


#-------------- Get Data ------------------------
#define a function to read the To Do list
#@staticmethod
def read_Donations(file):
    donation_data = [] #initialize a list of dictionaries
    raw_donor_data = []
    #loop through DonorList.txt and places the data into dictionaries
    for line in file:
        #read in the raw data from the file
        raw_donor_data.append([(line.strip().split(",")[0]), float((line.strip().split(",")[1]))])

    #now form the key-value pairs in raw_donor_data into a dictionary of lists
    #I'll try the defaultdict subclass in the collections module.  I've never tried that before.
    from collections import defaultdict
    donation_data = defaultdict(list)
    for k, v in raw_donor_data:
        donation_data[k].append(v)

    return donation_data

#-------------- Process Data ------------------------
#define a function that will accept the donor data and determine the following values
#1. number of donations made
#2. total amount of donations
#3. average donation amount
def do_math(data):
    donor_math = {}
    for k, v in data.items():
        # v is the list of donations for each donor (k)
        total = sum(v)
        num = len(v)
        avg = total/num
        donor_math[k] = num, total, avg

    return donor_math

#-------------- Present Data ------------------------
#create a function that will format data and display it in a pleasing fashion
def display_donor_data(data):

    #in order to make the user diplay more visually appealing, we need to figure out
    # the max lengths in each 'column'
    name_len = []
    num_len = []
    total_len = []
    avg_len = []

    #loop through key/value pairs to determine max length in each field
    for k, v in data.items():

        name_len.append(len(k))
        num_len.append(len(str(v[0])))
        total_len.append(len(str(v[1])))
        avg_len.append(len(str(v[2])))

    #now determine if data field lengths are greater than the header lengths.  whichever length is greater will be
    #our column widths.  there must be a more elegant way of doing this but it works for now.
    # any advice would be appreciated.
    if max(name_len) > len("Donor Name"):
        name_col_width = max(name_len)
    else: name_col_width = len("Donor Name")
    if max(num_len) > len("Number of Donations"):
        num_col_width = max(num_len)
    else: num_col_width = len("Number of Donations")
    if max(total_len) > len("Total Donations($)"):
        total_col_width = max(total_len)
    else: total_col_width = len("Total Donations($)")
    if max(avg_len) > len("Average Donation"):
        avg_col_width = max(avg_len)
    else: avg_col_width = len("Average Donation")

    #in order to use the python .format method to format the string.
    # this took me a while to truly figure out.
    header_format_string = "{0:^" + str(name_col_width+5) + "s} {1:^" + str(num_col_width+5) + "s}" \
                            " {2:^" + str(total_col_width+5) + "s} {3:^" + str(avg_col_width+5) + "s}"
    data_format_string = "{0:^" + str(name_col_width+5) + "s} {1:^" + str(num_col_width+5) + "s} " \
                            "{2:^" + str(total_col_width+5) + "s} {3:^" + str(avg_col_width+5) + "s}"


    #first display some headers so the data doesn't look like random words and numbers
    print(header_format_string.format("Donor Name", "Number of Donations", "Total Donations($)", "Average Donation"))
    print(header_format_string.format("----------", "-------------------", "------------------", "----------------"))

    #data should be sorted by total donation amount.  dictionaries aren't ordered so a different approach is needed.
    #we'll need a list representation of our data.  a list of tuples, i believe is how this works out.
    sorted_data = sorted(data.items(), key=lambda v: v[1][1], reverse = True)

    #loop through data to print to terminal.  it's probably better to format the data in a different fashion prior this
    #point but here we are.
    for i, f in enumerate(sorted_data):
        print(data_format_string.format(sorted_data[i][0], str(sorted_data[i][1][0]), str(sorted_data[i][1][1]), str(sorted_data[i][1][2])))


def display_donor_list(data):
    #this function will display a list donor names to the user

    #in order to make the user diplay more visually appealing, we need to figure out
    # the max lengths in each 'column'
    name_len = []
    #loop through key/value pairs to determine max length in each field
    for k, v in data.items():
        name_len.append(len(k))

    if max(name_len) > len("Donor Name"):
        name_col_width = max(name_len)
    else: name_col_width = len("Donor Name")

    #in order to use the python .format method to format the string.
    # this took me a while to truly figure out.
    header_format_string = "{0:^" + str(name_col_width+5) + "s}"
    data_format_string = "{0:^" + str(name_col_width+5) + "s}"

    #first display some headers so the data doesn't look like random words and numbers
    print(header_format_string.format("Donor Name"))
    print(header_format_string.format("----------"))

    #now display the donor names
    for k in data:
        print(data_format_string.format(k))

def add_to_donor_data(data, name, donation):
    #create a function add a new donor to the list or add a new donation for an existing donor
    if name in data:
        data[name].append(donation)
    else:
        data[name] = donation

    return data

def send_thanks_option(data):
    #create a function which will add new donors/donations to the data and send a thank you email
    print("You've chosen to enter a new donation and send a 'Thank You' email.\n")
    #user may now enter the name or donor or type 'list' to see a list of previous donors
    while True:
        user_name_input = input("Enter the name of the donor or type 'list' to see a list of previous donors.\n")
        if user_name_input.lower() == "list":
            display_donor_list(data)
        else:
            break

    #now user should enter a donation amount.  if the input isn't a number, an exception will be raised
    while True:
        try:
            donation_amt = float(input("How much did " + user_name_input + " donate?\n"))
            break
        except ValueError:
            print("I don't think that was a dollar amount.  Try again.")
    #add this new donation to the donor data
    data = add_to_donor_data(data, user_name_input, donation_amt)

    print(data)


#-------------- Main User Interactions ------------------------
if __name__ == '__main__':

    #------------ Open/Create The Current Donor List -------------------
    #open the Donations.txt file which resides int he same folder on the C: drive as this script
    save_dir = "C:\Python Certificate\Python_100A\Mailroom"
    print("Retrieving file from " + save_dir + " directory\n")
    # open/create the Donations.txt file in the given directory
    file = open(save_dir + "\Donations.txt", 'r+')

    #----------interact with user and do stuff with data----------
    #read donations file before doing anything
    donor_data = read_Donations(file)

    #now ask the user what to do.  the options are to enter a donation and send a thank you email
    #or generate a report of historical donations

    option = input("Greetings!  What would you like to do?\n"
                   "[1] Enter a new donation amount and send a 'Thank You' email?\n"
                   "[2] Generate a historical report of donations\n"
                   "Type 1 or 2 and press enter for one of the options above or type quit to exit.\n")

    #if option == 1:


    #donor_math = do_math(donor_data)
    #display_donor_data(donor_math)
    #display_donor_list(donor_data)


    #donor_data = add_to_donor_data(donor_data, user_name_input, donation_amt)
    send_thanks_option(donor_data)
    print(donor_data)
    file.close()