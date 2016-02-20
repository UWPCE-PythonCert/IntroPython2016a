"""
#-------------------------------------------------#
# Title: Mailroom - Week3/4 assignment
# Dev:   BBounds
# Date:  February 14 2016
#Class: Python 2016a
Instructor: Rick Riehle / TA: Summer Rae
#-------------------------------------------------#


Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts
they have donated. This structure should be populated at first with at least five donors, with
between 1 and 3 donations each.  The script should prompt the user (you) to choose from a menu of 2 actions:
     Send a Thank You or Create a Report.


If the user (you) selects "Send a Thank You", prompt for a Full Name.
If the user types "list", show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.

Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isnt.
Once an amount has been given, add that amount to the donation history of the selected user.

Finally, use string formatting to compose an email thanking the donor for their generous donation.
Print the email to the terminal and return to the original prompt.
It is fine to forget new donors once the script quits running.

Creating a Report
If the user (you) selected "Create a Report" Print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular
(values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt. ### NEED HELP  HERE
From the original prompt, the user should be able to quit the script cleanly



What I was not able to accomplish:
  1. to dig into the list of values and pull, say..  donation #2 of 3 from the list in the dictionary's value.
  2. I was not able to answer all my string formatting goals, but i did get pretty good results.  for example, if I
  start up a new print string, (continuing from a prior end="" print line, how do I create a buffer to tell the new print line where
  to start printing using the format print string details.  Also, how do these buffers all line up - for the title row and
  detail row to fit (without trial and error) - do I count up the buffer spaces or something?
  3. was not able to get the sum of the dictionary values to fit in a report with the details of the donations in the same report in a simple way.
  I had to use nested nested loops.

"""

# memo to run the file only if this is a main file

if __name__ == "__main__":
    print("Hi there - this is a main file and you can run this script from here.")
else:
    raise Exception("This file was not created to be imported")

# set up imaginary donor information for use in the script
# input made-up values into a dictionary - very inefficeint - better to pull from a file (but had problems)

d1 = {("Sally Wood"): [50.00, 100.45, 75.24]}
d2 = {("Jim Nasium"): [150.00, 10.01]}
d3 = {("Bill Fold"): [45.00]}
d4 = {("Alice Wonder"): [10.00, 10.00, 25.02]}
d5 = {("Chuck Wheels"): [25.00, 25,25.14 ]}
d6 = {("No One"): [] }

dictall ={}
dictall.update(d1)
dictall.update(d2)
dictall.update(d3)
dictall.update(d4)
dictall.update(d5)
dictall.update(d6)

#play prints
#dictallsort_val = sorted(dictall,key=(dictall.get), reverse = True) # problem: this sorts on the first number, not the sum total


#user choice and menu driving functions:

def pause_foruser():
    waitvalue = input("\nHit any key to proceed.")

def num_Choice(question="Please input a numerical responce in the appropriate range", low=1, high=10):
    """ask for a number within a range from user"""
    choiceNum = None
    try:
        while choiceNum not in range(low, high):
            choiceNum = int(input(question))
    except Exception as e:
        print("Error in Choice: " + str(e))
    return str(choiceNum)

def yornore_Choice(question= "Please input 'y' or 'n' for yes/no. "):
    """ask for a yes or no answer from user"""
    choiceYN = None
    try:
        while choiceYN not in ('y', 'n'):
            choiceYN = input(question)
            if choiceYN == 'y' : print("\tOK - lets do that.", end="  ")
            if choiceYN == 'n': print("\tOK - let's not do that. Lets go back.")

    except Exception as e:
        print("Error in y/n choice:  " + str(e))

    return str(choiceYN)

def verify_input (responce_to_check, question = "Is this '{}' correct? Please input 'y' or 'n' "):
    """ask for a yes or no confirmation of the accuracy of the user's input"""
    choiceYN = None
    try:
        while choiceYN not in ('y', 'n'):
            #allow user to see if there answer is typed correctly
            choiceYN = input(question.format(responce_to_check)).lower()
            #print("in verify input function: check to see the value of choice YN", choiceYN)

            if choiceYN == 'y' :
                print("\tOK - accepted.", end="  ")
            elif choiceYN == 'n':
                print("\tOK - try to input that again.")

            return(choiceYN)

    except Exception as e:
        print("Error in y/n choice:  " + str(e))
    return None

#core menu function:

def menu_display():
    """Display the menu of choices"""
    print ("""
    Menu of Options:
    -----------------
    1) Send a Thank You letter
    2) Add a new Donor
    3) Add new Donations
    4) List Donors' Names
    5) Create a Donor Report
    6) Exit

    """)

