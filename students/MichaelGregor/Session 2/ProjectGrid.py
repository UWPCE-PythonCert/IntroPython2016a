
def grid_ceiling(num_dashes, num_plus):
    counter_plus = 1
    counter_dash = 0
    while counter_plus < num_plus:
        print("+", end='')

        while counter_dash < num_dashes:
            print("-", end='')
            counter_dash += 1
        counter_dash=0

        counter_plus += 1
    print("+")

def grid_wall(num_spaces, num_walls):
    counter_walls = 1
    counter_spaces = 0
    while counter_walls < num_walls:
        print("|", end='')

        while counter_spaces < num_spaces:
            print(" ", end='')
            counter_spaces += 1
        counter_spaces=0

        counter_walls += 1
    print("|")

def main():
    grid_ceiling(4,3)
    for x in range(3):

        for y in range(4):
            grid_wall(4,3)
        grid_ceiling(4,3)

def print_grid(grid_boxes=3, grid_box_size=4):
    box_count=0
    wall_count=0
    while box_count < grid_boxes:
        grid_ceiling(grid_box_size, grid_boxes)
        box_count += 1
        while wall_count < grid_box_size:
            grid_wall(grid_boxes, grid_box_size)
            wall_count += 1

if __name__ == "__main__":
    main()