'''
def encode(phrase):

    phrase_to_encode = phrase
    enconded_phrase = ""

    for char in phrase_to_encode:

        newChar = ord(char)
        newChar = newChar + 13
        enconded_phrase = enconded_phrase + chr(newChar)


    print(enconded_phrase)

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


def rot13(phrase):

    encoded_phrase = ""
    for character in phrase():
        if character.isalpha() and character.isupper():
            


if __name__ == '__main__':
    main()