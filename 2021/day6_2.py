#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

# lanternfishs = [3,4,3,1,2]
lanternfishs = list(map(int, advent_downloader(6)[0].split(',')))
fish_dict = {}
for i in range(9):
    fish_dict[i] = len([f for f in lanternfishs if f == i])


for day in range(256):
    new_fishes = 0
    new_fish_dict = {}
    for key in reversed(sorted(fish_dict)):
        if key == 0:
            new_fish_dict[6] = fish_dict[key] + new_fish_dict.get(6, 0)
            new_fish_dict[8] = fish_dict[key] + new_fish_dict.get(8, 0)
        else:
            new_fish_dict[key - 1] = fish_dict[key]
    fish_dict = new_fish_dict

print(sum(fish_dict.values()))
