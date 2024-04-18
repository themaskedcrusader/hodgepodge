#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def trees_encountered_part_2(input):
    trees = [
        trees_encountered(1, 1, input),
        trees_encountered(3, 1, input),
        trees_encountered(5, 1, input),
        trees_encountered(7, 1, input),
        trees_encountered(1, 2, input)
    ]
    product = 1
    for tree in trees:
        product = product * tree

    print("Product of runs: {}".format(product))


def trees_encountered(right, down, input):
    current = 0
    length = 0
    trees = 0
    count = 0
    for row in input:
        temp = list(row)
        if length == 0:             # Eat first row, continue
            length = len(row) - 1
            count = count + 1
            continue
        current = current + right   # move right
        if current > length:
            current = current - length - 1

        if count % down == 0:       # If we've moved down enough, run the calculation
            if temp[current] == '#':
                trees = trees + 1
        else:
            current = current - right   # we need to move down at least one more row, undo right slope
        count = count + 1

    print("Trees Encountered = {}".format(trees))
    return trees


def main():
    forest_layout = advent.read_input(os.getcwd(), problem_key)
    trees_encountered(3, 1, forest_layout)
    trees_encountered_part_2(forest_layout)


if __name__ == "__main__":
    main()
