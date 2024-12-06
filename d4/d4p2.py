import re
import numpy as np

input = open('./d4/input.txt', 'r').read().strip()

rows = input.split('\n')
matrix = np.array([list(x) for x in rows])

total = 0
for x in range(len(rows)):
    for y in range(len(rows)):
        if matrix[x,y] == 'A':
            if x-1 >= 0 and y-1 >= 0 and x-1 >= 0 and y+1 < len(rows) and x+1 < len(rows) and y+1 < len(rows) and x+1 < len(rows) and y-1 >= 0:
                if (matrix[x-1,y-1] == 'M' and matrix[x+1,y+1] == 'S' or  matrix[x-1,y-1] == 'S' and matrix[x+1,y+1] == 'M') and (matrix[x+1,y-1] == 'M' and matrix[x-1,y+1] == 'S' or  matrix[x+1,y-1] == 'S' and matrix[x-1,y+1] == 'M'):
                    total += 1
print(total)
