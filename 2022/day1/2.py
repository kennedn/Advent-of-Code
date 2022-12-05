#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader
rows = [r.strip("\n") for r in advent_downloader(1)]

curr_cals = 0
calories = []
for r in rows:
  if r == "":
    calories.append(curr_cals)
    curr_cals = 0
    continue
  curr_cals += int(r)

print(sum(sorted(calories)[-3::]))
  
  
  
