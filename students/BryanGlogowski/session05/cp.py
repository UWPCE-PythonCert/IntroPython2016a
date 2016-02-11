#!/usr/bin/env python3

def copy_file(src, dest):
    global f1, f2

    try:
        f1 = open(src, 'rb')
    except FileNotFoundError:
        print("could not read '{}'".format(src))
        return

    try:
        f2 = open(dest, 'wb')
    except IOError:
        print("could not open '{}'".format(dest))
        return

    for line in f1.readlines():
        try:
            f2.write(line)
        except IOError:
            print("could not write to '{}'".format(dest))
            return

    f1.close()
    f2.close()
    print("'{}' successfully copied to '{}'".format(src, dest))
    return

copy_file('students.txt', 'foo.txt')

