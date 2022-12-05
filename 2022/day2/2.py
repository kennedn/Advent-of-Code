#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener
rows = [r.strip("\n").split(" ") for r in advent_downloader(2)]

answers = []
for r in rows:
  x = r[0]
  if x == "A": x = 0   #  Rock
  if x == "B": x = 1   #  Paper
  if x == "C": x = 2   #  Scissors

  y = r[1]
  score = 0
  if y == "X":         #  Lose
    score = ((x + 2) % 3 + 1) + 0
  elif y == "Y":         #  Draw
    score = (x + 1) + 3
  elif y == "Z":         #  Win
    score = ((x + 1) % 3 + 1) + 6

  answers.append(score)

print(sum(answers))