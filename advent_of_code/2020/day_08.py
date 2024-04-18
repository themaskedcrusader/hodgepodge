#!/usr/bin/python3

import copy
import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def run_the_program(code):
    acc_value = 0
    current_step = 0
    past_instructions = []
    while current_step not in past_instructions:
        if current_step == len(code):
            return acc_value, True
        past_instructions.append(current_step)
        instruction, value = code[current_step].split()
        if instruction == "acc":
            acc_value += int(value)
            current_step += 1
        elif instruction == "jmp":
            current_step += int(value)
        elif instruction == "nop":
            current_step += 1
    return acc_value, False


def get_status(result):
    if result:
        return "passed"
    else:
        return "crashed"


def flip(instruction):
    if instruction == "jmp":
        return "nop"
    return "jmp"


def fix_code(code, test):
    attempt = copy.deepcopy(code)
    found = -1
    for count in range(0, len(code)):
        instruction, value = code[count].split()
        if instruction == "jmp" or instruction == "nop":
            found += 1
            if found == test:
                instruction = flip(instruction)
                attempt[count] = "{} {}".format(instruction, value)
                return test + 1, attempt


def part_one_infinite_loop(code):
    acc_value, success = run_the_program(code)
    status = get_status(success)
    print("Part 1: The program {}; acc value = {}".format(status, acc_value))


def part_two_attempt_a_fix(code):
    acc_value = 0
    passed = False
    test = 0
    while not passed:
        test, attempt = fix_code(code, test)
        acc_value, passed = run_the_program(attempt)
    print("Part 2: the program passed after {} tests ; acc value = {}".format(test, acc_value))


def main():
    code = advent.read_input(os.getcwd(), problem_key)
    part_one_infinite_loop(code)
    part_two_attempt_a_fix(code)

if __name__ == "__main__":
    main()
