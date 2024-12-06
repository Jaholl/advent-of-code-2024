import re

input = open('./d3/input.txt', 'r').read().strip()

matches = re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', input)

total = 0
print(matches)
do_is_true = True

for x,y,do,dont in matches:
    if (do):
        do_is_true = True
        continue
    elif (dont):
        do_is_true = False
        continue

    if (do_is_true):
        total += int(x) * int(y)

print(total)