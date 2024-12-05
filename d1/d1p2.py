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

for l in [int(a) for a in left]:
    for r in [int(a) for a in right]:
        if l == r:
            total += l

print(total)