#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

moves = [re.match(r'(?P<op>\w+) ?(?P<x>[-]?\d+)?', r.strip("\n")) for r in advent_downloader(10)]
# moves = [re.match(r'(?P<op>\w+) ?(?P<x>[-]?\d+)?', r.strip("\n")) for r in advent_opener('e.txt')]

sum = 0
def important_tick(x_reg, tick):
  global sum
  for j in [20, 60, 100, 140, 180, 220]:
    if j == tick: 
      print(f"{tick=}, {x_reg=}, {x_reg * tick=}")
      sum += x_reg * tick

x_reg = 1
tick = 1
for m in moves:
  important_tick(x_reg, tick)

  tick += 1
  if m['op'] == 'noop':
    continue

  important_tick(x_reg, tick)

  tick +=1
  x = int(m['x'])
  # print(f"add {x=}, {x_reg=}, {x_reg + x=}")
  x_reg += x
print(sum)