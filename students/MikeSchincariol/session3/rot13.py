#!/usr/bin/python3

def rot13(text):

    # Create the translations tables to feed to str.translate()
    lc_first_half  = "abcdefghijklm"
    lc_second_half = "nopqrstuvwxyz"
    lc_translate = str.maketrans(lc_first_half + lc_second_half,
                                 lc_second_half + lc_first_half)

    uc_first_half = lc_first_half.upper()
    uc_second_half = lc_second_half.upper()
    uc_translate = str.maketrans(uc_first_half + uc_second_half,
                                 uc_second_half + uc_first_half)

    # Loop over each character
    retval = ""
    for char in text:
        if char.isspace():
            # Pass spaces through unmodified
            retval += char
        elif char.islower():
            # Convert lower case letter
            retval += str(char).translate(lc_translate)
        elif char.isupper():
            # Convert upper case letter
            retval += str(char).translate(uc_translate)
        else:
            # Pass numbers and punctuation through unmodified
            retval += char

    # Done. Return the result back to the caller.
    return retval


# If not called as a function, run some tests
if __name__ == "__main__":
    test_val = '"Hello World"'
    result = rot13(test_val)
    assert(result == '"Uryyb Jbeyq"')
    print("Test {0} OK: {1} -> {2}".format(1, test_val, result))

    test_val = '"Zntargvp sebz bhgfvqr arne pbeare"'
    result = rot13(test_val)
    assert(result == '"Magnetic from outside near corner"')
    print("Test {0} OK: {1} -> {2}".format(2, test_val, result))