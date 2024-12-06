import re
import numpy as np

input = open('./d4/input.txt', 'r').read().strip()

rows = input.split('\n')
matrix = np.array([list(x) for x in rows])

total = 0
for x in range(len(rows)):
    for y in range(len(rows)):
        if matrix[x,y] == 'X':
            if x-3 >= 0:
                if matrix[x-1,y] == 'M' and matrix[x-2,y] == 'A' and matrix[x-3,y] == 'S':
                    total += 1
            if x+3 < len(rows):
                if matrix[x+1,y] == 'M' and matrix[x+2,y] == 'A' and matrix[x+3,y] == 'S':
                    total += 1
            if y-3 >= 0:
                if matrix[x,y-1] == 'M' and matrix[x,y-2] == 'A' and matrix[x,y-3] == 'S':
                    total += 1
            if y+3 < len(rows):
                if matrix[x,y+1] == 'M' and matrix[x,y+2] == 'A' and matrix[x,y+3] == 'S':
                    total += 1
            if x-3 >= 0 and y-3 >= 0:
                if matrix[x-1,y-1] == 'M' and matrix[x-2,y-2] == 'A' and matrix[x-3,y-3] == 'S':
                    total += 1
            if x-3 >= 0 and y+3 < len(rows):
                if matrix[x-1,y+1] == 'M' and matrix[x-2,y+2] == 'A' and matrix[x-3,y+3] == 'S':
                    total += 1
            if x+3 < len(rows) and y+3 < len(rows):
                if matrix[x+1,y+1] == 'M' and matrix[x+2,y+2] == 'A' and matrix[x+3,y+3] == 'S':
                    total += 1
            if x+3 < len(rows) and y-3 >= 0:
                if matrix[x+1,y-1] == 'M' and matrix[x+2,y-2] == 'A' and matrix[x+3,y-3] == 'S':
                    total += 1
print(total)
