# mailroom

#my = dict(name='Chris', 'John', amount='1','2','3')
#my = dict(name='Chris', 'John', amount='1','2','3')
d = {'doner1': 'Chris C', 'doner2': 'John J','doner3': 'Matt M','doner4': 'Luke L','doner5': 'Eli E'}
a = {'amount1': 1,'amount2': 2,'amount3': 3,'amount4': 4,'amount5': 5}

print("print the doners",d)
print("print the amounts",a)
# prompt for option


#FIZZBUZZ function
def donfunc(option,name,amount):
    #if thanks you:
    if option == 'yes':
        #print("print doner",name)
        if name == "list":
            print("print the list of doners",d)
            don_again = input('Enter full name of doner:')
            dname = don_again
            if don_again in (d):
                print("print the list of doners",d)
            else:
                d['doner6'] = dname
            #print("print the doners",d)
        else:
            dname = name
            d['doner6'] = dname
           # amount = input('Enter the donation amount:')

        if amount.isdigit() == True:
            print("print new amount",amount)
        else:
           # print("enter a number please:")
            amount = input('enter a number please:')
        a['amount6'] = amount
        print("print the list of doners",d)
        print("print the list of amounts",a)

        #print("Dear %s,\n",%dname)
        print('Dear {0},'.format(dname))
        print("Thank you for your {0}th donation".format(amount))
        #don = input('Enter full name of doner or list:')

def repfunc():
    #if opt2 == 'yes':
    for i, item in enumerate(d):
        #print("the %ith item is: %s"%(i, item))  
        print("the %ith doner is: %s"%(i,d.get(item)))

opt1 = input('Send a Thank You?:')
opt2= input('Create a Report?:')


if opt1 == 'yes':
    don = input('Enter full name of doner or list:')
    amou = input('enter the donation number:')
    #call the function
    donfunc(option=opt1,name=don,amount=amou)
if  opt2 == 'yes':
    #call the function
    repfunc()
