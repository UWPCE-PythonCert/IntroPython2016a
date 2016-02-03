#!/usr/bin/python
#Author:kbindhu
#Date:1/27/2016
#ROT13 encryption
"""Below program takes any amount of text and returns the text with each letter replaced
by letter 13 away from it."""
"""Algorithm is to convert each letter in the input text to ascii code with ord function.
Then for alphabets a-m and A-M add 13 to ascii values and for n-z and N-Z subtract 13 from ascii values.All other
characters are printed like space are printed as such"""
import codecs
def rot13( myString):
    out_str=''
    for i in myString:
        encp=ord(i)
        """checking that ascii corresponds to alaphbets a-m or A-M add 13 to it and find the corresponding letter""" 
        if(97<=encp<110) or (65<=encp<78):
            encp=encp+13
            #print(chr(encp),end='')
            out_str+=chr(encp)
            """if ascii corresponds to alphabets above m subtract 13 from the ascii and findcorresponding letter"""
        elif(110<=encp<=122) or(78<=encp<=90):
            encp =encp-13
            #print(chr(encp),end='')
            out_str+=chr(encp)
        else:
            #print(i,end='')
            out_str+=chr(encp)
    return out_str


#Test block
if __name__ == '__main__':
    print("Main module is being run directly ")
    Myoutstrng=rot13("Hello")
    #using the rot_13 algorithm to test my code
    assert (Myoutstrng) == codecs.encode('Hello', 'rot_13')
    Myoutstrng=rot13("Zntargvp sebz bhgfvqr arne pbeare")
    assert (Myoutstrng) == codecs.encode('Zntargvp sebz bhgfvqr arne pbeare', 'rot_13')
    Myoutstrng=rot13("Zntargvpjij**")

    assert(Myoutstrng)=='deewhuhfu',"Asssertion Error,Expected is :%s" %codecs.encode('Zntargvpjij**', 'rot_13')
else:
    print("rot_13.py is being imported into another module ")
    
# nicely done!
