#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

trees = [[c for c in r.strip("\n")] for r in advent_downloader(8)]
# trees = [[c for c in r.strip("\n")] for r in advent_opener('e.txt')]
visible_count = 0
for y in range(len(trees)):
  for x in range(len(trees[0])):
    dirs = [
      trees[y][:x],                   # Left
      trees[y][x+1:],                 # Right 
      [t[x] for t in trees[:y]],      # Top
      [t[x] for t in trees[y+1:]]     # Bottom
    ]
    hidden = True
    for i,d in enumerate(dirs):
      if len(d) == 0 or max(d) < trees[y][x]:
        hidden = False
        break
    if not hidden:
      visible_count += 1
print(visible_count)
    


