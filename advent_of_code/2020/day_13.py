#!/usr/bin/python3

import os
from math import gcd

import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def part_1_which_bus(earliest, routes):
    time = int(earliest)
    rem = time
    chosen_route = 0
    for route in routes.split(','):
        if route == 'x':
            continue
        else:
            route = int(route)
            new_rem = -(time % route) + route
            if new_rem < rem:
                rem = new_rem
                chosen_route = route
    print("Part 1: Answer {}".format(rem * chosen_route))


def part_2_which_offset(route_list):
    routes = []
    for index, route in enumerate(route_list):
        if route != 'x':
            routes.append([index, int(route)])

    test = routes[0][0]
    offset = routes[0][1]
    harmony = []
    found = False
    while not found:
        test += offset
        for index, route in routes:
            if (test + index) % route != 0:
                break
            elif route not in harmony:
                # found harmony between routes
                harmony.append(route)
                offset = (route * offset) // gcd(route, offset)
        else:
            found = True

    print("Part 2: Answer {}".format(test))


def main():
    earliest, routes = advent.read_input(os.getcwd(), problem_key)
    part_1_which_bus(earliest, routes)
    part_2_which_offset(routes.split(","))


if __name__ == "__main__":
    main()
