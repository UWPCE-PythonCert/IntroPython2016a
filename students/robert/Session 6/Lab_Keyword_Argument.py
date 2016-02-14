HW
"""
Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it print the colors (use strings for the colors)
Call it with a couple different parameters set
Have it pull the parameters out with *args, **kwargs - and print those
"""

#function to print colors
def print_color(fore_color = 'Blue', back_color = 'Green', link_color = 'Grey', visited_color = 'Black'):
    print(fore_color,back_color,link_color,visited_color)

#Test
print_color('red','yellow',visited_color = 'purple',link_color = 'orange')

#function to pass it with args and print
def print_color(args):
    print ("{} {} {} {}".format(*args))

args = ['red','yellow','orange','purple']
print_color(args)

#function to pass it with kwargs and print
def print_color(kwargs):
    print ("{fore_color} {back_color} {link_color} {visited_color}".format(**kwargs)) 

kwargs = {'fore_color':'red','back_color':'yellow','link_color':'orange','visited_color':'purple'}
print_color(kwargs)