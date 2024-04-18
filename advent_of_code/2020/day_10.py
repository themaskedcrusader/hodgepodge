#!/usr/bin/python3

import os
import pycommon.advent as advent
from collections import Counter

problem_key = os.path.basename(__file__).replace(".py", "")


def part_1_divine_jolts(data_set):
    data_set.sort()
    previous = 0
    ones = threes = 0
    for value in data_set:
        if int(value) == previous + 1:
            ones += 1
        elif int(value) == previous + 3:
            threes += 1
        previous = int(value)
    threes += 1
    return ones, threes


def part_2_how_many_possible_combinations(data_set):
    data_set.sort()
    data_set.append(data_set[-1] + 3)  # target value

    counts_to_power = Counter()
    counts_to_power[0] = 1

    for value in data_set:
        counts_to_power[value] = \
            counts_to_power[value - 1] + \
            counts_to_power[value - 2] + \
            counts_to_power[value - 3]

    return counts_to_power[data_set[-1]]


def main():
    data_set = advent.read_numerical_input(os.getcwd(), problem_key)
    singles, triples = part_1_divine_jolts(data_set)
    print("Part 1: Ones {}, threes {} = product {}".format(singles, triples, singles * triples))
    possible_combinations = part_2_how_many_possible_combinations(data_set)
    print("Part 2: Possible Combinations: {}".format(possible_combinations))


if __name__ == "__main__":
    main()
