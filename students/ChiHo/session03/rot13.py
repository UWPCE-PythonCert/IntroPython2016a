# ROT13 Lab
# Student: Chi Kin Ho
# Date: Thursday, January 28, 2016

def rot13(s):
    """
    The ROT13 encryption scheme is a simple substitution cypher where each letter in a text is replace
    by the letter 13 away from it (imagine the alphabet as a circle, so it wraps around).

    :param s: the string text to be encrypted
    :return: the encrypted text using the ROT13 encryption scheme
    """

    encrypted_message = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                # This is a upper case letter.
                encrypted_message += chr( ((ord(letter) - ord('A') + 13) % 26) + ord('A') )
            else:
                # This is a lower case letter.
                encrypted_message += chr( ((ord(letter) - ord('a') + 13) % 26) + ord('a') )  # great!
        else:
            encrypted_message += letter
    else:
        # Display the encrypted message on the screen.
        print(encrypted_message)


if __name__ == '__main__':
    rot13('Zntargvp sebz bhgfvqr arne pbeare')



