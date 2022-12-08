#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

trees = [[c for c in r.strip("\n")] for r in advent_downloader(8)]
# trees = [[c for c in r.strip("\n")] for r in advent_opener('e.txt')]
scores = []
for y in range(len(trees)):
  for x in range(len(trees[0])):
    dirs = [
      trees[y][:x][::-1],             # Left
      trees[y][x+1:],                 # Right 
      [t[x] for t in trees[:y]][::-1],# Top
      [t[x] for t in trees[y+1:]]     # Bottom
    ]
    score = 0
    for i,d in enumerate(dirs):
      tree_count = 0
      while True:
        if len(d) == 0: break 
        tree_count += 1
        if d.pop(0) >= trees[y][x]: break
      score = tree_count if i == 0 else score * tree_count
    scores.append(score)
    
print(max(scores))
    


