"""rot13.py"""
import string

def rot13 (str):
    """Translate str by mapping alphachars from intab to chars 13 ascii positions away in outtab"""
    intab =  "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outtab = "nopqrstuvwzyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

    return str.translate(str.maketrans(intab,outtab))

#Assigned string to translate
print(rot13("Zntargvp sebz bhgfvqr arne pbeare"))

#General Test
print(rot13("The Quick Brown Fox Jumped Over The Lazy Dog"))
