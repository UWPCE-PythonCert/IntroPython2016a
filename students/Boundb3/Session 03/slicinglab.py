# this is a re-do of the slicing lab to make sure I did it

'''

return a sequence with the first and last items exchanged.
return a sequence with every other item removed
return a sequence with the first and last 4 items removed, and every other item in between
return a sequence reversed (just with slicing)
return a sequence with the middle third, then last third, then the first third in the new order
'''

x = ("1234567890 I went to the store only Monday abcdefghijklmnopqrstuvwxyz12")
print(x)

x_switchfirstnlast = x[-1:]+x[1:-2]+x[0:1]
print(x_switchfirstnlast)

x_every_other_removed = x[::2]
print(x_every_other_removed)

x_mid_with_missing_mid = x[4:-4:2]
print(x_mid_with_missing_mid)

x_reversed = x[::-1]
print(x_reversed)

thirds = (len(x)//3)
leftover = (len(x)%3)
print(thirds,"\n",leftover)
x_mid_last_first_thirds = x[(thirds):(-thirds)]+ " *|* " +  x[(-thirds):] + " *|* " + x[:(thirds)]
print(x_mid_last_first_thirds)
