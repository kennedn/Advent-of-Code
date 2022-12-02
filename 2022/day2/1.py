#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener
rows = [r.strip("\n").split(" ") for r in advent_downloader(2)]
# rows = [r.strip("\n").split(" ") for r in advent_opener("day_2 example.txt")]

answers = []
for r in rows:
  x = r[0]
  if x == "A": x = 1   #  Rock
  if x == "B": x = 2   #  Paper
  if x == "C": x = 3   #  Scissors

  y = r[1]
  score = 0
  if y == "X":         #  Rock 
    if x == 1:
      score = 3 + 1
    elif x == 2:
      score = 0 + 1
    elif x == 3:
      score = 6 + 1
  elif y == "Y":         #  Paper
    if x == 1:
      score = 6 + 2
    elif x == 2:
      score = 3 + 2
    elif x == 3:
      score = 0 + 2
  elif y == "Z":         #  Scissors
    if x == 1:
      score = 0 + 3
    elif x == 2:
      score = 6 + 3
    elif x == 3:
      score = 3 + 3

  answers.append(score)

print(sum(answers))