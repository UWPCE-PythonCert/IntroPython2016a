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

    encrypted = rot13("Wow This might Work")

    print(encrypted)


def rot13(phrase):

    encoded_phrase = ""

    # Iterate through each character in phrase
    for character in phrase:

        # Preform check on whether or not character is a letter and if its upper case
        letter = character.isalpha()
        case = character.isupper()

        # If its a letter, we begin doing 'encryption' on the character
        if letter is True:

            # If its an upper case letter the ascii's integer will be lower than the lower case numbers
            # What this does is allows us to always be adding ascii's integers to provide us a way to 'loop'
            # around the alphabetic circle so to speak
            if case is True:

                asc = ord(character)
                # We have to handle the situation of when adding 13 ascii integers will move into non-alpha characters
                # by skipping over them.  This helps us 'loop' around the alphabet
                if asc > 77:
                     asc = asc + 19

                     # When we jump over the non-alpha characters for ascii integers 91-96, we end up into lower case
                     # alpha characters.  We need to preserve the original case, so we bring it back to upper case.
                     encoded = (chr(asc)).upper()

                # If adding 13 ascii integers won't move us past alpha characters, simply add 13
                else:
                    asc = asc + 13
                    encoded = chr(asc)

                # We append our encrypted character to the encrypted string and return to the for loop
                encoded_phrase = encoded_phrase + encoded

            elif case is False:

                # We send the lower case letter to upper to preserve the simplicity of our looping around the alphabet.
                character = character.upper()
                asc = ord(character)

                # We have to handle the situation of when adding 13 ascii integers will move into non-alpha characters
                # by skipping over them.  This helps us 'loop' around the alphabet
                if asc > 77:
                    asc = asc + 19
                    encoded = chr(asc)
                else:
                    asc = asc + 13
                    encoded = chr(asc)

                # We need to preserve the lower case element of the character if we didn't have a need to 'loop' around
                # the alphabet
                encoded = encoded.lower()

                encoded_phrase = encoded_phrase + encoded

        # If it isn't a letter, simply add the character to the encrypted phrase to preserve spacing and/or punctuation.
        else:

            encoded_phrase = encoded_phrase + character

    return encoded_phrase
            


if __name__ == '__main__':
    main()