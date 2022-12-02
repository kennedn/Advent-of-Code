#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader
rows = [r.strip("\n") for r in advent_downloader(1)]

max_cals=0
curr_cals=0
for r in rows:
  if r == "":
    if curr_cals > max_cals:
      max_cals = curr_cals
    curr_cals = 0
    continue
  curr_cals += int(r)
print(max_cals)
  
  