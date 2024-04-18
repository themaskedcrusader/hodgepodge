#!/usr/bin/python3

import os
import pycommon.advent as advent

# Notes: Row Binary: F = 0, B = 1
#       Seat Binary: L = 0, R = 1
# Seat ID = (row * 8) + seat
# highest seat id: 1023

problem_key = os.path.basename(__file__).replace(".py", "")


def get_seat_id(boarding_pass):
    row_bits = boarding_pass[:-3]
    row_bits = row_bits.replace("F", "0")
    row_bits = row_bits.replace("B", "1")
    row = int(row_bits, 2)

    seat_bits = boarding_pass[-3:]
    seat_bits = seat_bits.replace("L", "0")
    seat_bits = seat_bits.replace("R", "1")
    seat = int(seat_bits, 2)

    return (row * 8) + seat


def highest_boarding_pass_value(boarding_passes):
    max_id = 0
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass)

        if seat_id > max_id:
            max_id = seat_id

    print("Part 1: The maximum seat id is {}".format(max_id))


def what_s_my_seat_number(boarding_passes):
    seats = []
    for boarding_pass in boarding_passes:
        seats.append(get_seat_id(boarding_pass))

    seats.sort()
    previous = 0

    for seat in seats:
        if previous == 0:
            previous = seat
            continue
        elif previous != seat - 1:
            print("Part 2: My seat is {}".format(seat - 1))
            return
        else:
            previous = seat


def main():
    boarding_passes = advent.read_input(os.getcwd(), problem_key)
    highest_boarding_pass_value(boarding_passes)
    what_s_my_seat_number(boarding_passes)


if __name__ == "__main__":
    main()
