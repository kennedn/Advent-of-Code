#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re

lines = [r.strip("\n") for r in advent_downloader(7)]
# lines = [r.strip("\n") for r in advent_opener('e.txt')]

path = []
storage = []

def process_line(line):
  global path
  cd = re.match(r'^\$ cd (.*)$', line)
  if cd:
    if cd[1] == '..':
      path.pop()
    elif cd[1] == '/':
      path = ['/']
    else:
      path.append(cd[1])
    return

  file = re.match('^(\d+) ([a-z\.]+)', line)
  if file:
    print(path, file[1], file[2])
    storage.append({
      'path': path[:],
      'size': int(file[1]),
      'name': file[2]
    })
    return

  folder = re.match('^dir ([a-z]+)', line)
  if folder:
    print(path,"dir", folder[1])
    storage.append({
      'path': path[:],
      'size': -1,
      'name': folder[1]
    })

def folder_size(base):
  global storage
  size = 0
  for item in [s for s in storage if s['path'][:len(base)] == base]: 
    if item['size'] == -1: continue
    size += item['size']
  return size

for l in lines:
  process_line(l)

limit = 100000
count = 0
for folder in [s.split(".") for s in list(set([".".join(s['path']) for s in storage]))]:
  size = folder_size(folder)
  if size <= limit:
    count += size
print(count)