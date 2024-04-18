#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


def find_two_digits(input):
    for one_val in input:
        val1 = int(one_val)
        for two_val in input:
            val2 = int(two_val)
            sum = val1 + val2
            if sum == 2020:
                return val1, val2


def find_three_digits(input):
    for one_val in input:
        val1 = int(one_val)
        for two_val in input:
            val2 = int(two_val)
            for three_val in input:
                val3 = int(three_val)
                sum = val1 + val2 + val3
                if sum == 2020:
                    return val1, val2, val3


def product_of_two_entries(input):
    val1, val2 = find_two_digits(input)
    print(" Check  : {} + {} = {}".format(val1, val2, val1+val2))
    print(" VAL 2  : {}".format(val2))
    print(" VAL 1  : {}".format(val1))
    print(" Answer : {}\n".format(val1 * val2))


def product_of_three_entries(input):
    val1, val2, val3 = find_three_digits(input)

    print(" VAL 1  : {}".format(val1))
    print(" VAL 2  : {}".format(val2))
    print(" VAL 3  : {}".format(val3))
    print(" Check  : {} + {} + {} = {}".format(val1, val2, val3, val1+val2+val3))
    print(" Answer : {}\n".format(val1 * val2 * val3))


def main():
    expense_report = advent.read_input(os.getcwd(), problem_key)
    product_of_two_entries(expense_report)
    product_of_three_entries(expense_report)


if __name__ == "__main__":
    main()
