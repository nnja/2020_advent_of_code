from itertools import combinations
from math import prod
from util import *

data = get_data(1)


def p1(data):
    """
    find the two entries that sum to 2020 and then multiply those two numbers together.
    """
    copy = data[:]
    for item1 in data:
        for item2 in data:
            if int(item1) + int(item2) == 2020:
                return int(item1) * int(item2)


def p1_optimized(data, num_combos=2):
    data = map(int, data)
    return [
        prod(items) for items in combinations(data, num_combos) if sum(items) == 2020
    ][0]


def p2(data):
    for item1 in data:
        for item2 in data:
            for item3 in data:
                if int(item1) + int(item2) + int(item3) == 2020:
                    return int(item1) * int(item2) * int(item3)


def p2_optimized(data):
    return p1_optimized(data, num_combos=3)


def test():
    test_data = """
    1721
    979
    366
    299
    675
    1456"""

    run_tests(p1, [(test_data, 514579)])
    run_tests(p1_optimized, [(test_data, 514579)])
    run_tests(p2, [(test_data, 241861950)])
    run_tests(p2_optimized, [(test_data, 241861950)])


test()
print("Result1:", p1_optimized(data))
print("Result2:", p2_optimized(data))