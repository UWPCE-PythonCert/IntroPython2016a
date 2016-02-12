
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
#First
length = len(s) - 1
s[0], s[length] = s[length], s[0]
print(s)
'''
'''
#second

sliceable = s[::2]
print(sliceable)
'''
'''
#third
length = len(s)
length -= 1
s.pop(length)
s.pop(0)

slicable = s[::2]

print(slicable)
'''
'''
#fourth
s = s[::-1]
print(s)
'''

