#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

def reset_flashmap():
    global flash_map
    flash_map = []
    for y in range(len(squids)):
        flash_map.append([False] * len(squids[y]))

squids = [re.findall('\d', r) for r in advent_downloader(11)]
# squids = [re.findall('\d', r) for r in advent_opener('day_11_example.txt')]
squids = [list(map(int,s)) for s in squids]
flash_map = []
reset_flashmap()

    
def flash(x, y, init=False):
    if not init: squids[y][x] += 1

    if (squids[y][x] <= 9 or flash_map[y][x]):
        return

    print(f'{x=}, {y=}')
    flash_map[y][x] = True


    if x-1 >= 0:
        flash(x-1,y)
    if x+1 <= len(squids[y]) - 1:
        flash(x+1, y)

    if y-1 >= 0:
        flash(x,y-1)
        if x-1 >= 0:
            flash(x-1,y-1)
        if x+1 <= len(squids[y]) - 1:
            flash(x+1, y-1)

    if y+1 <= len(squids) - 1:
        flash(x,y+1)
        if x-1 >= 0:
            flash(x-1,y+1)
        if x+1 <= len(squids[y]) - 1:
            flash(x+1,y+1)

def print_squids():
    for y in range(len(squids)):
        print(squids[y])

def step():
    reset_flashmap()

    for y in range(len(squids)):
        for x in range(len(squids[y])):
            squids[y][x] += 1
                
    for y in range(len(squids)):
        for x in range(len(squids[y])):
            flash(x, y, True)

    for y in range(len(squids)):
        for x in range(len(squids[y])):
            if squids[y][x] > 9:
                squids[y][x] = 0

    return sum(row.count(True) for row in flash_map)

i = 1 
while True:
    if step() == len(squids) * len(squids[0]):
        print(i)
        break
    i += 1



        


