import time

from InputHelper import InputHelper

helper = InputHelper(1)
data = helper.load_data()


def parse_data(input_data):
    left = []
    right = []

    for line in input_data:
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r))

    return left, right


def pair_numbers_and_sum(left, right):
    final_sum = 0

    left.sort()
    right.sort()

    for index, left_num in enumerate(left):
        right_num = right[index]
        final_sum += abs(right_num - left_num)

    return final_sum


def similar_numbers_result(left, right):
    final_sum = 0
    right_number_index_list = {}
    right_numbers_count = {}

    left.sort()
    right.sort()

    for key, left_number in enumerate(left):
        if left_number in right_numbers_count:
            final_sum += right_numbers_count[left_number]
            continue
        if left_number not in right_number_index_list:
            start_index = 0
        else:
            start_index = right_number_index_list[left_number]
        current_number_count = 0
        for index, number in enumerate(right, start_index):
            if number < left_number:
                continue
            elif number == left_number:
                current_number_count += 1
            elif number > left_number:
                break
        current_number_result = current_number_count * left_number
        if not left_number in right_numbers_count:
            right_numbers_count[left_number] = current_number_result
        if not left_number in right_number_index_list:
            right_number_index_list[left_number] = index
        final_sum += current_number_result

    return final_sum


left_list, right_list = parse_data(data)

start = time.time()
task1Sum = pair_numbers_and_sum(left_list, right_list)
print("The sum of differences is {}, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = similar_numbers_result(left_list, right_list)
print("The sum of similarities is {}, calculated in {:.2f}ms".format(task2Sum, (time.time() - start) * 1000))
