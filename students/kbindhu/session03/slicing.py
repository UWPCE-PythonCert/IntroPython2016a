#!/usr/bin/python
#Author Krishna Bindhu
#Date 1/26/2015

#creating a list
l=[ ]
for i in range(1,20):
    l.append(i)
print("Input List")
print (l)


#Swap function for exchanging last and first value
def Swap(a):
    a[0],a[-1]=a[-1],a[0]
    return a
 #Function call
print("Swapped List")
print(Swap(l))

#Had to create list again as older lsit get rewritten every time with return value
l=[ ]
for i in range(1,20):
    l.append(i)
print("Input List")
print (l)

# below function removes every other item from list
def ItemRemoved(a):
    return a[0:-1:2]
print("sequence with every other item removed")
print (ItemRemoved(l))


l=[ ]
for i in range(1,20):
    l.append(i)
print("Input List")
print (l)

#Below function removes last 4 items from list and every other item
def LastFourRemoved(l):
    a=l[0:-4:2]
    return(a)
print("sequence with the first and last 4 items removedand every other item in between")
print(LastFourRemoved(l))

l=[ ]
for i in range(1,20):
    l.append(i)
print("Input List")
print (l)


#function to reverse a string
def  Reverse(l):
    a=l[::-1]
    return(a)
print("Sequence Reversed")
print(Reverse(l))

l=[ ]
for i in range(1,20):
    l.append(i)
print("Input List")
print (l)


#Function to return a sequence with the middle third, then last third, then the first third in the new order
def EveryThird(l):
    a=list() #Newlist
    s=int(len(l)/3) #s has index for last element of first third
    s1=int(len(l)*2/3) #s1 has index for last elemnet of second third
    FirstThird=l[:s]   #slice to print from index zero to s
    MidThird=l[s:s1]  #slice to print from index s to seconf third
    LastThird=l[s1:]
    a.extend(MidThird)
    a.extend(LastThird)
    a.extend(FirstThird)
    return(a)
print("sequence with the middle third, then last third then the first third in the new order")
print (EveryThird(l))
