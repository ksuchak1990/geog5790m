"""
A script to work on the practical for cellular automata.
@author: ksuchak1990
data_created: 19/03/21
last_modified: 19/03/21
"""
# Imports
from copy import deepcopy

# Functions

# Main
# Set up variables
number_of_iterations = 10
width = 10
height = 10
fire_start_x = 4
fire_start_y = 4
fuel_amount = 5

# Build environment
def make_environment(env_height, env_width):
    """
    Function to create a rectangular grid environment.

    Params
        env_height - height of grid, int
        env_width - width of grid, int
    Returns
        environment - rectangular environment, list of lists
    """
    environment = list()
    for i in range(env_height):
        row_list = list()
        for j in range(env_width):
            row_list.append(fuel_amount)
        environment.append(row_list)
    return environment

def print_environment(env):
    """
    Function to print out a rectangular grid environment.

    Params
        env - rectangular environment to print out, list of lists.
    Returns
        None
    """
    height = len(env)
    # Valid because grid is rectangular
    width = len(env[0])
    for i in range(height):
        for j in range(width):
            print(env[i][j], end=' ')
        print('')
    print('')

def is_adjacent_to_fire_torus(env, h, w):
    """
    Function to check if a given cell is adjacent to a cell that is on fire.
    Assumes toroidal geometry.

    Params
        env - rectangular environment, list of list.
        h - the vertical index of the cell to consider, int.
        w - the horizontal index of the cell to consider, int.

    Returns
        is_adjacent - is cell on adjacent to fire, boolean.
    """
    is_adjacent = False
    height = len(env)
    width = len(env[0])
    adjacent_indices = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                        [0, 1], [1, -1], [1, 0], [1, 1]]
    for diffs in adjacent_indices:
        adj_val = env[(h + diffs[0]) % height][(w + diffs[1]) % width]
        if 0 < adj_val < fuel_amount:
            return True
    return is_adjacent

def is_adjacent_to_fire_wall(env, h, w):
    """
    Function to check if a given cell is adjacent to a cell that is on fire.
    Assumes that boundaries have hard walls.

    Params:
        env - rectangular environment, list of lists.
        h - the vertical index of the cell to consider, int.
        w - the horizontal index of the cell to consider, int.

    Returns:
        is_adjacent - is cell adjacent to fire, boolean.
    """
    is_adjacent = False
    height = len(env)
    width = len(env[0])
    adjacent_indices = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                        [0, 1], [1, -1], [1, 0], [1, 1]]
    for diffs in adjacent_indices:
        h_ind = h + diffs[0]
        w_ind = w + diffs[1]
        is_valid = 0 <= h_ind < height and 0 <= w_ind < width
        if is_valid:
            adj_val = env[h_ind][w_ind]
        else:
            continue
        if 0 < adj_val < fuel_amount:
            return True
    return is_adjacent

def is_dead(env):
    """
    Function to check if an environment is completely burned out.

    Params:
        env - a rectangular environment, list of lists.

    Returns:
        is_dead - whether or not environment is burned, boolean.
    """
    total = 0
    for i, x in enumerate(env):
        total += sum(env[i])
    return not bool(total)

e = make_environment(height, width)
print_environment(e)

# Set a fire
e[fire_start_y][fire_start_x] -= 1
print_environment(e)
results = deepcopy(e)

# Modelling
for t in range(number_of_iterations):
    for h in range(height):
        for w in range(width):
            if is_adjacent_to_fire_wall(e, h, w) and e[h][w] > 0:
                results[h][w] -= 1
    e = deepcopy(results)
    print_environment(e)
    if is_dead(e):
        print('Completed after {0} iterations'.format(t))
        break
