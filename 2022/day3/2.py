#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener


# for i,c in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#   print(f"'{c}': {i+1},")
priority_lookup = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5,
  'f': 6,
  'g': 7,
  'h': 8,
  'i': 9,
  'j': 10,
  'k': 11,
  'l': 12,
  'm': 13,
  'n': 14,
  'o': 15,
  'p': 16,
  'q': 17,
  'r': 18,
  's': 19,
  't': 20,
  'u': 21,
  'v': 22,
  'w': 23,
  'x': 24,
  'y': 25,
  'z': 26,
  'A': 27,
  'B': 28,
  'C': 29,
  'D': 30,
  'E': 31,
  'F': 32,
  'G': 33,
  'H': 34,
  'I': 35,
  'J': 36,
  'K': 37,
  'L': 38,
  'M': 39,
  'N': 40,
  'O': 41,
  'P': 42,
  'Q': 43,
  'R': 44,
  'S': 45,
  'T': 46,
  'U': 47,
  'V': 48,
  'W': 49,
  'X': 50,
  'Y': 51,
  'Z': 52,
}

rows = [r.strip("\n") for r in advent_downloader(3)]
groups = [[rows[i], rows[i+1], rows[i+2]] for i in range(0,len(rows),3)]
priority = 0
for g in groups:
  delta = [c for c in g[1] if c in g[0]]
  priority += priority_lookup[next(c for c in g[2] if c in delta)]

print(priority)