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
        continue

    if (report_values_normal == report_values_normal_sorted or report_values_normal == report_values_reverse_sorted):
        total += 1

print(total)