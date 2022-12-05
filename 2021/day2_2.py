#!/usr/bin/env python3
from dataclasses import dataclass
from file_handler import advent_opener

@dataclass
class Direction:
    direction: str
    amount: int

lines = advent_opener('day2.txt')

directions = []
for line in lines:
    directions.append(Direction(line.split(" ")[0], int(line.split(" ")[1])))


x_axis = 0
aim = 0
depth = 0
for val in directions:
    if val.direction == 'forward':
        x_axis += val.amount
        depth += val.amount * aim
    elif val.direction == 'down':
        aim += val.amount
    elif val.direction == 'up':
        aim -= val.amount
print(f"{x_axis} * {depth} = {x_axis*depth}")
