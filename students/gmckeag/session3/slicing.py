def first_and_last(s):
    return [s[0], s[-1]]

def every_other_removed(s):
    return s[::2]

def loose_first_last4_and_every_other_between(s):
    return s[1:-4:2]

def reverse(s):
    return s[::-1]

def thirds(s):
    third = len(s) // 3
    return s[third:] + s[:third]


if __name__ == '__main__':
    s = [1,2,3,4,5,6,7,8,9,10,11,12]
    print('List = ', s)
    print('First and last = ', first_and_last(s))
    print('Every other removed =', every_other_removed(s))
    print('First removed, last 4 removed and every other between removed = ', loose_first_last4_and_every_other_between(s))
    print('Reversed = ', reverse(s))
    print('Middle Last, First = ', thirds(s))


