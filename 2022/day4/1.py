#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

rows = [r.strip("\n") for r in advent_downloader(4)]

ranges = []
for r in rows:
  r = re.findall(r'[\d]{1,2}', r)
  r = list(map(int, r))
  ranges.append([set(range(r[0],r[1]+1)),set(range(r[2],r[3]+1))])

contained = [True for r in ranges if r[0] >= r[1] or r[0] <= r[1]]
print(len(contained))
