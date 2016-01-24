def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row():
    print ('+ - - - - + - - - - + - - - - + - - - - +'),

def print_column():
    print ('|         |         |         |         |')

def print_columns():
    do_four(print_column)

def print_rows():
    print_row()
    print_columns()

def print_grid():
    do_four(print_rows)
    print_row()

print_grid()