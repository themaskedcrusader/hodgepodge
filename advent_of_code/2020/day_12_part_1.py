#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")
half_circle = 180
full_circle = 360


class Ship:
    direction = 90
    ew = 0
    ns = 0

    def move(self, move):
        instruction = move[0]
        increment = int(move[1:])
        if 'L' == instruction or 'R' == instruction:
            self.change_direction(instruction, increment)
        elif 'F' == instruction:
            self.move_forward(increment)
        else:
            self.move_cardinal(instruction, increment)

    def move_east_west(self, increment):
        if self.direction == 90:
            self.ew += increment
        else:
            self.ew -= increment

    def move_north_south(self, increment):
        if self.direction == half_circle:
            self.ns -= increment
        else:
            self.ns += increment

    def move_cardinal(self, instruction, increment):
        if 'N' == instruction:
            self.ns += increment
        if 'S' == instruction:
            self.ns -= increment
        if 'E' == instruction:
            self.ew += increment
        if 'W' == instruction:
            self.ew -= increment

    def move_forward(self, increment):
        if self.direction % half_circle == 0:
            self.move_north_south(increment)
        else:
            self.move_east_west(increment)

    def re_center(self):
        if self.direction < 0:
            self.direction += full_circle
        if self.direction >= full_circle:
            self.direction -= full_circle

    def change_direction(self, instruction, increment):
        if 'L' == instruction:
            self.direction -= increment

        if 'R' == instruction:
            self.direction += increment

        self.re_center()


def run_route(moves):
    ship = Ship()
    for move in moves:
        ship.move(move)

    abs_ns = abs(ship.ns)
    abs_ew = abs(ship.ew)
    print("Part 1: Manhattan Distance = {}".format(abs_ns + abs_ew))


def main():
    moves = advent.read_input(os.getcwd(), problem_key.replace("_part_1", ""))
    run_route(moves)


if __name__ == "__main__":
    main()
