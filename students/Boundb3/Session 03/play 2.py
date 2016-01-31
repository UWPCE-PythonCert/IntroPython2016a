'''

play 2 - to find how to get first letter print()

'''

'''

#display fruits beginning with letter P
print("lets find the fruit that start with the letter 'P'")
fruitLst = ["Pinanpple", "rose", "tea", "peach", "orange", " apple"]
for i in fruitLst:
    print ("i is", i)
    print ("i is first place=" ,i[0])
    print(i[0], i[0].upper())

    if "P" == i[0].upper:
        print(i)
'''
'''
fruitLst = ["Pinanpple", "rose", "tea", "peach", "orange", " apple"]
fruitLst = fruitLst + fruitLst
print(fruitLst)
fruitLst = fruitLst *2
print(fruitLst)
'''
'''

copyfruitLst = ["Pinanpple", "rose", "teA", "Peach", "ORANGE", " apple"]
copyfruitLst = copyfruitLst *3
print(copyfruitLst)
#new questions
fruitset = set(copyfruitLst)
print ("now it is a set?",type(fruitset))
print(fruitset)
fruitLst = list(fruitset)
print("now it is a list?",type(fruitLst))
print(fruitLst)
fruitLstlwr = []
for item in fruitset:
    item= item.lower()
    fruitLstlwr.append(item)
    reply = None
    while reply != "yes" and reply != "no":
        reply = input("do you like {}?  Input yes or no. ".format(item)).lower()
        if reply == "yes":
            print("great, we will keep {}".format(item))
        elif reply == "no":
            fruitLstlwr.remove(item)
            print("OK - say goodby to {}".format(item))
        else:
            print("you must enter yes or no")
print("this is your new list of favorites",fruitLstlwr)
'''

rvrscopy_fruitLst = ["Pinanpple", "rose", "teA", "Peach", "ORANGE", " apple","hi", "i"]
for item in rvrscopy_fruitLst:
    if len(item)>1:
        print (item)
        first = item[0]
        last = item[-1]
        item = last + item[1:-1] + first
    print(item)








