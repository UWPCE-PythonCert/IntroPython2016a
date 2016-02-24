'''
TO DO : this is the string formating lab assignment

A couple Exercises
Write a format string that will take:

( 2, 123.4567, 10000)

and produce:

'file_002 :   123.46, 1e+04'
Rewrite: "the first 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values
Trick: You can pass in a tuple of values to a function with a *:

for an arbitrary number of numbers...(from chapter 4 from class slides


'''

#for the lab

def defined_string(z):
    print("file_{:03d} \t {:.2f} \t {:.0e} ".format(*z))

z = ( 2, 123.4567, 10000)
defined_string(z) #format specfic to the lab exercise


#for fun
def string_for(a):
    for i in range(0,2):
        print("first is: {:d}  next is {:d} and third is: {:d}".format(*a))

a = (3,4,5,6,7,8)
y = string_for(a) #simple plain format

# a comma separater format
print("this is comma separted number format: {:,}".format(12346.34))

import datetime
d= datetime.datetime(2016, 2, 22,17,49,00)
print("this is the time: {:%Y-%m-%d %H:%M:%S}".format(d))

# for details:
#  https://docs.python.org/3/library/string.html#string-formatting