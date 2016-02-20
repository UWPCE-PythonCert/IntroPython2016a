#This is from session 4 of python 100a
#instructinos for a dict and set lab

'''
Learning about dictionaries and sets
Goal:
Learn the basic ins and outs of Python dictionaries and sets.

Procedure
In your student dir in the IntroPython2015 repo, create a session04 dir and put in a new dict_lab.py file.

The file should be an executable python script. That is to say that one should be able to run the script directly like so:

Add the file to your clone of the repository and commit changes frequently while working on the following tasks. When you are done, push your changes to GitHub and issue a pull request.
'''

#create a dictionary
# be lazy and start with a list
d={}
print(type(d))

# be lazy and start with a list
l=["city:Seattle", "name:Chris", "cake:chocolate"]
for x in l:
    print (x)
    k,v = x.split(":")
    d[k]=v
#confirm in dictionary format
print(d)

#delete cake
del d['cake']
print(d)

#add entry for fruit with mango
d['fruit'] = "mango"
print(d)

#display the keys
print(d.keys())

#display the values
print(d.values())

#confirm booleon for cake in dictionary
res = "cake" in d # this could be like this: just: "in d", or like thins :'in d.keys()
print (res)

#confirm booleon for mango in dictionary
res2 = "mango" in d.values()
print(res2)

#using dictionary from before,
d2 = {}
l=["city:Seattle", "name:Chris", "cake:chocolate"]
for x in l:
    print (x)
    k,v = x.split(":")
    d2[k]=v
print("d2 = ", d2) # to confirm

#make a new dictionary using same keys but with the number of t's in each as its value'
for k,value in d2.items():
    count = 0
    for letter in value:
        if letter.lower() == "t":
            count +=1
    d2[k] = (count)
print (d2)

#SETS

#create sets
s2 = set()
#confirm type
print(type(s2))
#create more sets:
s3 = set()
s4 = set()

# sets divisible by some #

def set_division(top,modulus,set):
    for num in range(top):
        s = num+1
        if s % modulus == 0:
            set.add(s)
    return set

#create set modulus 2 fro range 1-20
s2 = set_division(20,2,s2)
print ("s2 is" , s2)
print(type(s2))

#create set modulus 3 fro range 1-20
s3 = set_division(20,3,s3)
print ("s3 is" , s3)

#create set modulus 4 fro range 1-20
s4 = set_division(20,4,s4)
print ("s4 is" , s4)

#is set s3 subset of set2
res3 = s3.issubset(s2)
print (res3)

#is set s4 subset of set2
res4 = s4.issubset(s2)
print (res4)

#create a set with python
s_p = set("Python")
print(s_p)

#add an i to it
s_p.add("i")
print(s_p)

#frozen set marathon
s_m = set("marathon")
fs_m = frozenset(s_m)
print(fs_m)

#union of python (with i) and marathon sets
print("union of python and marathon" ,s_p.union(fs_m))


#intersection of pyton(with i) and marathon
print("intersection of python and marathon" ,s_p.intersection(fs_m))