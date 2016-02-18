def print_grid(n):
    x = int(n/2)
    def print_row():
        print('+', end=' '),
        print('-' * x, end=' '),
        print('+', end=' '),
        print('-' * x, end=' '),
        print('+')
    def print_column():
        y = (x + 1)
        i = (y - 1)
        for i in range(0, i):
            print('|', end=' '),
            print(' ' * x, end=' '),
            print('|', end=' '),
            print(' ' * x, end=' '),
            print('|')
    print_row()
    print_column()
    print_row()
    print_column()
    print_row()


print_grid(10)


def second_grid(x, y):
    n = (y-1)
    for n in range(0, n):
        def print_rows():
            print('+', end=' '),
            print('-' * y, end=' '),
        print_rows()
        print('+')
        def print_columns():
            print('|', end=' '),
            print(' ' * y, end=' '),
        print_columns()
        print('|')
    print_rows()
    print('+')
second_grid(3, 4)
