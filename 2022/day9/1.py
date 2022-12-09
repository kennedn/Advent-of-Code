#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

# rows = [re.match(r'^([LRUD]) (\d+)$',r.strip("\n")) for r in advent_downloader(9)]
rows = [re.match(r'^([LRUD]) (\d+)$',r.strip("\n")) for r in advent_opener('e.txt')]
   
moves = [[m[1],int(m[2])] for m in rows]

deltas = []

for m in moves:
  if m[0] == 'L':
    for i in range(m[1]): deltas.append([-1, 0, 'L'])
  elif m[0] == 'R':
    for i in range(m[1]): deltas.append([1, 0, 'R'])
  elif m[0] == 'U':
    for i in range(m[1]): deltas.append([0, 1, 'U'])
  elif m[0] == 'D':
    for i in range(m[1]): deltas.append([0, -1, 'D'])

head = [0,0]
tail = [0,0]
tail_visits = set(tuple([0,0]))
for d in deltas:
  head = [head[0] + d[0], head[1] + d[1]]
  if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1 :
    tail = [head[0] + (d[0]*-1), head[1] + (d[1]*-1)]
    tail_visits.add(tuple(tail))
  print(d[2], head, tail)

print(len(tail_visits))