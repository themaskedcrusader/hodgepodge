#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")
question_groups = []


def get_unique_counts(line):
    line = line.replace(' ', '')
    counts = {}
    for index in range(0, len(line)):
        key = line[index]
        counts[key] = True
    return counts


def part_one_sum_of_counts():
    sum = 0
    for line in question_groups:
        counts = get_unique_counts(line)
        sum += len(counts)
    print("Part 1: Sum of counts: {}".format(sum))


def part_two_sum_of_counts():
    sum = 0
    for line in question_groups:
        possible = {}
        populated = False
        for word in line.split():
            if len(possible) == 0 and not populated:
                possible = get_unique_counts(word)
                populated = True
            else:
                next_count = get_unique_counts(word)
                to_remove = {}
                for key in possible:
                    if key not in next_count:
                        to_remove[key] = True

                for key in to_remove:
                    del possible[key]
        sum += len(possible)
    print("Part 2: Sum of counts: {}".format(sum))


def main():
    global question_groups
    question_groups = advent.read_groups_as_row(os.getcwd(), problem_key)
    part_one_sum_of_counts()
    part_two_sum_of_counts()

if __name__ == "__main__":
    main()
