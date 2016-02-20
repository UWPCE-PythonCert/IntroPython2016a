
'''
this is to make a clean start on mailroom 2-13-15
'''


# memo to run the file only if this is a main file

if __name__ == "__main__":
    print("hi there - this is a main file and can run this script directly")
else:
    raise Exception("This file was not created to be imported")

# set up imaginary donor information for use in the script
# input made-up values into a dictionary - very inefficeint - better to pull from a file (but had problems)

d1 = {("Sally Wood"): [50.00, 100.45, 75.25]}
d2 = {("Jim Nasium"): [150.00, 10.00]}
d3 = {("Bill Fold"): [45.00]}
d4 = {("Alice Wonder"): [10.00, 10.00, 25.00]}
d5 = {("Chuck Wheels"): [25.00, 25,25 ]}
d6 = {("No One"): [] }
dictnamelist = [d1,d2,d3,d4,d5,d6]
dictnametuple = (d1,d2,d3,d4,d5,d6)

dictall ={}
dictall.update(d1)
dictall.update(d2)
dictall.update(d3)
dictall.update(d4)
dictall.update(d5)
dictall.update(d6)

dictallsort_val = sorted(dictall,key=dictall.get, reverse = True) # problem: this sorts on the first number, not the sum total

for v in sorted (dictall,key = dictall.get, reverse = True):
    print ("for v in sorted by Value:", v, dictall[v])
    tsum = ( "sum of value = ", sum(dictall[v]))
    print (tsum)
#sumzip = zip (tsum,dictallsort_val)
#print(sumzip[3], sumzip[4])



dictallsort_key = sorted(dictall, reverse = False)

for k in sorted (dictall,  reverse = False):
    print ("for k in sorted by Key " , k, dictall[k])

print ("dictall = ",dictall)
print("dictnamelist =",dictnamelist)
print("dictnametuple = ", dictnametuple)
print("sorted dictallsort_val = ",dictallsort_val )

'''
for x,y in d2:
    d2value = d2.get(x,y)
    print (x ,y)
    print(d2value)

easyvalue = d2.get("Jim", "Nasium")
print(easyvalue)
#sumd2 = sum(d2.values())
#print(sumd2)

k,v = dictall.keys(), dictall.values()
print("this isk:", k)
print ("this is v" , v)


d2a= (d2[1])
print (d2a)
'''

print(sum(dictall["Jim Nasium"]))
print(dictnamelist[1])



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
            if choiceYN == 'y' : print("\tOK - lets do that.", end="")
            if choiceYN == 'n': print("\tOK - let's not do that. Lets go back.")


    except Exception as e:
        print("Error in y/n choice:  " + str(e))
    return str(choiceYN)

def verify_input (responce_to_check, question = "Is this '{}' correct? Please input 'y' or 'n' "):
    """ask for a yes or no confirmation of input"""
    choiceYN = None
    try:
        while choiceYN not in ('y', 'n'):
            #allow user to see if there answer is good
            choiceYN = input(question.format(responce_to_check)).lower()
            print("check to see the value of choice YN", choiceYN)

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
    if fullname in dictall.keys():
        print("That donor is in the donor list.")
        return fullname
    else:
        return None

def split_fname(fullname):
    fname, lname = fullname.split()
    return fname

def split_lname(fullname):
    fname, lname = fullname.split()
    return lname

def add_name_to_db(fullname):
    dictall[fullname] = []
    print("\tAdded {} to the donor database".format(fullname))
    return fullname

def add_donation(fullname):
    donation = None
    while type(donation) != float:
        try:
            donation= float(input("What value of donation would you like to add for {}?".format(fullname)))
        except ValueError as e:
            print("wrong value type - use $$.CC format")
        except Exception as e:
            print("please input you donation amount with $$.CC format")
    print ("donation is: " , donation)
    print("fullname key before", dictall[fullname])
    dictall[fullname] = dictall[fullname] + [donation]
    print("fullname key after", dictall[fullname])

def list_out_donors():
    s_dictall = sorted(dictall.items(),reverse = False)
    print("""
    \t Donors:
    \t--------""")
    for donors, values in s_dictall:
        print("\t\t",donors)

def thank_you_email(fullname):

    fname = split_fname(fullname)
    print("""
        Dear {},

        It is such a pleasure to have you as a supporter.

        Thank you for your donations.

        Regards,

        Duey How

        President """.format(fname))


#start of MAIN

# program welcome
print("\nWelcome to your Donor Management program.")

#call the function that cooresponds to the users selection
while(True):
    # call the menu screen first
    print("\nAll your list options operate through this main menu:")
    menu_display()

    # call the choice function to get the users choice of action
    #print("calling the choice function") #used for testing
    strChoice = num_Choice("Please input your selection from 1-6:",1,7)
    #verifiy choice selection - for routing tracking for debugging
    print("\n\tYour menu choice was: ",strChoice)

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

        #print out the thank you letter to screen
        thank_you_email(fullname)

        #pause before returning user to menu
        pause_foruser()

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
        if dbcheck_name == new_donor_name:
            print("That name, {}, is already on the list of donors.".format(dbcheck_name))
            continue
        else:
            add_name_to_db(dbcheck_name)

        '''
        #*******check to see if they would like to add donations for this donor (new or old name)

        print("would you like to add a donation for {}".format())
        if dbcheck_name == None:
            print("Name not added because already a donor.  Would you like to add donations for this person? ")
            yorn = yornore_Choice()
            if yorn == 'y' : add_donation(new_donor_name)
            else: continue


        else:
            print("dbcheck_name is", dbcheck_name)
            fname, lname = dbcheck_name.split()
            print("added {} to the donor database.  Would you like to add {}'s first donation?".format (dbcheck_name,fname))
            yorn = yornore_Choice()
            if yorn == 'y' : add_donation(dbcheck_name)
            else: continue

        continue
        '''


    # if they choose selection 3 - add new donations for donor
    elif(strChoice == '3'):
        print ("made it to choice {}: add donation".format(strChoice))

        #for user to find name
        res = str(input("would you like to see a list of donors and their donations? y/n").lower())
        if res == 'y':
            print("here is list of donors")
            list_out_donors()

        #check to see if list is on the donor list
        fullname = str(input("type in the full name of the donor."))

        #reply from list
        fullname_on_list = is_name_in_the_list(fullname)

        #if reply is not on list - prompt user to return to menu
        if fullname_on_list == None:
            print("Name not found on donor list.  Please enter donor into system first")
            continue

        #if reply is on the list - then add donation for the user
        else:
            res = 'n'
            while res == 'y':
                add_donation(fullname_on_list)
                res = input("would you like to add donation for this user? y/n").lower()
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

