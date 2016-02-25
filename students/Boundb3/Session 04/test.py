
#play with string print format
print(1234567890112345678901234567890)
a= "abcd\te\tfghij\tklmno\tpqrstu\tvvw\txyz"
b= "ab\tcdefgh\tij\tklmnopqrs\ttu\tvvwx\tyz"
print(a)
print(a.expandtabs())
print(a.expandtabs(tabsize=12))
print(a.expandtabs(tabsize=14))
print(b.expandtabs(tabsize=14))
print(a.rstrip("z"))


# this is extracted from intro Python 20116a added examples for session 5
def print_me( nums ):
    formatter = "the first %d numbers are: " + ", ".join( ["%i"] * len(nums) )
    print ("formatter: ", formatter)
    print (formatter%(( len(nums), ) + nums))

print_me( (2,3,4,5,6) )

#this did not work either - from format_test.py in session 04 examples
#or all on one line
#def print_msg(t):
 #   print ("the first %i numbers are: " + ", ".join(["%i"] * len(t)) ) % ((len(t),) + t)

#print_msg((56,67,34,23))

tpl1 = (3,4,5,6,7,8,9,1)
playformat = "i went to the store %d times per week and  %d every  day: " + " , ".join(["%i"]*len(tpl1))
print("playformat:", playformat)
print(playformat%((len(tpl1),(len(tpl1)/2),)+ tpl1))

list1 = ["hi", "iwent", "to", "the" ]
a= "this is a pen: "
b= "this is not a .."
print("a.join(b) looks like this: ", a.join(b))
print("this is a join: ", "*".join(list1))
print (" ".join(list1))