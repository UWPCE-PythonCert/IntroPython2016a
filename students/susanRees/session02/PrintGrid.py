def print_grid(n):
    x = int(n/2)
    def print_row():
        print('+', end=' '),
        print('-' * x, end=' '),
        print('+'),
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
    print_column()
    print_column()

print_grid(8)

#HOW  DO I MAKE THE ROW AND COLUMNS PRINT ON THE SAME LINE???????? (END=' ' ISN'T WORKING)