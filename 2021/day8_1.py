#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

# raw = advent_opener("day_8_example.txt")
raw = advent_downloader(8)
segments = [l.split('|') for l in raw]
for i, seg in enumerate(segments):
    for j, s in enumerate(seg):
        segments[i][j] = s.replace("|", "").replace("\n", "").strip().split(" ")

unique_segments = 0
for seg in segments:
    for digit in seg[1]:
        digit_length = len(digit)
        if digit_length in [2, 4, 3, 7]:
            unique_segments += 1

print(unique_segments)
