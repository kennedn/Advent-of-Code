#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

# nums = list(map(int, advent_opener('day_9_example.txt')))
# preamble_size = 5

nums = list(map(int, advent_downloader(9, 2020)))
preamble_size = 25


def preamble_contains_sum(preamble, target):
    sums = set([i+j for j in preamble[1:] for i in preamble])
    return target in sums

def sum_in_sublist(list, target):
    for i in range(len(list)):
        for j in range(i+2, len(list)-1):
            sub_list = list[i:j]
            list_sum = sum(sub_list)
            if list_sum > target:
                break
            if target == list_sum:
                return min(sub_list) + max(sub_list)

for i, n in enumerate(nums[preamble_size:]):
    if not preamble_contains_sum(nums[i:i+preamble_size], n):
        break

print(n)
print(sum_in_sublist(nums, n))


