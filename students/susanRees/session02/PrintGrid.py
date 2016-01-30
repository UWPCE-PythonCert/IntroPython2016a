def print_grid(n):
    x = int(n/2)
    def print_row():
        print('+', end=' '),
        print('-' * x, end=' '),
        print('+')
        def print_column():
            y = (x + 1)
            i = (y - 1)
            for i in range(0, i):
                print('|', end=' '),
                print(' ' * x, end=' '),
                print('|')
            else:
                print_row()
    print_row()

print_grid(8)

# print header/middle/footer row, divider row - use lists?
