from util import run_tests, get_data

import re

data = get_data(2)

def p1(data):
    """
    Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
    """
    matches = 0
    expression = r'(\d+)-(\d+) (.): (\w*)'
    for line in data:
        min_num, max_num, target, pw = re.search(expression, line).groups()
        if pw.count(target) <= int(max_num) and pw.count(target) >= int(min_num):
            matches += 1
    return matches


def p2(data):
    """
    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
    """
    matches = 0
    expression = r'(\d+)-(\d+) (.): (\w*)'
    for line in data:
        index1, index2, target, pw = re.search(expression, line).groups()
        if (pw[int(index1) - 1] == target) != (pw[int(index2) - 1] == target):
            matches += 1 

    return matches


def test():
    data = """
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc"""

    run_tests(p1, [(data, 2)])

    run_tests(p2, [(data, 1)])


test()
print("Result1:", p1(data))
print("Result1:", p2(data))