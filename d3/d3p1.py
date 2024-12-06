import re

input = open('./d3/input.txt', 'r').read().strip()

matches = re.findall(r'mul\((\d+),(\d+)\)', input)

total = 0

for x,y in matches:
    total += int(x) * int(y)

print(total)