from math import prod

from util import *

data = get_data(3)


def p1(data, right=3, down=1):
    """
    Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
    """
    pos_x = 0
    pos_y = 0
    trees = 0

    while pos_y < len(data):
        section = data[pos_y]
        if section[pos_x] == "#":
            trees += 1
        pos_x = (pos_x + right) % len(section)
        pos_y += down

    return trees


def p2(data):
    """
    Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
    """

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    return prod([p1(data, right, down) for right, down in slopes])


def test():

    data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

    run_tests(p1, [(data, 7)])
    run_tests(p2, [(data, 336)])


test()
print("Result1:", p1(data))
print("Result1:", p2(data))
