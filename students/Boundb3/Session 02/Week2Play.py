'''def is_it_true(xyz):
    if(xyz):
        print("yes there was something there")
    else:
        print("nothing was passed in")

is_it_true([4])

'''

def do_twice(f,printstuff):
    f(printstuff)
    f(printstuff)

def print_spam(b):
    print(b)

do_twice(print_spam,"printthiss")
