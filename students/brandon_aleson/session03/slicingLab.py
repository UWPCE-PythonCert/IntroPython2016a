# Brandon Aleson
# Intro to Python
# 1/27/16
# slice lab


# return a sequence with the first and last items exchanged.
def switch(n):
    first = n[0]
    last = n[-1]
    n[0] = last
    n[-1] = first
    return n
    # better solution:
    # newList = n[-1]+n[1:-1]+n[0]
    # return newList


# return a sequence with every other item removed
def skip(n):
    skipped = n[::2]
    return skipped


# return a sequence with the first and last 4 items removed, and every other item in between
def chop(n):
    chopped = n[4:(len(n)-4):2]
    return chopped


# return a sequence reversed
def reverse(n):
    n = n[::-1]
    return n


# return a sequence with the middle third, then last third, then the first third in the new order
def thirds(n):
    third = int(len(n)/3)
    thirds = n[third:(third*2)] + n[(third*2):(len(n))] + n[:third]
    return thirds
