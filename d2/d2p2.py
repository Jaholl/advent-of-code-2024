import re

input = open('.\d2\input.txt', 'r').read().strip()

reports = input.split('\n')

total = 0

for report in reports:
    temptotal = total
    skipped = False
    increase = None
    report_values_normal = [int(x) for x in re.findall('\d+', report)]
    for index in range(len(report_values_normal)):
        if(index + 1 == len(report_values_normal)):
            total += 1
            break

        forward = report_values_normal[index + 1] - report_values_normal[index]

        if (forward == 0):
            if (not skipped):
                skipped = True
                continue
            break

        if increase == None:
            increase = forward > 0

        if (0 < forward <= 3):
            if (increase):
                continue
            if (not skipped):
                skipped = True
                continue
            break
        if (-3 <= forward < 0):
            if (not increase):
                continue
            if (not skipped):
                skipped = True
                continue
            break
        if (not skipped):
            skipped = True
            continue
        break
    if (temptotal != total):
        continue
    report_values_normal.reverse()
    skipped = False
    increase = None
    for index in range(len(report_values_normal)):
        if(index + 1 == len(report_values_normal)):
            total += 1
            break
        forward = report_values_normal[index + 1] - report_values_normal[index]

        if (forward == 0):
            if (not skipped):
                skipped = True
                continue
            break

        if increase == None:
            increase = forward > 0

        if (0 < forward <= 3):
            if (increase):
                continue
            if (not skipped):
                skipped = True
                continue
            break
        if (-3 <= forward < 0):
            if (not increase):
                continue
            if (not skipped):
                skipped = True
                continue
            break
        if (not skipped):
            skipped = True
            continue
        break
print(total)