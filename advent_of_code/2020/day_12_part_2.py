#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")
half_circle = 180
full_circle = 360


class Waypoint:
    ew = 10
    ns = 1

    def move_cardinal(self, instruction, increment):
        if 'N' == instruction:
            self.ns += increment
        if 'S' == instruction:
            self.ns -= increment
        if 'E' == instruction:
            self.ew += increment
        if 'W' == instruction:
            self.ew -= increment

    def rotate(self, instruction, increment):
        if 'L' == instruction:
            self.rotate_counter_clockwise(self, increment)

        if 'R' == instruction:
            self.rotate_clockwise(self, increment)

    def new_rotate_values(self, new_ew, new_ns):
        self.ew = new_ew
        self.ns = new_ns

    def rotate_counter_clockwise(self, increment):
        if increment == 90:
            self.new_rotate_values(self, -self.ns, self.ew)
        if increment == 180:
            self.new_rotate_values(self, -self.ew, -self.ns)
        if increment == 270:
            self.new_rotate_values(self, self.ns, -self.ew)

    def rotate_clockwise(self, increment):
        if increment == 90:
            self.new_rotate_values(self, self.ns, -self.ew)
        if increment == 180:
            self.new_rotate_values(self, -self.ew, -self.ns)
        if increment == 270:
            self.new_rotate_values(self, -self.ns, self.ew)


class Ship:
    way_point = Waypoint
    ew = 0
    ns = 0

    def move(self, move):
        instruction = move[0]
        increment = int(move[1:])
        if 'L' == instruction or 'R' == instruction:
            self.way_point.rotate(self.way_point, instruction, increment)
        elif 'F' == instruction:
            self.move_forward(increment)
        else:
            self.way_point.move_cardinal(self.way_point, instruction, increment)

    def move_forward(self, increment):
        for i in range(0, increment):
            self.ew += self.way_point.ew
            self.ns += self.way_point.ns


def run_route(moves):
    ship = Ship()
    for move in moves:
        ship.move(move)

    abs_ns = abs(ship.ns)
    abs_ew = abs(ship.ew)
    print("Part 2: Manhattan Distance = {}".format(abs_ns + abs_ew))


def main():
    moves = advent.read_input(os.getcwd(), problem_key.replace("_part_2", ""))
    run_route(moves)


if __name__ == "__main__":
    main()
