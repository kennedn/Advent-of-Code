#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Direction:
    direction: str
    amount: int

directions = []
with open('day2.txt') as f:
    while True:
        l = f.readline()
        if l == '':
            break
        directions.append(Direction(l.split(" ")[0], int(l.split(" ")[1])))

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
