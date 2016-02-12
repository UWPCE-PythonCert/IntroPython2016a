import string
upper = ""
if __name__ == '__main__':
    print("This program will encrypt your input using ROT13.")
    print("Please enter the text to be encrypted")
    encrypt = input()
    for k in encrypt:
        if k.isalpha() == False:
            print(k, end='')
        else:
            if k.isupper():
                upper = True
            else:
                upper = False
            outputL = chr(ord(k.lower())-13)
            outputU = chr(ord(k.lower())+13)
            if (ord(k.lower())) > 109:
                if upper == True:
                    print(outputL.upper(), end='')
                else:
                    print(outputL, end='')
            else:
                if upper == True:
                    print(outputU.upper(), end='')
                else:
                    print(outputU, end='')

    print("")
    print("Please enter the text to be encrypted")
    encrypt = input()
    for k in encrypt:
        if k.isalpha() == False:
            print(k, end='')
        else:
            if k.isupper():
                upper = True
            else:
                upper = False
            outputL = chr(ord(k.lower())+13)
            outputU = chr(ord(k.lower())-13)
            if (ord(k.lower())) < 110:
                if upper == True:
                    print(outputL.upper(), end='')
                else:
                    print(outputL, end='')
            else:
                if upper == True:
                    print(outputU.upper(), end='')
                else:
                    print(outputU, end='')
