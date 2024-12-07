input = open('./d5/input.txt', 'r').read().strip()

input = input.split('\n\n')

page_orders = {}

for po in input[0].split('\n'):
    a, b = po.split('|')
    a = int(a)
    b = int(b)
    if b in page_orders:
        page_orders[b].append(a)
    else:
        page_orders[b] = [a]

updates = []

for update in input[1].split('\n'):
    updates.append([int(x) for x in update.split(',')])

total = 0
for update in updates:
    update_copy = update.copy()
    for value in update:
        found = False
        index = update_copy.pop(0)
        if index in page_orders:
            non_allowed_numbers = page_orders[index]
            for y in non_allowed_numbers:
                if y in update_copy:
                    found = True
                    break
            if found:
                break
        if len(update_copy) == 0:
            total += update[int((len(update)-1)/2)]

print(total)