#data task functions:

def get_donor_info():
    print("Lets get name data of the donor.")
    fr_name = str(input("what is the first name of the donor?")).title()
    la_name = str(input("what is the last name of the donor?")).title()
    full_name = fr_name + " " + la_name
    #print("this is the full name:",  full_name)
    return full_name

def is_name_in_the_list(fullname,database = dictall):
    if fullname.title() in dictall.keys():
        print("That donor is in the donor list.")
        return ("yes")
    else:
        print("That donor is NOT currently in the donor list.")
        return fullname


def split_fname(fullname):
    fname, lname = fullname.split()
    return fname

def split_lname(fullname):
    fname, lname = fullname.split()
    return lname

def add_name_to_db(fullname):
    #print("in the addname to db function.  this is the full name passed to this add name fucntion", fullname)
    dictall[fullname] = [] #establish name with empty list for donaation
    print("\tAdded {} to the donor database".format(fullname))
    return fullname

def add_donation(fullname):
    donation = None
    while type(donation) != float:
        try:
            donation= float(input("What value of donation would you like to add for {}?".format(fullname)))
        except ValueError as e:
            print("wrong value type - use $$.CC format without commas")
        except Exception as e:
            print("please input you donation amount with $$.CC format")
    print ("Adding a Donation for $: " , donation)
    #print("fullname key's value before", dictall[fullname])
    dictall[fullname] = dictall[fullname] + [donation]
    print("Here is a summary of {}'s donations now.".format(split_fname(fullname)), dictall[fullname])

def list_out_donors():
    s_dictall = sorted(dictall.items(),reverse = False)
    print("""
    \t Donors:
    \t--------""")
    for donors, values in s_dictall:
        print("\t\t",donors)

def list_out_donors_and_donations():
    s2_dictall = sorted(dictall.items(),reverse = False)
    print("{:^15}{:^45}".format("Name","Donations"))
    print("-"*15, " "*15, "-"*15)
    for k,v in s2_dictall:
        print("{:<15}  {:>30}".format(k,str(v)))
    print("\n"*2)

def print_report_sumtotal_summary():
    """Report of the total sum of donations per donor."""
    print("\n\nReport of donors by total historical contributions:")

    s2_dictall = sorted(dictall.items(),reverse = False)

    #create a new dictionary with same keyword name and value is the sum of donations
    sumvalue_dict ={}
    for k, tv in s2_dictall:
        sumvalue_dict[k]= sum(tv)

    # now sort on the values in the new dictionary - to give a list of keys (keys only) by sum of donations
    s_sumvalue_dict_list = sorted(sumvalue_dict,key=sumvalue_dict.get,reverse = True)

    #various print plays to see values
    #print("this is s2 dictall: ", s2_dictall)
    #print("this is the sorted value list: s sumvalue dict list ", s_sumvalue_dict_list)
    #print("this is the new dictionary sumvalue dict ", sumvalue_dict)

    #begin print table
    print("{:^15}{:^45}".format("Name","Donations | Details"))
    print("-"*15, " "*15, "-"*20)
    #print report contents for sorted donor by value of historical donations
    for name in s_sumvalue_dict_list:
        #print(name)
        for n,v in sumvalue_dict.items():
            #print(n,v)
            if name == n:
                print("{:<20} {:>20.2f} ".format(name,v,),end="")
                for k,l in dictall.items():
                    if name == k:
                        #print("{:>60)}".format(str(dictall[k])))
                        print(dictall[k])

     #   print("{:<15}  {:>30}".format(k,str(v)))
    #print("\n"*2)


def print_report():
    """Report of name, count, average, and sum total of donations by donor"""
    print("Report of donor name, count, average, and sum total of their donations. "
          "Sorted by Name - not able to determine sort by total donations!!!")
    s_dictall = sorted(dictall.items(),reverse = False) #sorting list extract of dictionary items (by key alphebetized)
    #print("this is s dictall before formatting: ", s_dictall)
    print("{:<15}{:<8} {:^8}   {:>10} ".format("Name","Count","Average","Sum Total"))
    print("{:^38}".format("-"*46))
    for k,v in s_dictall:
        if sum(v)>0:
            print("{:<15} {:<8} ${:8.2f}    ${:>10.2f}".format(k,len(v),(sum(v)/len(v)),sum(v)) )
        else:
            print("{:<15} {:<8} ${:8.2f}    ${:>10.2f}".format(k,len(v),0.0,sum(v)) )



