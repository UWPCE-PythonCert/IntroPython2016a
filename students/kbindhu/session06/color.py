def color(fore_color='red',back_color='white',link_color='blue',visited_color='yellow',**kwargs):
    print("Fore_color is: {}".format(fore_color))
    print("back_color is: {}".format(back_color))
    print("link_color is: {}".format(link_color))
    print("visited_color is: {}".format(visited_color))
    print("The keyword arguments are :",kwargs)

""" print the colors"""
color()
"""Call with a couple different parameters set"""
color('orange','grey')
"""pull out Have it pull the parameters out with *args, **kwargs """
color(other_color='navy')