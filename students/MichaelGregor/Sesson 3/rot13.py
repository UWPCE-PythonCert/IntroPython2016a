'''
Simple Framework that i created to flesh out a possible solution

def encode(phrase):

    phrase_to_encode = phrase
    encoded_phrase = ""

    for char in phrase_to_encode:

        newChar = ord(char)
        newChar = newChar + 13
        encoded_phrase = encoded_phrase + chr(newChar)


    print(encoded_phrase)

def decode(phrase):

    phrase_to_decode = phrase
    decoded_phrase = ""

    for char in phrase_to_decode:

        newChar = ord(char)
        newChar = newChar - 13
        decoded_phrase = decoded_phrase + chr(newChar)

    print(decoded_phrase)

def main():

    text_to_alter = input("Enter some text you wish to alter: ")

    print("Enter 1 to encode\nEnter 2 to decode")
    execution = input(":")

    while not (execution == "1" or execution == "2"):
        execution = input("Please enter 1 or 2 only:")

    if execution == "1":
        encode(text_to_alter)
    elif execution == "2":
        decode(text_to_alter)

'''

def main():

    encrypted = rot13("Zntargvp sebz bhgfvqr arne pbeare", decrypt=True)

    print(encrypted)


def rot13(phrase, decrypt):

    encoded_phrase = ""

    for character in phrase:                                # We loop through each character in the phrase

        letter = character.isalpha()                        # As we want to preserve casing and punctuation, we need
        case = character.isupper()                          # to check each character for both before encode/decode


        if letter is True:

            if case is True:

                if decrypt is True:                         # If decypting, we case all upper case letters to lower
                    character = character.lower()           # so we only have to subtract ascii's integers to complete
                    asc = ord(character)                    # the alphabet loop

                    if asc < 110:                           # We need to skip over ascii's integers 91-96 which aren't
                        asc = asc - 19                      # letters
                        encoded = chr(asc)

                    else:
                        asc = asc - 13
                        encoded = (chr(asc)).upper()        # We bring the char back to upper to preserve casing

                elif decrypt is False:
                    asc = ord(character)

                    if asc > 77:                            # When encrypting, we are 'looping' into lower case ascii
                        asc = asc + 19                      # integers, so we need to bring it back to upper case

                        encoded = (chr(asc)).upper()

                    else:
                        asc = asc + 13
                        encoded = chr(asc)

                encoded_phrase = encoded_phrase + encoded   # We append our 'new' character to our encoded/decode phrase

            elif case is False:

                if decrypt is True:
                    asc = ord(character)

                    if asc < 110:                           # When looping backward we run into uppercase letters so we
                        asc = asc - 19                      # bring the character to lower to preserve case.

                        encoded = (chr(asc)).lower()

                    else:
                        asc = asc - 13
                        encoded = chr(asc)

                elif decrypt is False:
                    character = character.upper()           # We send this to upper to start so we can just add ascii
                    asc = ord(character)                    # integers and send them to lower to preserve case after
                                                            # encode/decode
                    if asc > 77:
                        asc = asc + 19
                        encoded = chr(asc)
                    else:
                        asc = asc + 13
                        encoded = chr(asc)

                    encoded = encoded.lower()

                encoded_phrase = encoded_phrase + encoded

        else:
            encoded_phrase = encoded_phrase + character     # If character isn't an alpha char, we preserve it and move
                                                            # to the next character.
    return encoded_phrase

if __name__ == '__main__':
    main()
    
    
# nice job! 
