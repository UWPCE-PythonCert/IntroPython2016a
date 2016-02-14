#!/usr/bin/env python 

def main_command():
    while True:
        user_choice = input("Type 1 for Send a Thank You; Type 2 for Create Report: Type 3 to quit: ->")
        try:
            user_choice = int(user_choice)
            if user_choice not in [1, 2, 3]:
              print("Invalid selection. Please try again.")
            else:
              break
        except:
            print("Invalid selection. Please try again.")
        finally:
            pass
    return user_choice



def donor_name():
    for i in dln.keys():
        print(i) 

def Sending_a_Thank_You():
    prompt = True
    while prompt: 
        full_name = input("Full Name: |'list'| ->")
        if full_name == 'list':
           donor_name()
           prompt = True
        elif full_name == 'main':
           break
        elif full_name in dln.keys():
           prompt = False
        else:        
            dln[full_name] = []
            prompt = False
    promptN = True
    while promptN:
        donation = input("Donation Amount: ->")
        try:
            val = int(donation)
        except ValueError:
            promptN == True
            continue
        else:
            break
    dln[full_name] += [int(donation)]
    print ("Thank you, {name}, for your generous donation of {amount}".format(name = full_name, amount = int(donation)))

def getKey(item):
    return item[1]

def Creating_a_Report():
    list = []
    for k,v in dln.items():
        list += [[k,sum(v),len(v),sum(v)/len(v)]]
    listN = sorted(list,key=getKey)
    for x in listN:
        print ("{DN} {TD} {ND} {ADA}".format(DN = x[0], TD = x[1], ND = x[2], ADA = x[3]))
  

if __name__ == "__main__":

#Create a list with 5 donors and info
    dln = {'donor1':[10],'donor2':[20,30],'donor3':[40],'donor4':[50,60,70],'donor5':[80]}

    while True:
        choice = main_command()
        if choice in [1]:
           Sending_a_Thank_You()
        elif choice in [2]:
           Creating_a_Report()
        else:
           break


