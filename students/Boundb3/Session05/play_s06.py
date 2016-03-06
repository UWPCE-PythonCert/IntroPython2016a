# an example for a "switch dict"
#You can do a dispatch table by putting functions as the value. see below

arg_dict = {0:"zero", 1:"one", 2: "two"}
x = arg_dict.get(1, "nothing")
y = arg_dict.get(5, "nothing")
print("x is {} and y is {}".format(x,y))


def print_me():
    print("made it to printme")
    print("me")

def print_that():
    print("made it to printthat")
    print("that")
    return "howdy z"

def print_this():
    print("made it to printthis")
    print("this")

arg_dict2 = {0: print_me, 1:"One", 2: print_that}

#this does not work, as all called functions execute if no "" and i only get a print string otherwise
z = arg_dict2.get(2, "nothing")()  #!!!!! oh - need the extra object call parathesis in the get call -- *** here***
print("z is" , z)


arg_dict2.get(2, "nothing")()

'''
What would this be like if you used functions instead? Think of the possibilities.

In [11]: def my_zero_func():
return "I'm zero"

In [12]: def my_one_func():
    return "I'm one"

In [13]: switch_func_dict = {
    0: my_zero_func,
    1: my_one_func,
}

In [14]: switch_func_dict.get(0)()#b <---look at this set of paranthesis!!!!!
Out[14]: "I'm zero"

'''