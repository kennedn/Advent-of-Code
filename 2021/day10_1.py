#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
import re

lines = [l.replace("\n","") for l in advent_downloader(10)]
lines = [l.replace("\n","") for l in advent_opener('day_10_example.txt')]

openers = re.compile('\(|\[|\{|\<')

closure_map = {
    ')': '(',
    '>': '<',
    '}': '{',
    ']': '['
}

points_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

opener_stack = []
corrupted_chars = []
for line in lines:
    for c in line:
        if openers.match(c):
            opener_stack.append(c)
        elif len(opener_stack) > 0:
            if opener_stack[-1] == closure_map[c]:
                opener_stack.pop()
            else:
                corrupted_chars.append(c)
                break
        else:
            break

print(sum([points_map[c] for c in corrupted_chars]))

