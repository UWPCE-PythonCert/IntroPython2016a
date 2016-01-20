def grid(n):
    """ Returns grid string """
    horizontal_border = '+' + n * ' -' + ' + ' + n * '- ' + '+\n'
    vertical_border   = '|' + n * '  ' + ' | ' + n * '  ' + '|\n'

    grid = str()
    for i in range(2*n+1):
        if i == 0 or i ==  n or i == 2*n:
            grid += horizontal_border
        else:
            grid += vertical_border
    return grid

if __name__ == '__main__':
    n = int(input('Enter  an int: '))
    print(grid(n))
