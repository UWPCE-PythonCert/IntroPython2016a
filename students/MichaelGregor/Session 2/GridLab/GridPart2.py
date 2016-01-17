import math

def main():
    print_grid(16)

def print_grid(size=3):
    ''' This function builds the grid based on the dimensions and size of the box provided

    :param size: The total size square of the grid. (default=3)
    :type size: int
    :return: None
    '''
    # Extremely hacky way of getting the correct sizing.  There must be a better way to do this.
    size = size / 2
    size = (int(size))

    # We only want 4 squares, regardless of size, so we hard code the number of iterations for the first for loop.
    for x in range(2):
        print_line(2,size, isLine=True)
        for x in range(size):
            print_line(2,size, isLine=False)
    print_line(2, size, isLine=True)


def print_line(num_plus, num_dash, isLine):
    '''
    This function prints a line in the grid.  A line with + and - characters is isLine is True.  A line with
    | and space characters if it is false.  We keep this in one function and paramaterize the function to aid
    in code reuse.

    :param num_plus: The number of + characters or columns we want in the grid
    :type num_plus: int
    :param num_dash: The number of - or spaces horizontally for each box
    :type num_dash: int
    :param isLine: If True, we will print a line that has + and - characters.  If False, we do | and space characters
    :type: bool
    :return: None
    '''
    # Checking to see if we are printing a line with +'s or a line with pipes
    if isLine:
        firstChar = "+"
        secondChar = "-"
    else:
        firstChar = "|"
        secondChar = " "

    plus_counter = 0
    space_counter = 0

    # We begin looping based on the dimensions provided

    # First while loop is for the + or | character printing
    while plus_counter < num_plus:
        print(firstChar, end="")

        # Second while loop is for the - or space characters
        while space_counter < num_dash:
            print(secondChar, end="")
            space_counter += 1

        # We have to re-initialize the space counter or the loop with exit immediately after we print the next
        # + or | character
        space_counter=0

        plus_counter +=1
    print(firstChar)

if __name__ == "__main__":
    main()