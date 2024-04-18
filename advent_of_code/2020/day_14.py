#!/usr/bin/python3

import os, re
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def get_mask(line):
    return (line.split("=")[1]).strip()


def get_command(line):
    command = re.split('\[|\]| = ', line)
    return int(command[1]), int(command[3])


def get_masked_value(mask, _in):
    ret = list(mask)
    binary_input = list(format(_in, '0{}b'.format(len(mask))))
    for index in range(0, len(mask)):
        if ret[index] == "X":
            ret[index] = binary_input[index]
    return "".join(ret)


def get_masked_address(mask, _in):
    mask = list(mask)
    ret = list(mask)
    binary_input = list(format(_in, '0{}b'.format(len(mask))))
    for index in range(0, len(mask)):
        if mask[index] == "0":
            ret[index] = binary_input[index]
        elif mask[index] == "1":
            ret[index] = "1"
        elif mask[index] == "X":
            ret[index] = "X"
    return "".join(ret)


def get_floating_addresses(address_mask):
    ret = []
    mask_count = address_mask.count("X")
    addresses_to_generate = 2**mask_count
    for i in range(0, addresses_to_generate):
        i = format(i, "0{}b".format(mask_count))
        index = 0
        new_address = list(address_mask)
        for j in range(0, len(new_address)):
            if new_address[j] == "X":
                new_address[j] = i[index]
                index += 1
        ret.append(int("".join(new_address), 2))
    return ret


def calculate_sum(memory):
    ret = 0
    for slot in memory:
        ret += memory[slot]
    return ret


def part_1_initialize(program):
    mask = ''
    mem = {}
    for line in program:
        if line.startswith("mask"):
            mask = get_mask(line)
        else:
            address, value = get_command(line)
            mem[address] = int(get_masked_value(mask, value), 2)
    print("Part 1 : Answer {}".format(calculate_sum(mem)))


def part_2_version_2_initialize(program):
    mask = ''
    mem = {}
    for line in program:
        if line.startswith("mask"):
            mask = get_mask(line)
        else:
            address, value = get_command(line)
            address_mask = get_masked_address(mask, address)
            addresses = get_floating_addresses(address_mask)
            for address in addresses:
                mem[address] = value
    print("Part 2: Answer = {}".format(calculate_sum(mem)))


def main():
    program = advent.read_input(os.getcwd(), problem_key)
    part_1_initialize(program)
    part_2_version_2_initialize(program)


if __name__ == "__main__":
    main()
