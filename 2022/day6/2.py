#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re
import string

stream = [r.strip("\n") for r in advent_downloader(6)][0]
# stream='bvwbjplbgvbhsrlpgdmjqwftvncz'
# stream='nppdvjthqldpwncqszvftbrmjlhg'
# stream='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

processed = ""
for s in stream:
  processed += s
  if len(processed) < 14 : continue

  last_4 = set(processed[-14:])
  if len(last_4) == 14:
    break

print(len(processed))

# rows = [r.strip("\n") for r in advent_opener('day_5_example.txt')]
