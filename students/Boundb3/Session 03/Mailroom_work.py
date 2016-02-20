"""
#-------------------------------------------------#
# Title: Mailroom - Week3/4 assignment
# Dev:   BBounds
# Date:  February 1 2016
#Class: Python 2016a
Instructor: Rick Riehle / TA: Summer Rae
#-------------------------------------------------#


Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts
they have donated. This structure should be populated at first with at least five donors, with


between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 2 actions:
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


"""
# memo to run the file only if this is a main file

if __name__ == "__main__":
    print("hi there - this is a main file and can run this script directly")
else:
    raise Exception("This file was not created to be imported")

# set up imaginary donor information for use in the script
dictall ={}

# input made-up values into a dictionary - very inefficeint - better to pull from a file (but had problems)

d1 = {("Sally", "Wood", "Ms."): [50.00, 100.45, 75.25]}
d2 = {("Jim", "Nasium", "Mr."): [150.00, 10.00]}
d3 = {("Bill", "Fold", "Mr."): [45.00]}
d4 = {("Alice", "Wonder", "Mrs."): [10.00, 10.00, 25.00]}
d5 = {("Chuck", "Wheels", "Mr."): [25.00, 25,25 ]}
d6 = {("no", "one", "yet"): [] }
dictnamelist = ["d1","d2","d3","d4","d5","d6"]
dictall.update(d1)
dictall.update(d2)
dictall.update(d3)
dictall.update(d4)
dictall.update(d5)
dictall.update(d6)

print ("Here is the printout of dictall = ",dictall)


# for fun, unpack the key and make a new key in a new dictionary with re-ordered values (like in a letter)
dictsalutation = {}
sdictsalutation = {} #sorted dic

def print_report():

    print("\n\t  Donor's Report: \n\t _________________\n")
    count = 0
    nameall =(),
    for tplKey, lstValue in dictall.items(): # dictionary as it is first built up
        #print(strKey + " / " + strValue + "\t")
        #print("type ofkey",type(strKey))
        firstn = tplKey[0]
        lastn = tplKey[1]
        saluten = tplKey[2]
        nameall = (saluten, firstn, lastn)
        dictsalutation[nameall] = lstValue
        count +=1
    #print("{} item(s) added to dictionary. Here is dictionary now: {}".format(count,dictsalutation))

    for tplKey, lstValue in dictsalutation.items(): # preparing to try a sorted dictionary

        donations = sum(lstValue)
        count = (len(lstValue))
        avg_donation = 0
        try:
            avg_donation = donations/count
        except ZeroDivisionError:
            avg_donation = 0
        except Exception as e:
            print(e)

        print("{} {} {} has made {:d} donation(s) for a total of ${:f}"
        " (which is an ave of {:f})".format(tplKey[0],tplKey[1],tplKey[2],len(lstValue),sum(lstValue),avg_donation))

    input("\n\ttype any key to continue")

'''
print_report()
print("ran print report")
print("this is print of dictall", dictall)
print("*****")
print(dictsalutation)
print("***** - now sorted")
print(sorted(dictsalutation))
print("***** - now back to unsorted - is it still there?")
print(dictsalutation)
'''

def print_thanks(donors_fullname):
    print("Thank you ",donors_fullname)
    print("need to format a thank ou letter")

def add_new_donor():
    donor_fname = input("What is the new donor's first name?").title
    f = (donor_fname)
    donor_lastn = input("What is the new donor's last name?").title
    l = (donor_lastn)
    donor_salutation =  input("What is the donor's salutation for a letter? i.e: Mr. or Mrs?").title
    mr =(donor_salutation)
    key = (f , l , mr)
    print("the type of key created to dictionary is: ", type(key), "is" , key)
    print("Thank you, got the new donor.  Now I will post to the dictionary.")
    add_new_donor_to_dictionary(key)

def add_new_donor_to_dictionary(unposted_new_donor):
    f,l,mr = unposted_new_donor
    if (f,l,mr) in dictsalutation:
        print("{} already in dictionary.".format(unposted_new_donor))
        return
    else:
        dictall[(f,l,mr)] = [] #update the dictionary with a new key with empty list value
        dictsalutation[(f,l,mr)] = [] #update the salutation dictionary too (with new key with empty list value
        message = "Completed set up of new donor (added to dictionary):"
        print ("{} {}".format(message,unposted_new_donor))
        return unposted_new_donor


