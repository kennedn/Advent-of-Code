#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

rows = [re.match(r'^([LRUD]) (\d+)$',r.strip("\n")) for r in advent_downloader(9)]
# rows = [re.match(r'^([LRUD]) (\d+)$',r.strip("\n")) for r in advent_opener('e.txt')]
# rows = [re.match(r'^([LRUD]) (\d+)$',r.strip("\n")) for r in advent_opener('e2.txt')]
   
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

knots = [[0,0] for i in range(10)]
tail_visits = set()
tail_visits.add((0,0))
for d in enumerate(deltas):
  for i in range(len(knots)):
    if i == 0:
      knots[i] = [knots[i][0] + d[0], knots[i][1] + d[1]]
      continue
    if abs(knots[i-1][0] - knots[i][0]) <= 1 and abs(knots[i-1][1] - knots[i][1]) <= 1 :
      continue
    new_delta = [
      1 if knots[i-1][0] > knots[i][0] else 0 if knots[i-1][0] == knots[i][0] else -1, 
      1 if knots[i-1][1] > knots[i][1] else 0 if knots[i-1][1] == knots[i][1] else -1
    ]
    knots[i] = [knots[i][0] + new_delta[0], knots[i][1] + new_delta[1]]
  tail_visits.add(tuple(knots[-1]))
  print(d, knots)

print(len(tail_visits))