lines = open('input.txt', 'r').read().split('\n')

left = []
right = []

for x in lines:
    if (len(x)> 0):
        pair = x.split()
        left.append(pair[0])
        right.append(pair[1])

total = 0

left.sort()
right.sort()

for i in range(len(left)):
    total += abs(int(left[i])- int(right[i]))

print(total)