# 2-24-2016
#session06 keyword arguments lab

#1: write a function that 4 operational parameters with defaults

def pic_color(**kwargs):
    print("fore color is {fore_color} and back color is always {back_color}.  The link is {link}, but if you used it, it is {visited_color}.".format(**d))


d={"fore_color" : "gold", "back_color" : "silver", "link" : "orange", "visited_color": "purple"}
#check type
print(type(d))
#check key and values
for k,v in d.items():
    print (k, v)
#send to function
pic_color() #b3 -important** do not pass in an object (object d) when you call the def:  put the object **d in the format string!!


''' see new 1b below - you can define when you call the function'''


#2a - challenge - use positional (no defaults) and defaults

def pic_color_positional(*args,**kwargs):
    print("fore color is {} and back color is always {}. The link is {link}, but if you used it, it is {visited_color}  ".format(*t,**newd)) #defined here

t= ("black", "white")
newd = {"link" : "green", "visited_color": "skyblue"}

pic_color_positional() #not defined when called

#!!!!!!!!!!!!this more likely - defining the arguements when you call the function, not when it is in the function like 2a

#2b - challenge - use positional (no defaults) and defaults

def pic_color_positional(*args,**kwargs):
    print("fore color is {} and back color is always {}. The link is {link}, but if you used it, it is {visited_color}  ".format(*args,**kwargs)) #not defined the data here

t= ("black", "white")
newd = {"link" : "green", "visited_color": "skyblue"}

pic_color_positional(*t,**newd) #here defined what data to use when called the function


#1b: write a function that 4 operational parameters with defaults

def pic_color(**kwargs):
    print("fore color is {fore_color} and back color is always {back_color}.  The link is {link}, but if you used it, it is {visited_color}.".format(**kwargs))


d={"fore_color" : "gold", "back_color" : "silver", "link" : "orange", "visited_color": "purple"}

#send to function
pic_color(**d) #b3 -important** do not pass in an object (object d) when you call the def:  put the object **d in the format string!!