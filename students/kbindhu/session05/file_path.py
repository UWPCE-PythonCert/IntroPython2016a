#!/usr/bin/python
#kbindhu
#Date created:2/10/2015

import os 
print("-"*80)
print("Print all abs path of all files in a given directory")
print("-"*80)
for root, dirs, files in os.walk('.'):
    for file in files:
        p=os.path.join(root,file)
        print (os.path.abspath(p))

"""a program which copies a file from a source, to a destination line by line using file"""
f=open('src.txt','r')
f1=open('dest.txt','w')
for line in f.readline():
    f1.write(line)
f1.close()
f.close()

