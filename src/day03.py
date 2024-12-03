import re
import time

from InputHelper import InputHelper

helper = InputHelper(3)
data = helper.load_data(as_string=True)


def sum_valid_mul_instructions(line):
    valid_sum = 0

    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    for match in matches:
        valid_sum += int(match[0]) * int(match[1])

    return valid_sum


def sum_valid_with_do_and_dont(line):
    valid_sum_with_do_dont = 0
    allowed = True
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)", line)
    for match in matches:
        if match == "do()":
            allowed = True
        elif match == "don't()":
            allowed = False
        elif allowed and match.startswith("mul("):
            mul_match = re.search(r'mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)', match)
            valid_sum_with_do_dont += int(mul_match.group('first')) * int(mul_match.group('second'))

    return valid_sum_with_do_dont


start = time.time()
task1Sum = sum_valid_mul_instructions(data)
print("The sum of valid mul instructions is {}, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = sum_valid_with_do_and_dont(data)
print("The sum of valid mul instructions with do's and don'ts is {}, calculated in {:.2f}ms".format(task2Sum, (time.time() - start) * 1000))
