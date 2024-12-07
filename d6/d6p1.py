import numpy as np
import time

input = open('./d6/input.txt', 'r').read().strip()

rows = input.split('\n')
matrix = np.array([list(x) for x in rows])


start_pos = ()
current_pos = []
direction = 'up'

found_start = False
for x in range(len(rows[0])):
    for y in range(len(rows)):
        matrix_value = matrix[x, y]
        if matrix_value == '^':
            start_pos = (x, y)
            found_start = True
            break
    if found_start:
        break

current_pos = [start_pos[0], start_pos[1]]
while (True):
    if direction == 'up':
        if current_pos[0] - 1 < 0:
            break
        if matrix[current_pos[0] - 1, current_pos[1]] == "#":
            direction = 'right'
            continue
        current_pos = [current_pos[0] - 1, current_pos[1]]
        matrix[current_pos[0], current_pos[1]] = 'X'
    
    if direction == 'down':
        if current_pos[0] + 1 == len(rows):
            break
        if matrix[current_pos[0] + 1, current_pos[1]] == "#":
            direction = 'left'
            continue
        current_pos = [current_pos[0] + 1, current_pos[1]]
        matrix[current_pos[0], current_pos[1]] = 'X'
    
    if direction == 'left':
        if current_pos[1] - 1 < 0:
            break
        if matrix[current_pos[0], current_pos[1] - 1] == "#":
            direction = 'up'
            continue
        current_pos = [current_pos[0], current_pos[1] - 1]
        matrix[current_pos[0], current_pos[1]] = 'X'

    if direction == 'right':
        if current_pos[1] + 1 == len(rows):
            break
        if matrix[current_pos[0], current_pos[1] + 1] == "#":
            direction = 'down'
            continue
        current_pos = [current_pos[0], current_pos[1] + 1]
        matrix[current_pos[0], current_pos[1]] = 'X'
    #print()
    #print(matrix)
    #time.sleep(0.200)
visited_squares = 0
for row in matrix:
    visited_squares += sum(1 for x in row if x == 'X' or x == '^')

print(visited_squares)
