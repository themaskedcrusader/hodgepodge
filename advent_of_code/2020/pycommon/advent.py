import re


def get_full_file_path(cwd, problem_key):
    return "{}/input/{}.txt".format(cwd, problem_key)


def read_input(cwd, problem_key):
    file = get_full_file_path(cwd, problem_key)
    ret = []
    data = open(file, 'r')
    lines = data.readlines()
    for line in lines:
        ret.append(line.rstrip())
    return ret


def read_numerical_input(cwd, problem_key):
    file = get_full_file_path(cwd, problem_key)
    ret = []
    data = open(file, 'r')
    lines = data.readlines()
    for line in lines:
        ret.append(int(line))
    return ret


def read_groups_as_row(cwd, problem_key):
    file = get_full_file_path(cwd, problem_key)
    ret = []
    group_string = ""
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        if line.rstrip() == "":
            ret.append(group_string)
            group_string = ""
            continue
        else:
            group_string = "{} {}".format(group_string, line.rstrip())

    # Capture the last group string and return
    ret.append(group_string)
    return ret


bag_key = " bags contain"


def read_baggage(cwd, problem_key):
    file = get_full_file_path(cwd, problem_key)
    ret = {}
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        outer_bag = line.split(bag_key)[0]
        contains  = line.split(bag_key)[1]
        contents = {}
        for bags in contains.split(','):
            results = re.search(" ([0-9]+) ([a-z ]+) bag", bags, re.IGNORECASE)
            if results is not None:
                bag = results.group(2)
                count = results.group(1)
                contents[bag] = count
            else:
                contents = None
        ret[outer_bag] = contents

    return ret



