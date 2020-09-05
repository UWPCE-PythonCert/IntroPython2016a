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
    n = (x + 1)
    m = (n - 1)
    for m in range(0, m):
        def print_row():
            print('+', end=' '),
            print('-' * y, end=' '),
        def print_rows():
            n = (x + 1)
            m = (n - 1)
            for m in range (0, m):
                print_row()
        def print_column():
            print('|', end=' '),
            print(' ' * y, end=' '),
        def print_columns():
            n = (x + 1)
            m = (n - 1)
            for m in range (0, m):
                print_column()
        print_rows()
        print('+')
        def print_mult_columns():
            n = (y + 1)
            m = (n - 1)
            for m in range (0, m):
                print_columns()
                print('|')
        print_mult_columns()
    print_rows()
    print('+')
second_grid(4, 10)
