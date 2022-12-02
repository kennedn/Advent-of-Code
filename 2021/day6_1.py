#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

# lanternfishs = [3,4,3,1,2]
lanternfishs = list(map(int, advent_downloader(6)[0].split(',')))

new_fishes = 0
for day in range(80):
    new_fishes = 0
    for i, fish in enumerate(lanternfishs):
        lanternfishs[i] -= 1
        if lanternfishs[i] < 0:
            lanternfishs[i] = 6
            new_fishes += 1
    for i in range(new_fishes):
        lanternfishs.append(8)

print(lanternfishs)
print(f'{len(lanternfishs) = }')