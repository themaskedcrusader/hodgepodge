#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")
acceptance_criteria = {}
valid_tickets = []
field_columns = {}


def get_valid_values(value_range):
    ret = []
    for value in range(int(value_range[0]), int(value_range[1]) + 1):
        ret.append(value)
    return ret


def parse_acceptance_criteria(input_data):
    for line in input_data:
        if line == "":
            break
        category, data = line.split(":")
        data = data.split(" ")
        valid_values = get_valid_values(data[1].split("-"))
        valid_values = valid_values + (get_valid_values(data[3].split("-")))
        acceptance_criteria[category] = valid_values


def value_in_acceptance_criteria(value):
    for _, key in enumerate(acceptance_criteria):
        if value in acceptance_criteria[key]:
            return True
    return False


def which_field(values):
    fields = []
    for key in acceptance_criteria:
        criteria_values = acceptance_criteria[key]
        found = True
        for value in values:
            if value not in criteria_values:
                found = False
                break
        if found:
            fields.append(key)
    return fields


def sanitize_fields(source_set):
    ret = {}
    while True:
        for key in ret:
            pop_key = ret[key]
            source_set.pop(pop_key, None)
        if len(source_set) == 0:
            break
        for key in source_set:
            values = source_set[key]
            if len(values) == 1:
                value = values[0]
                ret[value] = key
                for sub_key in source_set:
                    values = source_set[sub_key]
                    if value in values:
                        values.remove(value)
    return ret


def part_1_nearby_tickets_error_scanning_rate(input_data):
    read_lines = False
    scanning_error_rate = 0
    for line in input_data:
        if line.startswith("nearby"):
            read_lines = True
            continue
        if read_lines:
            valid = True
            for value in line.split(","):
                value = int(value)
                if not value_in_acceptance_criteria(value):
                    valid = False
                    scanning_error_rate += value
            if valid:
                valid_tickets.append(line)
    print("Part 1: Scanning error rate {}".format(scanning_error_rate))


def part_2_which_field_is_which():
    column_values = {}
    column_fields = {}
    for valid_ticket in valid_tickets:
        columns = valid_ticket.split(",")
        count = 1
        for column in columns:
            values = column_values.get(count, [])
            values.append(int(column))
            column_values[count] = values
            count += 1
    for key in column_values:
        values = column_values[key]
        column_fields[key] = which_field(values)
    global field_columns
    field_columns = sanitize_fields(column_fields)


def part_2_which_is_my_seat(input_data):
    my_ticket = []
    found = False
    for line in input_data:
        if line.startswith("your"):
            found = True
            continue
        if found:
            my_ticket = line.split(",")
            break

    product = 1
    for key in field_columns:
        if key.startswith("departure"):
            cell = field_columns[key]
            product *= int(my_ticket[cell - 1])
    print("Part 2: Answer {}".format(product))


def main():
    input_data = advent.read_input(os.getcwd(), problem_key)
    parse_acceptance_criteria(input_data)
    part_1_nearby_tickets_error_scanning_rate(input_data)
    part_2_which_field_is_which()
    part_2_which_is_my_seat(input_data)


if __name__ == "__main__":
    main()
