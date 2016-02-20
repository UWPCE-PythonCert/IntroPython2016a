# Slicing Lab
# Student: Chi Kin Ho
# Date: Saturday, January 23, 2016


def exchange(s):
    """
    This functions takes any sequence and returns a sequence with the first and last
    items exchanged.

    :param s: any sequence
    :return: a sequence with the first and last items exchanged
    """
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        return s[len(s)-1:] + s[1:len(s)-1] + s[0:1]


def every_other_items_removed(s):
    """
    This function takes any sequence and returns a sequence with every other item
    removed.

    :param s: any sequence
    :return: a sequence with every other item removed
    """
    return s[::2]


def first_and_last_4_items_removed(s):
    """
    This function takes any sequence and returns a sequence with the first and last
    4 items removed, and every other item in between.

    :param s: any sequence
    :return: a sequence with the first and last 4 items removed, and every other
             item in between
    """
    s = s[4:]
    s = s[:-4]
    return s


def reverse(s):
    """
    This function takes any sequence and returns a sequence reversed.

    :param s: any sequence
    :return: a sequence reversed
    """

    return s[::-1]


def middle_third_last_third_first_third(s):
    """
    This function takes any sequence and returns a sequence with the middle third,
    then last third, then the first third in the new order.

    :param s: any sequence
    :return: a sequence with the middle third, then last third, then the first
            third in the new order
    """

    return s[int(len(s)/3):int(2*len(s)/3)] + s[int(2*len(s)/3):] + s[0:int(len(s)/3)]


if __name__ == '__main__':
    print(exchange(""))
    print(exchange("a"))
    print(exchange("ab"))
    print(exchange("abc"))
    print(exchange("abcd"))
    print(exchange("abcde"))
    print(exchange("abcdefghijk"))

    print(every_other_items_removed(""))
    print(every_other_items_removed("a"))
    print(every_other_items_removed("ab"))
    print(every_other_items_removed("abc"))
    print(every_other_items_removed("abcd"))
    print(every_other_items_removed("abcde"))
    print(every_other_items_removed("abcdefghijk"))

    print(first_and_last_4_items_removed(""))
    print(first_and_last_4_items_removed("a"))
    print(first_and_last_4_items_removed("ab"))
    print(first_and_last_4_items_removed("abc"))
    print(first_and_last_4_items_removed("abcd"))
    print(first_and_last_4_items_removed("abcde"))
    print(first_and_last_4_items_removed("abcdefghijk"))

    print(reverse(""))
    print(reverse("a"))
    print(reverse("ab"))
    print(reverse("abc"))
    print(reverse("abcd"))
    print(reverse("abcde"))
    print(reverse("abcdefghijk"))

    print(middle_third_last_third_first_third(""))
    print(middle_third_last_third_first_third("a"))
    print(middle_third_last_third_first_third("ab"))
    print(middle_third_last_third_first_third("abc"))
    print(middle_third_last_third_first_third("abcd"))
    print(middle_third_last_third_first_third("abcde"))
    print(middle_third_last_third_first_third("abcdefghijkl"))



