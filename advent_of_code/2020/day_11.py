#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")
occupied = '#'
empty = 'L'


class FloorMapCalculator:

    @staticmethod
    def is_out_of_bounds(a, b, x, y, width, height):
        return a < 0 or b < 0 or a > width - 1 or b > height - 1 or (a == x and b == y)

    @staticmethod
    def get_seat_in_angle(data_set, x, y, delta_x, delta_y, width, height):
        while True:
            x = x + delta_x
            y = y + delta_y
            if FloorMapCalculator.is_out_of_bounds(x, y, -1, -1, width, height):
                return empty
            elif data_set[x][y] == occupied:
                return occupied
            elif data_set[x][y] == empty:
                return empty

    @staticmethod
    def adjacent_occupied_v1(data_set, x, y, width, height):
        ret = 0
        for a in range(x-1, x+2):
            for b in range(y-1, y+2):
                if FloorMapCalculator.is_out_of_bounds(a, b, x, y, width, height):
                    continue
                else:
                    if data_set[a][b] == '#':
                        ret += 1
        return ret

    @staticmethod
    def adjacent_occupied_v2(data_set, x, y, width, height):
        ret = 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y, -1, -1, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y, -1,  0, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y, -1,  1, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y,  0, -1, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y,  0,  1, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y,  1, -1, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y,  1,  0, width, height) == occupied else 0
        ret += 1 if FloorMapCalculator.get_seat_in_angle(data_set, x, y,  1,  1, width, height) == occupied else 0
        return ret

    @staticmethod
    def run_rules(floor_map, occupied_calculator=None, occupied_limit=0):
        calculator = getattr(FloorMapCalculator, occupied_calculator)
        width = len(floor_map[0])
        height = len(floor_map)
        ret = [[0 for x in range(width)] for y in range(height)]
        for x in range(width):
            for y in range(height):
                seated = calculator(floor_map, x, y, width, height)
                if floor_map[x][y] == occupied and seated >= occupied_limit:
                    ret[x][y] = empty
                elif floor_map[x][y] == empty and seated == 0:
                    ret[x][y] = occupied
                else:
                    ret[x][y] = floor_map[x][y]
        return ret

    @staticmethod
    def count_occupied(floor_map):
        ret = 0
        for x in range(len(floor_map[0])):
            for y in range(len(floor_map)):
                if floor_map[x][y] == occupied:
                    ret += 1
        return ret


def seating_model(data_set, part, occupied_calculator, limit):
    before = data_set
    while True:
        after = FloorMapCalculator.run_rules(
            before,
            occupied_calculator=occupied_calculator,
            occupied_limit=limit)
        if before == after:
            break
        else:
            before = after
    print("Part {}: Seats occupied = {}".format(part, FloorMapCalculator.count_occupied(after)))


def main():
    data_set = advent.read_input(os.getcwd(), problem_key)
    seating_model(data_set, 1, "adjacent_occupied_v1", 4)
    seating_model(data_set, 2, "adjacent_occupied_v2", 5)


if __name__ == "__main__":
    main()
