prev = 0
balance = 0
day = 0
longest_dep1 = 0
longest_dep2 = 0
longest_day = 0
wins = 0


def start_game(deposit_1, deposit_2):
    global day, balance, prev
    day = 2
    prev = deposit_1
    balance = deposit_1 + deposit_2
    day_loop()


def day_loop():
    global day, balance, prev
    day += 1
    prev_tmp = prev
    prev = balance
    balance += prev_tmp
    if balance >= 1000000:
        return
    else:
        day_loop()


def run_test():
    global balance, day, longest_day
    for dep1 in range(1, 1000):
        for dep2 in range(1, 1000):
            start_game(dep1, dep2)
            if balance == 1000000:
                print(">>>>>> WE WON AFTER {} days".format(day))
                global wins
                wins += 1
                if day > longest_day:
                    global longest_dep1, longest_dep2
                    longest_day = day
                    longest_dep1 = dep1
                    longest_dep2 = dep2
    print("Our longest run was {} days with deposits {} and {}".format(longest_day, longest_dep1, longest_dep2))


if __name__ == '__main__':
    run_test()

