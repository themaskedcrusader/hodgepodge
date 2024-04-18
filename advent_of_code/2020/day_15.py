#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def play_game(part, start_sequence, end_state):
    found_numbers = {}
    next_number = last_round = this_round = 0
    for count in range(0, end_state):
        if last_round:
            next_number = this_round - last_round
        else:
            next_number = 0
        this_round = count + 1
        if count < len(start_sequence):
            next_number = int(start_sequence[count])
        last_round = found_numbers.get(next_number, 0)
        found_numbers[next_number] = this_round
    print("Part {}: Answer {}".format(part, next_number))


def main():
    game_start = advent.read_input(os.getcwd(), problem_key)[0].split(",")
    play_game(1, game_start, 2020)
    play_game(2, game_start, 30000000)


if __name__ == "__main__":
    main()
