#!/usr/bin/env python3

def rot13(s):
    """
    Encode/Decode ROT-13 string
    :param s - string to be encoded ROT-13:
    :return string
    """

    from_table = 'abcdefghijklmnopqrstuvwxyz'
    from_table += from_table.upper()
    to_table = 'nopqrstuvwxyzabcdefghijklm'
    to_table += to_table.upper()
    trantab = str.maketrans(from_table, to_table)

    encoded_char_list = []
    for c in s[:]:
        encoded_char = c.translate(trantab)
        encoded_char_list.append(encoded_char)

    return ''.join(encoded_char_list)


if __name__ == '__main__':
    s1 = 'abcdEFG This ia a Little Thing with 3423t23t0~~2#@ junk IN the Middle  123\n'
    s2 = rot13('abcdEFG This ia a Little Thing with 3423t23t0~~2#@ junk IN the Middle  123\n')
    s3 = rot13(s2)
    assert s1 == s3

    print(rot13('Zntargvp sebz bhgfvqr arne pbeare'))


