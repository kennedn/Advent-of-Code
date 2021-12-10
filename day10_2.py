#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
import re

lines = [l.replace("\n","") for l in advent_downloader(10)]
# lines = [l.replace("\n","") for l in advent_opener('day_10_example.txt')]

openers = re.compile('\(|\[|\{|\<')

closure_map = {
    ')': '(',
    '>': '<',
    '}': '{',
    ']': '['
}

points_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def calc_points(line):
    points = 0
    for l in line:
        points *= 5
        points += points_map[l]
    return points

corrupted_lines = []
for line in lines:
    opener_stack = []
    for c in line:
        if openers.match(c):
            opener_stack.append(c)
        else:
            if len(opener_stack) == 0: break
            if opener_stack[-1] == closure_map[c]:
                opener_stack.pop()
            else:
                opener_stack = [] # corrupted
                break
    if len(opener_stack) > 0:
        corrupted_lines.append(opener_stack[::-1])

corrupted_lines = sorted([calc_points(l) for l in corrupted_lines])
print(corrupted_lines[(len(corrupted_lines) - 1) // 2])