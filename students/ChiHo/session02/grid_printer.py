# Week 2 - Lab #3: Print Grid
# Date: Sunday, January 17, 2016
# Student: Chi Kin Ho


def print_grid(n, m):

    """
       This function takes two natural number arguments, n and m.  It prints a
       grid with n by n squares where each square has the width of m characters.
    """

    # Initialize the grid before drawing.
    grid = ''
    for i in range(n):
        # Draw a horizontal row of border.
        grid += print_one_row_of_symbols(n, m, '+', '-')
        # Draw m rows of vertical bars.
        grid += print_one_row_of_symbols(n, m, '|', ' ') * m
    # Draw the last horizontal row of border.
    grid += print_one_row_of_symbols(n, m, '+', '-')
    # Output the grid on the screen.
    print(grid)


def print_one_row_of_symbols(n, m, outer_symbol, inner_symbol):

    """
       This function takes two natural number arguments, n and m, and two character arguments,
       outer_symbol and inner_symbol.  It prints one row of symbols with (n+1) outer_symbols
       and m inner_symbols between two outer_symbols.
    """

    # Draw the first outer symbol in a row.
    grid = outer_symbol
    for i in range(n):
        # Draw n inner symbols in the same row.
        grid += inner_symbol * m
        # Draw the outer symbol.
        grid += outer_symbol
    # Draw a new line.
    grid += '\n'
    return grid


# Test Case 1: 2 x 2 grid where each square has the width of 1.
print_grid(2, 1)
# Test Case 2: 2 x 2 grid where each square has the width of 7.
print_grid(2, 7)
# Test Case 3: 3 x 3 grid where each square has the width of 4.
print_grid(3, 4)
# Test Case 4: 5 x 5 grid where each square has the width of 3.
print_grid(5, 3)
