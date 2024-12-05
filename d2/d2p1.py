import re

input = open('.\d2\input.txt', 'r').read().strip()

reports = input.split('\n')

total = 0

for report in reports:
    report_values_normal = [int(x) for x in re.findall('\d+', report)]
    #print ("values: ", report_values_normal)
    if (len(set(report_values_normal)) < len(report_values_normal)):
        continue

    report_values_normal_sorted = [int(x) for x in re.findall('\d+', report)]
    report_values_reverse_sorted = [int(x) for x in re.findall('\d+', report)]
    report_values_normal_sorted.sort()
    report_values_reverse_sorted.sort(reverse=True)

    differences = [(j-i) for i,j in zip(report_values_normal, report_values_normal[1:])]
    if (any((0 == x or x > 3 or x < -3) for x in differences)):
        unsave_levels = sum(1 for i in differences if i > 3 or i < -3 or i == 0)
        if (unsave_levels == 1):
            report_values_normal = [i for i in differences if i <= 3 and i >= -3 and i != 0]
            report_values_normal_sorted = [i for i in differences if i <= 3 and i >= -3 and i != 0]
            report_values_reverse_sorted = [i for i in differences if i <= 3 and i >= -3 and i != 0]
            report_values_normal_sorted.sort()
            report_values_reverse_sorted.sort(reverse=True)
            if (report_values_normal == report_values_normal_sorted or report_values_normal == report_values_reverse_sorted):
                print(report_values_normal)
                print(report_values_normal_sorted)
                print(report_values_reverse_sorted)
                total += 1
        continue

    if (report_values_normal == report_values_normal_sorted or report_values_normal == report_values_reverse_sorted):
        total += 1

print(total)