#!/usr/bin/python3

import re
import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")
passports = []


def validate_passports():
    ret = []
    passport = {}
    for pass_string in passports:
        # Read Passport into data data structure
        for entry in pass_string.split():
            key = entry.split(":")[0]
            value = entry.split(":")[1]
            passport[key] = value

        # Count elements
        count = len(passport)
        if count == 8 or (count == 7 and passport.get("cid", None) is None):
            ret.append(passport)

        passport = {}

    return ret


def between_valid_inputs(val, min_val, max_val):
    return min_val <= int(val) <= max_val


def is_valid_height(height):
    units = height[-2:]
    value = height[:-2]
    if units == "in":
        return between_valid_inputs(value, 59, 76)
    elif units == "cm":
        return between_valid_inputs(value, 150, 193)
    else:
        return False


def is_valid_hair_color(hcl):
    pattern = re.compile('^#[0-9a-f]{6}$')
    patch = pattern.match(hcl)
    return patch is not None


valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_eye_color(color):
    return color in valid_eye_colors


def is_valid_passport_id(id_number):
    pattern = re.compile("^\d{9}$")
    return pattern.match(id_number)


def is_passport_valid(password):
    return \
        between_valid_inputs (password["byr"], 1920, 2002) and \
        between_valid_inputs (password["iyr"], 2010, 2020) and \
        between_valid_inputs (password["eyr"], 2020, 2030) and \
        is_valid_height      (password["hgt"]) and \
        is_valid_hair_color  (password["hcl"]) and \
        is_valid_eye_color   (password["ecl"]) and \
        is_valid_passport_id (password["pid"])


def how_many_valid_passports_part_1():
    valid_passports = validate_passports()
    print("Valid Passports Part 1 : {}".format(len(valid_passports)))


def how_many_valid_passports_part_2():
    valid_passports = validate_passports()
    valid = 0
    for passport in valid_passports:
        if is_passport_valid(passport):
            valid = valid + 1

    print("Valid Passports Part 2 : {}".format(valid))


def main():
    global passports
    passports = advent.read_groups_as_row(os.getcwd(), problem_key)
    how_many_valid_passports_part_1()
    how_many_valid_passports_part_2()


if __name__ == "__main__":
    main()
