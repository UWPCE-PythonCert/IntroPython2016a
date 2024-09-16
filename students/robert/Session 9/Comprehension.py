#!/usr/bin/env python

# Comprehension Lab

#Count Even Numbers
def count_evens(array):

    updated_array = [x for x in array if x%2 == 0 or x == 0 ]
    return len(updated_array)


# comprehension test for dict and set
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

def comprehension(dict):
    print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**dict))


num = [x for x in range(16)]
nhex = [hex(x) for x in range(16)]

for x in num:
    for y in nhex:
        numhex[x] = y


numhex = {x:hex(x) for x in range(16)}


#fp_copy = food_prefs
fp_copy = {}

def countA(v):
    count = 0
    for x in v:
        if x == 'a' or x == 'A':
            count+=1
    return count

for k,v in food_prefs.items():
    fp_copy[k] = countA(v)


Nlist = [i for i in range(21)]

Dlist = [2,3,4]

s2 = set(x for x in Nlist if x%2 == 0)

s3 = set(x for x in Nlist if x%3 == 0)

s4 = set(x for x in Nlist if x%4 == 0)

#slist = [s2,s3,s4]

slist = [set(x for x in Nlist if x%t == 0) for t in Dlist ]
