#!/usr/bin/env python3
nums = []
with open('day1_1.txt') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        nums.append(int(line))

count = 0    
for i in range(len(nums) - 1):
    if nums[i+1] > nums[i]:
        count += 1
print(count)
    