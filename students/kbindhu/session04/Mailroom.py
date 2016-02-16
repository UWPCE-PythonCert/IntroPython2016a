#!/usr/bin/python
#kbindhu
#Date created:1/20/2015


#function to display menu
def MenuDisp():
    print("Main Menu")
    print("1. Send a Thank you")
    print("2. Create Report")
    print("3.Exit")


#function for thank u card
def ThankYouCard():
    keep_going=True
    while keep_going:
        name=input('Please enter full name or type list to see full list of donors: ')
        if(name.casefold()=='list'):
            #call display function to display all donors
            DonorNameDisp()
        elif(name.casefold() not in don_dict):
            #call function to add the name to dict
            AddDonorToDict(name)
            #call function for calculation of  donation amount
            Amount=DonationAmountReceive()
            #add amout donated and number of donations to existing history
            don_dict[name.lower()][0]=don_dict[name.lower()][0]+1
            don_dict[name.lower()][1]=don_dict[name.lower()][1]+Amount
            keep_going = False
        elif(name.casefold() in don_dict):
            print("Hello {},Welcome Back".format(name.capitalize()))
            #call function for prompt a donation amount
            Amount=DonationAmountReceive()
            #add amout donated and number of donations to existing history
            don_dict[name.lower()][0]=don_dict[name.lower()][0]+1
            don_dict[name.lower()][1]=don_dict[name.lower()][1]+Amount
            keep_going=False
        else:
            print("Invalid option ....Try again")
    ThankEmail(name)
    return don_dict


#thanku email generation
def ThankEmail(name):
    print('')
    print("Email to Donor")
    print("From:kbindhu@example.com")
    print("To:{}@example.com".format(name))
    print("Subject:Donation")
    print("Hi {},".format(name.capitalize()))
    print('{:>50}'.format('Thank for your donation at example charity.'))
    print('{:<30}'.format('Regards'))
    print('{:<30}'.format('krishna Bindhu'))
    print('')




#function which print donor names as a list
def DonorNameDisp():
    for key in don_dict.keys():
        print(key.capitalize())

#function to add new donors to dictionary
def AddDonorToDict(name):
    name = name.lower()
    don_dict.setdefault(name, []).append(0)
    don_dict.setdefault(name, []).append(0)

#function to prompt for a donation amount
def DonationAmountReceive():
    while True:
        donationAmount=input('Enter amount for donation: ')
        #checking validity of amount enetered
        try:
            donationAmount=float(donationAmount)
            break
        except ValueError:
            print("Input must be integer,try again")
    return donationAmount


def CreateReport(don_dict):
    # writing keys and values of dictionary to list which can be easy to sort
    don_dict_list=[]
    for k in don_dict.keys():
        Num_of_donations=don_dict[k][0]
        Amt_of_don=don_dict[k][1]
        #calculating average
        Avg=don_dict[k][1]/don_dict[k][0]
        don_dict_list.append([k.capitalize(),Num_of_donations,Amt_of_don,Avg])

#sorting the list using amout donated using itemgetter
    from operator import itemgetter
    sorted_don_dict_list= sorted(don_dict_list,key=itemgetter(2))

#printing to a table

    from tabulate import tabulate
    print("")
    print (tabulate(sorted_don_dict_list,headers=["DonorName","Number of Donations","Amount Donated(dollars)","Average"]))
    print('')



#main function
if __name__ == "__main__":
    keep_going = True
    #creating a dictionary
    don_dict=dict()
    #populating dictionary with no of donations and donors names
    don_dict.setdefault('adam', []).append(5)
    don_dict.setdefault('bob', []).append(3)
    don_dict.setdefault('cathy', []).append(4)
    don_dict.setdefault('andy', []).append(1)
    don_dict.setdefault('phil', []).append(2)
    #populating  dictionary with amount of donations
    don_dict.setdefault('adam', []).append(100)
    don_dict.setdefault('bob', []).append(400)
    don_dict.setdefault('cathy', []).append(20)
    don_dict.setdefault('andy', []).append(10)
    don_dict.setdefault('phil', []).append(250)
    MenuDisp()

#Main Program
    while True:
        menu= input('Enter 1 for option1 , 2 for option2 or 3 for option3:  ')
        if(menu=='1'):
            #call thank u function
            don_dict_new=ThankYouCard()
            don_dict=don_dict_new
            MenuDisp()
        elif(menu=='2'):
            #call create report function
            CreateReport(don_dict)
            MenuDisp()
        elif(menu=='3'):
            from sys import exit
            exit()
        else:
            print("Wrong option selected")













