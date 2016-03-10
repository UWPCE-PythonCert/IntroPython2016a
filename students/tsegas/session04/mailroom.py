# mailroom script: Writes emails thanking donors for donation amounts and generates report of donations
#
import random
import string
import sys
from collections import Counter

# Initial Dictionary of doners nd amounts
d = {'Chris C': 200, 'John J': 300, 'Matt M': 400, 'Luke L': 100, 'Eli E': 500}
a = {'amount1': 1,'amount2': 2,'amount3': 3,'amount4': 4,'amount5': 5}

#print("The doners are:",d)
#print("print the amounts",a)

# function to get doner and the amount
def donfunc(option,name,amount):
    #if thanks you:
    if option == 'yes':
        #print("print doner",name)
        if name == "list":
            print("printing the list of doners.... ",d)
            don_again = input('Enter full name of doner:')
            dname = don_again
        else:
            dname = name

        if amount.isdigit() == True:
            #print("print new amount",amount)
            amount = int(amount)
        else:
           # print("enter a number please:")
            amount = input('enter a number please:')
            amount = int(amount)
        #a['amount6'] = amount
        if dname in (d):
            d[dname] = d[dname] + amount
        else:
            d[dname] = amount
        #print("print the list of doners",d)
        #print("print the list of amounts",a)

        #print("Dear %s,\n",%dname)
        print('Dear {0},'.format(dname))
        print("Thank you for your ${0}.00 donation".format(amount),'\n')
        #don = input('Enter full name of doner or list:')

def repeats(name,comp):
    if (name == comp):
        match = 1
        return match

def repfunc(count,dn):
    #if opt2 == 'yes':
    #for i, item in enumerate(d):
    #print(a)
    l = len(d)
    #print(l)
    #ak = list(a)[i]
    #print(ak)
    tot = sum(d.values())
    #print('total..........',tot)
    avg = tot/l
    numd = count
    n = ('{:s}         ${:d}.00       {}      ${:06.2f}.00'.format(dn,d[dn],numd,avg))
    print(n)

m = repeats(name="temp",comp="temp")

#function to print out the report
def report ():
    h = ('Doner         Total        Donation Count       Average Donation')
    print(h)
    for i, item in enumerate(d):
        f = list(d)[i]
        cnt = 0
        for i in d.keys():
            #print('iiiiiii',i)
            #print(cnt)
            m = repeats(name=f,comp=i)
            #print(m)
            if m == 1:
                cnt = cnt + 1
        #print('count........',cnt)
        #print("the %ith item is: %s with count %i"%(i, d.get(item),cnt))
        ndict = ('{:s}(count:{:d})'.format(f,cnt))
        repfunc(count=ndict,dn=f)


opt1 = input('Send a Thank You?:')
opt2= input('Create a Report?:')


if opt1 == 'yes':
    don = input('Enter full name of doner or list:')
    amou = input('enter the donation amount:')
    #call the function
    donfunc(option=opt1,name=don,amount=amou)
if  opt2 == 'yes':
    #call the function
    report()
