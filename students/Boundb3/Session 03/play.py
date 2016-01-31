def do_twice(func, arg):
    """Runs a function twice.

    func: function object
    arg: argument passed to the function
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """Prints the argument twice.

    arg: anything printable
    """
    print(arg)
    print(arg)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')

