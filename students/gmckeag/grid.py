def print_grid(n):

    horizontal_border = '+' + n * ' -' + ' +' + n * '- ' + '+'
    vertical_border   = '|' + n * '  ' + ' |' + n * '  ' + '|'

    for i in range(2*n+1):
        if i == 0 or i ==  n or i == 2*n:
            print(horizontal_border)
        else:
            print(vertical_border)

if __name__ == '__main__':
    n = int(input('Enter  an int: '))
    print_grid(n)
