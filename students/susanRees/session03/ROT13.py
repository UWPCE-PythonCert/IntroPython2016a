# each letter in a text is replace by
# theletter 13 away from it

# write function called rot13
# takes text and returns it encrypted by ROT13.
# preserve whitespace, punctuation and caps.

# include an if __name__ == '__main__': block
# with tests (asserts) to show it works

# try decrypting this:
# “Zntargvp sebz bhgfvqr arne pbeare"

import codecs

def rot13():
    print("Please input text to be encoded")
    secrets = input()
    str(secrets)
    print(codecs.encode(secrets, "rot-13"))

rot13()