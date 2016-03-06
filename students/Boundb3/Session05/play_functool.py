
import functools

def greet(greeting,target):
    return print("{}! {}".format(greeting,target))



greet = functools.partial(greet,"Hola")
greet("bob")
greet("steve")


