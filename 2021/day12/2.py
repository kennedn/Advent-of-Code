#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

rows = [r.strip().split("-") for r in advent_downloader(12)]
# rows = [r.strip().split("-") for r in advent_opener('day_12_example.txt')]
nodes = {}

for r in rows:
    nodes.setdefault(r[0], set()).add(r[1])
    nodes.setdefault(r[1], set()).add(r[0])

def branch_on_node(key, paths, previous_nodes=None, small_visited=False):
    previous_nodes = previous_nodes[:] if previous_nodes is not None else [] # create local copy of list

    if re.match(r'^[a-z]+$', key) and key in previous_nodes:
        if small_visited:
            return
        small_visited = True

    previous_nodes.append(key)

    if key == 'end':
        paths.append(previous_nodes)
        return

    for next_node in nodes[key]:
        if next_node == 'start': continue
        branch_on_node(next_node, paths, previous_nodes, small_visited)

paths = []
branch_on_node('start', paths)
print(len(paths))