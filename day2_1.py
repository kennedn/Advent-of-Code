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
y_axis = 0
for val in directions:
    if val.direction == 'forward':
        x_axis += val.amount
    elif val.direction == 'down':
        y_axis += val.amount
    elif val.direction == 'up':
        y_axis -= val.amount
print(f"{x_axis} * {y_axis} = {x_axis*y_axis}")
