#!/usr/bin/env python3
nums = []
with open('day1_1.txt') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        nums.append(int(line))

count = 0    
for i in range(len(nums) - 3):
    a = sum(nums[i:i+3])
    b = sum(nums[i+1:i+3+1])
    if b > a:
        count += 1
print(count)
    