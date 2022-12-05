#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re
import string

rows = [r.strip("\n") for r in advent_downloader(5)]

crates = [[f[1] for f in re.findall(r'\[[A-Z]\]|\s\s\s\s', r)] for r in rows[:8]]
crates = [[c for c in r if c in string.ascii_uppercase] for r in list(map(list,zip(*crates[::-1])))]

moves = [re.findall(r'\d{1,2}', r) for r in rows[10::]]
moves = [[int(m[0]), int(m[1])-1, int(m[2])-1] for m in moves]

def print_top_crates():
  print(''.join([c[-1] for c in crates]))

def move_crates(qnty, src, dest):
  for i in range(qnty):
    crates[dest].append(crates[src].pop())

for i,m in enumerate(moves):
  move_crates(m[0], m[1], m[2])

print_top_crates()
