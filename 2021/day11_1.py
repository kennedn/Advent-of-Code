#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

rows = [list(map(int, r.replace("\n", ""))) for r in advent_opener('day_11_example.txt')]
yellow = '\u001b[47;1m\u001b[30;1m'
reset = '\u001b[0m'

def neighbours(rows, x, y):
    n = {}
    if (x - 1 >= 0):
        n['left'] = [x - 1, y]
    if (x + 1 < len(rows[0])):
        n['right'] = [x + 1, y]
    if (y - 1 >= 0):
        n['up'] = [x, y - 1]
    if (y + 1 < len(rows)):
        n['down'] = [x, y + 1]

    if ('left' in n and 'up' in n):
        n['left_up'] = [x - 1, y - 1]
    if ('right' in n and 'up' in n):
        n['right_up'] = [x + 1, y - 1]
    if ('left' in n and 'down' in n):
        n['left_down'] = [x - 1, y + 1]
    if ('right' in n and 'down' in n):
        n['right_down'] = [x + 1, y + 1]

    return list(n.values())
    
flashes = 0
for day in range(10):
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if col == 0:
                flashes += 1
                for x_pos, y_pos in neighbours(rows, x, y):
                    rows[y_pos][x_pos] = (rows[y_pos][x_pos] + 1) % 9
                    if rows[y_pos][x_pos] == 0:
                        flashes += 1
    for y, row in enumerate(rows):
        for x, val in enumerate(row):
            if val == 0:
                print(f"{yellow}{val}{reset}", end=",")
            else:
                print(val, end=",")
        print()


print(flashes)
