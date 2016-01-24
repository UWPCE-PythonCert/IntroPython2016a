#!/usr/bin/env python3

size = 11

print("Testing print_grid...")

for row in range(0,size):
    for col in range(0,size):
        if col == 0 or col % int(size/2) == 0 or col == size - 1:
            if row == 0 or row % int(size/2) == 0 or row == size - 1:
                print("+", end=' ')
            else:
                print("|", end=' ')
        else:
            if row == 0 or row % int(size/2) == 0 or row == size - 1:
                print("-", end=' ')
            else:
                print(" ", end=' ')
    print()

def print_grid(size):
    size += 2
    for row in range(0,size):
        for col in range(0,size):
            if col == 0 or col % int(size/2) == 0 or col == size - 1:
                if row == 0 or row % int(size/2) == 0 or row == size - 1:
                    print("+", end=' ')
                else:
                    print("|", end=' ')
            else:
                if row == 0 or row % int(size/2) == 0 or row == size - 1:
                    print("-", end=' ')
                else:
                    print(" ", end=' ')
        print()

def print_grid2(cols, rows):
    line_length = (cols + 1) + (rows * cols)
    for j in range(line_length):
        if j == 0 or j % (rows+1) == 0:
            for i in range(line_length):
                if i == 0 or i % (rows+1) == 0:
                    print("+", end=' ')
                else:
                    print("-", end=' ')
            print()
        else:
            for i in range(line_length):
                if i == 0 or i % (rows+1) == 0:
                    print("|", end=' ')
                else:
                    print(" ", end=' ')
            print()


print("Testing print_grid(3)...")
print_grid(3)
print()

print("Testing print_grid(15)...")
print_grid(15)
print()

print("Testing print_grid2(3,4)...")
print_grid2(3,4)
print()

print("Testing print_grid2(5,3)...")
print_grid2(5,3)
print()




