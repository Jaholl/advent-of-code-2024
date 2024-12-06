import re

input = open('./d2/input.txt', 'r').read().strip()

reports = input.split('\n')

total = 0

for report in reports:
    increase = None
    found = False

    report_values_normal = [int(x) for x in re.findall(r'\d+', report)]
    for index in range(len(report_values_normal)):
        if(index + 1 == len(report_values_normal)):
            found = True
            total += 1
            break

        forward = report_values_normal[index + 1] - report_values_normal[index]

        if (forward == 0):
            break

        if increase == None:
            increase = forward > 0

        if (0 < forward <= 3):
            if (increase):
                continue
            break
        if (-3 <= forward < 0):
            if (not increase):
                continue
            break
        break

    if found:
        continue
    
    for index in range(len(report_values_normal)):
        increase = None
        report_copy = report_values_normal.copy()
        report_copy.pop(index)
        for i in range(len(report_copy)):
            if(i + 1 == len(report_copy)):
                total += 1
                found = True
                break

            forward = report_copy[i + 1] - report_copy[i]

            if (forward == 0):
                break

            if increase == None:
                increase = forward > 0

            if (0 < forward <= 3):
                if (increase):
                    continue
                break
            if (-3 <= forward < 0):
                if (not increase):
                    continue
                break
            break
        if found:
            break

print(total)