import pathlib
pth = pathlib.Path("./")
print(pth.absolute())

#C:\Python_100a\IntroPython2016a\examples\"students.txt"

with open('C:\Python_100a\IntroPython2016a\examples\students.txt',mode = "r") as f:
    file_content= f.read()
    print(file_content)
print(f.closed)

lang_dict ={}
name_list = []
count = 0

with open ('C:\Python_100a\IntroPython2016a\examples\students.txt',mode = "r") as f:
    for row in f.readlines():
        row = row.strip()
        name,lang = row.split(":")
        name_list.append(name) # not really needed, but seperate list of names - and we know there is only 1 name per row
        languages_list = lang.split(",") #used to split the side of the row which are languages (1 of many), and add them to a variable - which happens to store them as a list
        for item in languages_list: #cycle through the rows' language, and count the language per person per row and add to a dictionary
            if item not in lang_dict:
                lang_dict[item] = 1
            else:
                lang_dict[item] = lang_dict[item] + 1


        count += 1
        print ("{:02d}: name is {} and lang is {}".format(count,name,lang))
print("there are {} languages in all: {}".format (len(lang_dict),lang_dict))
print("there are {} people in the class".format(len(name_list)))
print("most popular languages (in order are: ", sorted(lang_dict,key=lang_dict.get, reverse = True))
for k, v in lang_dict.items():
    print("lang ={:<15}, count = {:>3}".format(k,v))

#try counter objects
import os,argparse
#cnt = Counter() # not working - counter() method not recognized - what lib do i need to import.  8.3.2: see https://docs.python.org/3.5/library/collections.html#collections.namedtuple