def thank_you_email(fullname):

    fname = split_fname(fullname)
    print("""
        Dear {},

        It is such a pleasure to have you as a supporter.

        Your total donations of ${:.2f} have been critical to our mission.

        Regards,

        Duey How

        President """.format(fname,sum(dictall[fullname])))


#start of MAIN

# program welcome
print("\nWelcome to your Donor Management program.")

#call the function that cooresponds to the users selection
while(True):
    # call the menu screen first
    print("\nAll your options operate through this main menu:")
    menu_display()

    # call the choice function to get the users choice of action
    #print("calling the choice function") #used for testing
    strChoice = num_Choice("Please input your selection from 1-6:",1,7)
    #verifiy choice selection - for routing tracking for debugging
    #print("\n\tYour menu choice was: ",strChoice, "Got it.")

#menu tasks:

    # if they choose selection 1 - send a thank you letter
    if (strChoice == '1'):
        print ("made it to choice {} : send a donor thank you letter".format(strChoice))

        #provide a list for visibility
        answer = input("do you want to see a list of donors to remind you of the donor's full name? Enter 'y' if you do.").lower()
        if answer == 'y':
            print("here is a recent list of donors.")
            list_out_donors()

        #run routine to get name of the donor you would like to send a letter
        fullname = get_donor_info()

        #let them know if donor is in database or not
        check_name = is_name_in_the_list(fullname)

        #print out the thank you letter to screen if user in database
        if check_name =="yes":
            thank_you_email(fullname)
        else:
            print("\n {} in not in the database.  Unable to write standard letter.".format(fullname))

        pause_foruser() #pause for user to absorb message
        continue

    # if they choose selection 2 - add a new donor
    elif(strChoice == '2'):
        print ("made it to choice {} : add a new donor".format(strChoice))

        #start ruitine to collect the first and last name of the donor
        new_donor_name = get_donor_info()
        print (new_donor_name)

        # allow user to verify they typed the name correctly
        happy_new_donor_name_yn = verify_input(new_donor_name)

        #if name is acceptable to user, see if it is already in the database of donors
        if happy_new_donor_name_yn == "y":
            dbcheck_name = is_name_in_the_list(new_donor_name,dictall)
        else: #returning to main menu for re-try a name error (maybe misspelled)
            print("Returning to main menu so you can try to re-enter your data.")
            continue

        #add if new name is new, or return to menu if not a new name
        if dbcheck_name == "yes":
            print("That name, {}, is already on the list of donors.".format(dbcheck_name.title()))
            continue
        else:
            print("Adding name to donor list.")
            add_name_to_db(new_donor_name)


    # if they choose selection 3 - add new donations for donor
    elif(strChoice == '3'):
        print ("made it to choice {}: add donation".format(strChoice))

        #for user to find name
        res = str(input("would you like to see a list of donors and their donations? y/n").lower())
        if res == 'y':
            print("Here is list of donors with their current donations on record.")
            list_out_donors_and_donations()

        #check to see if list is on the donor list
        fullname = str(input("type in the full name of the donor."))

        #reply from list
        fullname_on_list = is_name_in_the_list(fullname)

        #if reply is not on list - prompt user to return to menu
        if fullname_on_list == "yes":
            res2 = 'n'
            res2 = input("would you like to add donation for this user? y/n").lower()
            while res2 == 'y':
                add_donation(fullname.title())
                res2 = input("would you like to add another donation for this user? y/n").lower()
            continue

        #if reply is on the list - then add donation for the user
        else:
            print("Name not found on donor list.  Please enter donor into system first")
            continue


    # if they choose selection 4 - print list of donor names
    elif(strChoice == '4'):
        print ("made it to choice {} : print list of donor names".format(strChoice))

        list_out_donors()

        pause_foruser()
        continue

    # if they choose selection 5 - output donor report
    elif(strChoice == '5'):
        print ("You made it to choice {}:  Output Donor report".format(strChoice))
        print_report()
        print_report_sumtotal_summary()


        pause_foruser()
        continue
        # if they choose selection 6 - exit
    elif(strChoice == '6'):
        print ("You made it to choice {} : exit".format(strChoice))
        choice = yornore_Choice("\tAre you sure you want to exit? ")
        if choice == "y":
            print("\n\tElvis has left the building.  Good bye.")
            break
        else:
            print("\nOK, Lets go back to the menu.")
            continue
    else:
        print("You should not have made it to here.  There must be a problem in the while loop.")
        break

#salutation to the user
print("\nSee you next time.")
