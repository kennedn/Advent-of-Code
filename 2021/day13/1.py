#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

# rows = [r.strip() for r in advent_opener('e')]
rows = [r.strip() for r in advent_downloader(13)]

dots = [[int(m[1]), int(m[2])] for m in [re.match('^(\d+),(\d+)$', r) for r in rows] if m]

folds = [[m[1], int(m[2])] for m in [re.match('^fold along ([xy])=(\d+)$', r) for r in rows] if m]

paper = [["." for i in range(max([d[0] for d in dots]) + 1)] for j in range(max([d[1] for d in dots]) + 1)]

for d in dots:
    paper[d[1]][d[0]] = "#"
# rows = [r.strip().split("-") for r in advent_opener('day_12_example.txt')]

def combine(paper, axis, idx):
    if axis =='x':
        paper = list(map(list, zip(*paper[::-1])))

    for offset in range(1,len(paper) - idx):
        for x in range(len(paper[offset])):
            if idx - offset < 0:
                break
            paper[idx-offset][x] = paper[idx+offset][x] if paper[idx-offset][x] == '.' else paper[idx-offset][x]
    paper = paper[:idx]
    return list(map(list,zip(*paper)))[::-1] if axis == 'x' else paper

                       
# for f in folds:
f = folds[0]
paper = combine(paper, f[0], f[1])
    
# for p in paper:
#     print(p)

print([p for r in paper for p in r].count("#"))