#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def get_password_and_policy(line):
    count = line.split()[0]
    char = line.split()[1]
    password = line.split()[2]

    first_policy_value = count.split('-')[0]
    second_policy_value = count.split('-')[1]
    policy_char = char.replace(':', '')

    return int(first_policy_value), int(second_policy_value), policy_char, password


def is_password_valid_part_1(line):
    min_count, max_count, policy_char, password = get_password_and_policy(line)
    policy_count = password.count(policy_char)
    return (policy_count >= int(min_count)) and (policy_count <= int(max_count))


def is_password_valid_part_2(line):
    index1, index2, policy_char, password = get_password_and_policy(line)
    check_1 = password[index1 - 1] == policy_char
    check_2 = password[index2 - 1] == policy_char
    return check_1 != check_2


def how_many_passwords_valid_part_1(input):
    valid_count = 0
    for line in input:
        if is_password_valid_part_1(line):
            valid_count = valid_count + 1

    print("Part one valid password count = {}".format(valid_count))


def how_many_passwords_valid_part_2(input):
    valid_count = 0
    for line in input:
        if is_password_valid_part_2(line):
            valid_count = valid_count + 1

    print("Part two valid password count = {}".format(valid_count))


def main():
    policy_and_password = advent.read_input(os.getcwd(), problem_key)
    how_many_passwords_valid_part_1(policy_and_password)
    how_many_passwords_valid_part_2(policy_and_password)


if __name__ == "__main__":
    main()
