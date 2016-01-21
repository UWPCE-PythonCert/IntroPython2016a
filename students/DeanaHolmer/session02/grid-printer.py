# Deana Holmer
# UWPCE Python 2016 Winter
# "grid-printer.py" due 1/21/2016
# In this exercise we draw blocks using functions, loops and string
# manipulation

import os
os.chdir('C:\\Documents\\Python\\python35src\\UWPython1\\week2')


def block_ceiling(num_blocks_across, block_width):
    print_line = '+'
    for i in range(0, num_blocks_across):
        print_line = print_line + ' -' * block_width + ' +'
    return print_line


def block_wall(num_blocks_across, block_width):
    print_line = '|'
    for i in range(0, num_blocks_across):
        print_line = print_line + '  ' * block_width + ' |'
    return print_line

# parameters 
block_width = 4
block_height = 4
num_blocks_across = 2
num_blocks_down = 2

for i in range(0, num_blocks_down):
    print(block_ceiling(num_blocks_across, block_width))
    for j in range(0, block_height):
        print(block_wall(num_blocks_across, block_width))
print(block_ceiling(num_blocks_across, block_width))
