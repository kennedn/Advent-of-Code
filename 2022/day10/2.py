#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

moves = [re.match(r'(?P<op>\w+) ?(?P<x>[-]?\d+)?', r.strip("\n")) for r in advent_downloader(10)]
# moves = [re.match(r'(?P<op>\w+) ?(?P<x>[-]?\d+)?', r.strip("\n")) for r in advent_opener('e.txt')]

# screen = [str(i % 10) for i in range(241)]
screen = ['.' for i in range(241)]
cycle = 0
def tick(x_reg):
  global cycle
  cycle += 1
  found = False
  for x in [x_reg - 1, x_reg, x_reg + 1]:
    if x != (cycle - 1) % 40: continue
    found = True
    
  if found:
    print('#', end="")
  else:
    print(' ', end="")
  if cycle % 40 == 0:
    print()


x_reg = 1
for m in moves:
  tick(x_reg)

  if m['op'] == 'noop':
    continue

  tick(x_reg)

  x = int(m['x'])
  x_reg += x