"""Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isnt.
Once an amount has been given, add that amount to the donation history of the selected user.
"""

def add_new_donations(key_name):
    new_donation_Q= input("Has {} provided a new donation? Type 'yes' or 'no'".format(key_name)).lower
    a= verify(new_donation_Q)
    if key_name in dictall:

        lstValueNew =[]
        if a == "yes":
            donation_amount = int(input("What is the amount of the donation?"))
            try:
                b = int(verify(new_donation_Q))
            except Exception as e:
                print(e, "is not a valid number.  value not excepted" )
                return None
            lstValueNew.append(b)

            dictall[key_name] = lstValue
            dictsalutation[key_name] = lstValue
            print("Ive updated that: Donor {} provided {:d} in a donation").format(key_name,lstValue)
    else:
        print("name {} not found. Try again.". format(key_name))

    return

def list_donors():
    ''' screen print list of donors in a table'''
    print("temp# \t donor name \t\t donation history \n "
          "--------------------------------------------------------")
    count = 0

    for tplkey, lstvalue in dictsalutation.items():

        print ("No: {} \t {} \t\t {}".format((count+1),(tplkey[0],tplkey[1],tplkey[2]),lstvalue),sep="\t\t")
        count += 1
    input("\n\ttype enter to proceed")

# create a menu



print_report()

while(True):
    print ("""
    Menu of Options:
    -----------------
    1) Send a Thank You letter
    2) Add a new Donor
    3) Add new Donations
    4) List Donors
    5) Create a Report
    6) Exit

    """)
    strChoice = str(input("Which option would you like to perform? [1 to 6]"))

    # 1 send thank you letter

    '''
    If the user (you) selects "Send a Thank You", prompt for a Full Name.
If the user types "list", show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
'''
    if (strChoice == '1'):
        full_name = input("Please enter the:"
        "1)full name and title of the donor, or"
        "2)'list' to see a list of donors, or"
        "3)'exit' to quit ").title
        if full_name == "exit":
            break
        elif full_name == "list":
            list_donors()
            continue

        elif full_name in dictsalutation:
            print("found it in dictsalutation")
            print_thanks(full_name)
            continue
        else:
            #*********
            print("I do not see this name in the list.")
            full_name = verify(full_name)
            answer = input("Would you like to try again or add {} name to the list?".format(full_name))
            if answer == "try again":
                break
            else:
                print("Ok, We will add {} to the list.  Lets collect the details one at a time.".format(full_name))
                created_new_donor_tpl = add_new_donor()
                add_new_donations(created_new_donor_tpl)
                print_thanks(created_new_donor_tpl)



    # 2 add new donor
    elif(strChoice == '2'):
        print("please check that the donor is not already on the list")
        list_donors()
        answer = input("do you still want to add the new donor? Type yes or no")
        a = (answer)
        if a == 'yes':
            add_new_donor()
        continue


    #3 add new donation
    elif(strChoice == '3'):
        print("please find your donor on the list below")
        list_donors()
        keynametry = input("please type the donors full name")
        add_new_donations(keynametry)
        continue


    #4 list donors
    elif(strChoice == '4'):
        print("Here is a list of donors:")
        list_donors()
        continue

    #5 create a report
    elif(strChoice == '5'):
        print_report()
        continue


    #6 Quit
    elif(strChoice == '6'):
        print("Thank you.  Have a good day.")
        break



'''


print (dictall)




print (d5.keys())
print (d4.items())
print (d3.values())

for strKey, strValue in dicTable.items():
            print(strKey)
        strKeyToRemove = input("Which item would you like removed?")
        if(strKeyToRemove in dicTable):
            del dicTable[strKeyToRemove]
        else:
            print("I'm sorry, but I could not find that item.")
        print(dicTable) #For testing
        continue


        elif(strChoice == '6'):
        objFile = open(objFileName, "w")
        for strKey, strValue in dicTable.items():
            objFile.write(strKey + "," + strValue + "\n")
        objFile.close()
        break
'''
