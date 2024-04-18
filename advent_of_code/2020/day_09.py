#!/usr/bin/python3

from collections import deque

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def is_valid(value, data_set):
    for value1 in data_set:
        for value2 in data_set:
            if int(value1) != int(value2) and int(value1) + int(value2) == int(value):
                return True
    return False


def find_flaw(data_set, index, length):
    flaw_set = []
    for i in range(0, length):
        flaw_set.append(data_set[index + i])
    print("Part 2: Flaw index value : {}".format(int(min(flaw_set)) + int(max(flaw_set))))


def part_1_first_failure(data_set, preamble_size):
    count = 0
    queue = deque()
    for value in data_set:
        if count < preamble_size:
            queue.append(value)
            count += 1
        else:
            if not is_valid(value, queue):
                print("Part 1: First Failure in set : {}".format(value))
                return value
            else:
                queue.popleft()
                queue.append(value)


def part_2_find_weakness_value(data_set, failure_value):
    index = 0
    while index < len(data_set):
        check_value = length = 0
        for idx in range(index, len(data_set)):
            check_value += int(data_set[idx])
            length += 1
            if check_value == int(failure_value):
                find_flaw(data_set, index, length)
                return
            elif check_value > int(failure_value):
                index += 1
                break


def main():
    data_set = advent.read_input(os.getcwd(), problem_key)
    failure_value = part_1_first_failure(data_set, 25)
    part_2_find_weakness_value(data_set, failure_value)


if __name__ == "__main__":
    main()
