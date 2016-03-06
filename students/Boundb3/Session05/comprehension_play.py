#list:
y = [x*3 for x in [3,6,9,12]]
print(y)

#set

y = {x**2 for x in [3,-3,6,9,12]}
print(y)

# dictionary

y = {x: "this_%x is :  "%x*3 for x in [3,6,9,12]}
print(y)
