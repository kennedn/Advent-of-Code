#!/usr/bin/env python3
from file_handler import advent_opener

lines = advent_opener('day3.txt')
# lines = advent_opener('day3.txt')
length = len(lines[0]) - 1
vals = [int(b, 2) for b in lines]
gamma = 0

for shift in range(length):
    res = []
    for v in vals:
        res.append((v >> shift) & 0x01)
    gamma += (max(set(res), key=res.count) << (shift))

epsilon = gamma ^ 0xFFF
#epsilon = 0b11111 - gamma
print(f"{gamma:012b}:{gamma} * {epsilon:012b}:{epsilon} = {gamma*epsilon}")