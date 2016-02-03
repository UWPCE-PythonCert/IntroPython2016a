"""
Add a python module named rot13.py to the session03 dir in your student dir.
This module should provide at least one function called rot13 that takes any
amount of text and returns that same text encrypted by ROT13.

This function should preserve whitespace, punctuation and capitalization.

Your module should include an if __name__ == '__main__': block with tests (asserts)
    that demonstrate that your rot13 function and any helper functions you add work properly.

As usual, add your new file to your local clone right away.
Make commits early and often and include commit messages that are descriptive and concise.  When you are done,
if you want me to review it, push your changes to github and issue a pull request.

try decrypting this:Zntargvp sebz bhgfvqr arne pbeare
"""



def rot13(codestr, ENcode=False):
    '''Code or decode a string based on a 13 letter shift to the right.  An optional second arguement: when True
    it will ENcode, when it is False it will DEcode the first alpha arguement. '''

    intab =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # write these outside the loop so they don't have to get
    outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM" # recreated every time :)
    assert len(intab) == len(outtab), "lengths are not the same." # why are you checking the lengths here? 
    if ENcode == False:
        answer = (codestr.translate(str.maketrans(outtab, intab)))
    else:
        answer = (codestr.translate(str.maketrans(intab, outtab)))
    return answer




if __name__ == "__main__":
    choice = 5
    while not choice == 2 and not choice == 1:
        try:
            choice = int(input("Do you want to 1)make code or 2)desypher code?  Type 1 for encode and 2 for desypher "))
            print ("OK, got it.  Number {} was your choice.".format(choice))
        except ValueError:
            print("You need to input a number.  Try again")
        assert choice == 1 or choice == 2 , "You did not type in a 1 or a 2- try again or you must be a spy."


    dedecoderring= input("Type in the string you would like to send through the decoder ring.")

    if choice == 1:
        print(rot13(dedecoderring, True))
    elif choice ==2:
        print(rot13(dedecoderring, False))
    else:
        print("I did not understand.  Try again.  I'm beginning to wonder if you are spy??")
