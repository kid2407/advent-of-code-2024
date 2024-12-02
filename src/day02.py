import time

from InputHelper import InputHelper

helper = InputHelper(2)
data = helper.load_data()


def parse_reports(reports):
    parsed = []

    for line in reports:
        parsed.append([int(number) for number in line.split(' ')])

    return parsed


def is_safe_report(report, with_dampener=False):
    last_number = None
    increasing = None
    is_safe = True
    for number in report:
        if last_number is not None:
            if abs(number - last_number) > 3 or last_number == number:
                is_safe = False
                break
            if (increasing is True and number < last_number) or (increasing is False and number > last_number):
                is_safe = False
                break
            if increasing is None:
                increasing = number > last_number
        if increasing is None and last_number is not None:
            increasing = number > last_number
        last_number = number
    return is_safe


def determine_safe_reports(reports, with_dampener=False):
    safe_count = 0

    for report in reports:
        is_safe = is_safe_report(report)
        if not is_safe and with_dampener is True:
            for index in range(0, len(report)):
                modified_report = report[:index] + report[index + 1:]
                if is_safe_report(modified_report):
                    is_safe = True
                    break
        safe_count += 1 if is_safe else 0

    return safe_count


report_list = parse_reports(data)

start = time.time()
task1Sum = determine_safe_reports(report_list)
print("The number of safe reports is {}, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = determine_safe_reports(report_list, True)
print("The number of safe report with the dampener correction is {}, calculated in {:.2f}ms".format(task2Sum, (
        time.time() - start) * 1000))
