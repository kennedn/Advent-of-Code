#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

moves = [re.match(r'(?P<op>\w+) ?(?P<x>[-]?\d+)?', r.strip("\n")) for r in advent_downloader(10)]
# moves = [re.match(r'(?P<op>\w+) ?(?P<x>[-]?\d+)?', r.strip("\n")) for r in advent_opener('e.txt')]

cycle = 0
def tick(x_reg):
  global cycle
  if x_reg - 1 <= cycle % 40 <= x_reg + 1: 
    print('#', end="")
  else:
    print(' ', end="")
  
  cycle += 1

  if cycle % 40 == 0:
    print()

x_reg = 1
for m in moves:
  tick(x_reg)

  if m['op']  == 'noop':
    continue

  tick(x_reg)

  x = int(m['x'])
  x_reg += x