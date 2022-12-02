#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

# adapters = list(map(int, advent_opener('day10_example.txt')))
adapters = list(map(int, advent_downloader(10, 2020)))
adapters.insert(0, 0)
adapters = sorted(adapters)
adapters.append(max(adapters) + 3)

# def adapter_finder(adapters, current_jolts, max_difference=3):
#     return min([adapter - current_jolts for idx, adapter in enumerate(adapters) if adapter - current_jolts < max_difference])

one_difference = 0
three_difference = 0
while len(adapters) > 1:
    adapter_difference = adapters[1] - adapters[0]
    if adapter_difference == 3:
        three_difference += 1
    elif adapter_difference == 1:
        one_difference += 1
    else:
        raise Exception(f"difference is {adapter_difference} :(")
    print(f"{adapters[0]} -> ", end="")
    adapters.pop(0)
print(adapters[0])


print(one_difference*three_difference)