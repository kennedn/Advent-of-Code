#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
from math import inf

# crabs = [16,1,2,0,4,2,7,1,2,14]
crabs = list(map(int, advent_downloader(7)[0].split(',')))

target_max = max(crabs)
min_fuel = inf
min_target = inf
for target in range(target_max + 1):
    fuel = sum([abs(target - c) for c in crabs])
    if fuel < min_fuel:
        min_fuel = fuel
        min_target = target

print(f"{min_fuel=}, {min_target=}")