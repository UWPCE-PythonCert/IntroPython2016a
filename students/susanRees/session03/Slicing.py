s = "thequickbrownfox"

#return a sequence with the first and last items exchanged.
s[-1]+s[1:-1]+s[0]

#return a sequence with every other item removed
s[::2]

#return a sequence with the first and last 4 items removed, and every other item in between
s[1:-5:2]

#return a sequence reversed (just with slicing)
s[-1], s[-2], s[-3], s[-4], s[-5], s[-6], s[-7], s[-8], s[-9], s[-10], s[-11], s[-12], s[-13], s[-14], s[-15], s[-16]

#return a sequence with the middle third, then last third, then the first third in the new order
s[5:11], s[11:16], s[0:5]