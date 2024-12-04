import re
import time
import numpy as np

from InputHelper import InputHelper

helper = InputHelper(4)
data = helper.load_data()


def find_word_in_lines(lines, target_word: str):
    word_count = 0
    for line in lines:
        # left-to-right
        word_count += sum(1 for _ in re.finditer('(?=' + target_word + ')', "".join(line)))
        # right-to-left
        word_count += sum(1 for _ in re.finditer('(?=' + target_word + ')', "".join(line[::-1])))
    return word_count


def find_word_count(lines):
    word_count = 0
    target_word = "XMAS"
    np_array = np.array([list(x) for x in lines])

    # left-right
    word_count += find_word_in_lines(np_array, target_word)

    # top-bottom
    transposed_list = np.rot90(np_array, 1)
    word_count += find_word_in_lines(transposed_list, target_word)

    # Diagonal Part - oh boy here we go
    for i in range(len(np_array)):
        for j in range(len(np_array[0])):
            if np_array[i][j] == 'X':
                # top-left to bottom-right
                if i + 3 < len(np_array) and j + 3 < len(np_array[0]):
                    word_count += 1 if (np_array[i + 1][j + 1] == 'M' and np_array[i + 2][j + 2] == 'A' and np_array[i + 3][j + 3] == 'S') else 0
                if i + 3 < len(np_array) and j - 3 >= 0:
                    word_count += 1 if (np_array[i + 1][j - 1] == 'M' and np_array[i + 2][j - 2] == 'A' and np_array[i + 3][j - 3] == 'S') else 0
                if i - 3 >= 0 and j + 3 < len(np_array[0]):
                    word_count += 1 if (np_array[i - 1][j + 1] == 'M' and np_array[i - 2][j + 2] == 'A' and np_array[i - 3][j + 3] == 'S') else 0
                if i - 3 >= 0 and j - 3 >= 0:
                    word_count += 1 if (np_array[i - 1][j - 1] == 'M' and np_array[i - 2][j - 2] == 'A' and np_array[i - 3][j - 3] == 'S') else 0

    return word_count


def find_correct_x_shaped_word_count(lines):
    word_count = 0
    np_array = np.array([list(x) for x in lines])

    for i in range(len(np_array)):
        for j in range(len(np_array[0])):
            if np_array[i][j] == 'A':
                if i + 1 < len(np_array) and i - 1 >= 0 and j + 1 < len(np_array[0]) and j - 1 >= 0:
                    word_count += 1 if ((np_array[i + 1][j + 1] == 'M' and np_array[i - 1][j - 1] == 'S' or np_array[i + 1][j + 1] == 'S' and np_array[i - 1][j - 1] == 'M') and
                                        (np_array[i - 1][j + 1] == 'M' and np_array[i + 1][j - 1] == 'S' or np_array[i - 1][j + 1] == 'S' and np_array[i + 1][j - 1] == 'M')) else 0
    return word_count


start = time.time()
task1Sum = find_word_count(data)
print("The word 'XMAS' is appearing {} times in the word search, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = find_correct_x_shaped_word_count(data)
print("The word 'MAS' is appearing {} times in the corrected word search, calculated in {:.2f}ms".format(task2Sum, (time.time() - start) * 1000))
