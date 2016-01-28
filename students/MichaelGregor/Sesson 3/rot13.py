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

    for character in phrase:

        letter = character.isalpha()
        case = character.isupper()


        if letter is True:

            if case is True:

                if decrypt is True:
                    character = character.lower()
                    asc = ord(character)

                    if asc < 110:
                        asc = asc - 19
                        encoded = chr(asc)

                    else:
                        asc = asc - 13
                        encoded = (chr(asc)).upper()

                elif decrypt is False:
                    asc = ord(character)

                    if asc > 77:
                        asc = asc + 19

                        encoded = (chr(asc)).upper()

                    else:
                        asc = asc + 13
                        encoded = chr(asc)

                encoded_phrase = encoded_phrase + encoded

            elif case is False:

                if decrypt is True:
                    asc = ord(character)

                    if asc < 110:
                        asc = asc - 19

                        encoded = (chr(asc)).lower()

                    else:
                        asc = asc - 13
                        encoded = chr(asc)

                elif decrypt is False:
                    character = character.upper()
                    asc = ord(character)

                    if asc > 77:
                        asc = asc + 19
                        encoded = chr(asc)
                    else:
                        asc = asc + 13
                        encoded = chr(asc)

                    encoded = encoded.lower()

                encoded_phrase = encoded_phrase + encoded

        else:
            encoded_phrase = encoded_phrase + character

    return encoded_phrase

if __name__ == '__main__':
    main()