#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re
import string

rows = [r.strip("\n") for r in advent_downloader(5)]
# rows = [r.strip("\n") for r in advent_opener('day_5_example.txt')]

separator = next(i for i,r in enumerate(rows) if r == "")

crates = [re.findall(r'\[([A-Z])\]|\s\s\s\s', r) for r in rows[:separator-1]]
crates = [[c for c in r if c] for r in list(map(list,zip(*crates[::-1])))]

moves = [re.findall(r'\d+', r) for r in rows[separator+1::]]
moves = [[int(m[0]), int(m[1])-1, int(m[2])-1] for m in moves]

def print_top_crates():
  print(''.join([c[-1] for c in crates]))

def move_crates(qnty, src, dest):
  stack = []
  for i in range(qnty):
    stack.append(crates[src].pop())
  for s in stack[::-1]:
    crates[dest].append(s)

for i,m in enumerate(moves):
  move_crates(m[0], m[1], m[2])

print_top_crates()
