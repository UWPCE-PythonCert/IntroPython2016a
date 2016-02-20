""" this is the list lab

***key questions on shallow copy - row 100 fixed in routine below it - buthow should we DEEP copy a list
*** the boolean AND on row:  80  AND



"""

#create and print a list
fruitStr = "apples,pears,oranges,peaches"
fruitLst = fruitStr.split(",")
print(fruitLst)

# ask and add a new fruit to the back of the list
newfruit = input("what new fruit would you like to add?")
fruitLst.append(newfruit)

# get a number from the user and show the number and fruit from the list
#starting with 1

request = int(input("pick a number between 1 and {}".format(len(fruitLst))))
print ("your list: ", fruitLst)
print("{} was the number for {}.  I will delete it.".format(request,fruitLst[request-1]))
del fruitLst[request-1]
print ("your updated list" , fruitLst)

#add another fruit to the beginning of the list using +
anotherfruit = [input("what other fruit would you like to add to the front of the list?")] # now it is a list item input
fruitLst = anotherfruit + fruitLst
print ("your list with {} looks like this:\n\t{}".format(anotherfruit[0],fruitLst))

#add another fruit to the beginning of the list using insert
anotherfruit2 = input("what second fruit would you like to add to the front of the list?") #now it is a string input
fruitLst.insert(0,anotherfruit2)
print ("here is the list with your second fruit {} added too:\n\t{}".format(anotherfruit2,fruitLst))

#display fruits beginning with letter P
print("\n\n Lets find the fruit that start with the letter 'P'")
pList = []
for i in fruitLst:
    if "P" == i[0].upper():
        pList.append(i)
print("\n\nHere is the full list of P fruits:", pList)


#starting again a new set of tasks
copyfruitLst = fruitLst[:] # preserve a copy of the list

print("\n\nOK - here is the current list of all the fruits, not just P",fruitLst)
x= fruitLst.pop(-1)
print("now here is your list without the last item: {} ".format(x), end ="")
print("\t{}".format(fruitLst))
for indx,item in enumerate(fruitLst):
    print("\t{} )  {}".format((indx+1),item.strip()))#*********
dislike = int(input("select an item number to be deleted:"))
dislikefruit = fruitLst[dislike-1]
fruitLst.pop((dislike-1))

print("So, you don't like {}.  Here is the remaining list:{}".format(dislikefruit, fruitLst))

#start for bonus - multiply list and delete all instances of disliked fruit
oldfruitLst = copyfruitLst[:]
print("\nOK - lets go back to the old list you had:",oldfruitLst)
oldfruitLst = oldfruitLst + oldfruitLst *2
for x in oldfruitLst:
    if x == dislikefruit:
        oldfruitLst.remove(x)
print("whoops we multiplied your list{}, but we lost all the {}!  where did it go?".format(oldfruitLst,dislikefruit))


#new questions - loop through list to ask yes or no if they like.  delete all occurances

fruitset = set(copyfruitLst) # drop any duplicates by turning list into a set
fruitLst = list(fruitset) #return it back into a list
fruitLstlwr = [] #prep for a new list to be built in all lower case
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

# one more exercise to reverse the list

## HOW do I not effect the original and the adapted one -- how to avoid a shallow copy!!!!!!!!!!!
rvrscopy_fruitLst = fruitLst[:]
print("fruitlist:" , fruitLst)
print("rvrscopy_fruitLst is", rvrscopy_fruitLst)
for item in fruitLst: #iterate on one list
    print ("item",item)
    if len(item)>1:
        first = item[0]
        last = item[-1]
        newitem = last + item[1:-1] + first
    else: newitem = item
    print("newitem is",newitem)
    rvrscopy_fruitLst.append(newitem)#update and make changes to the other list
    rvrscopy_fruitLst.remove(item)
print("original list is: ", fruitLst) #yea it works now - iterate on one list, and make changes to the other copy of the list
print("new rvrsed list is: ",rvrscopy_fruitLst) #yea it works now !!!
print("now we can get rid of the last entry in our fruit salad:  lets nix {}".format(fruitLst.pop()),fruitLst)


# start with a list and a list copy
# this time change all the letters to go backward, not just switch first and last letter

print("\n\n\n duplicate of last excercise is below - for grins - now that it works")
fruitLst = list(fruitset)
rvrscopy_fruitLst = fruitLst[:]  #this is creating the shallow copy - so how do we NOT do this???
print("fruitlist:" , fruitLst)
print("rvrscopy_fruitLst is", rvrscopy_fruitLst)
brandnew_list = []
for item in rvrscopy_fruitLst:
    print ("item is: ",item)
    if len(item)>1: #if each word in the list is longer than one letter, then swap first and last letter
        newitem = item[::-1]
    else: newitem = item
    print("newitem is: ",newitem)
    brandnew_list.append(newitem)

print("original list is: ", fruitLst)
print("new rvrsed brand new list is: ",brandnew_list)
print("now we can get rid of the last entry in our fruit salad:  lets nix {}".format(fruitLst.pop()),fruitLst)
