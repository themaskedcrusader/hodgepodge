#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def remove_duplicates(bags):
    ret = []
    for bag in bags:
        if len(ret) == 0:
            ret.append(bag)
        else:
            if bag not in ret:
                ret.append(bag)
    return ret


def find_nested_bags(rules, search):
    bags = []
    for bag in rules:
        contents = rules[bag]
        if contents is not None:
            for sub_bag in contents:
                if sub_bag == search:
                    bags.append(bag)
                    more = find_nested_bags(rules, bag)
                    for item in more:
                        bags.append(item)
    return bags


def count_nested_bags(rules, search):
    ret = 1
    my_bag = rules[search]
    if my_bag is not None:
        for sub_bag in my_bag:
            how_many = int(my_bag[sub_bag])
            count = count_nested_bags(rules, sub_bag)
            ret += how_many * count
    return ret


def part_one_how_many_bags(rules):
    search = "shiny gold"
    bags = remove_duplicates(find_nested_bags(rules, search))
    print("Part 1: Found {} bags in {} bags".format(search, len(bags)))


def part_two_how_many_bags(rules):
    search = "shiny gold"
    bags = count_nested_bags(rules, search)
    print("Part 2: Found {} bags in a single {} bag".format(bags - 1, search))


def main():
    rules = advent.read_baggage(os.getcwd(), problem_key)
    part_one_how_many_bags(rules)
    part_two_how_many_bags(rules)


if __name__ == "__main__":
    main()
