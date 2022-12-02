#!/usr/bin/env python3
from math import floor

def binary_search(lower_val, upper_val, lower_char, upper_char, line):
    if lower_val == upper_val:
        return lower_val

    middle = floor((lower_val + upper_val) / 2)

    if line[0] == lower_char:
        return binary_search(lower_val, middle, lower_char, upper_char, line[1:])
    elif line[0] == upper_char:
        return binary_search(middle + 1, upper_val, lower_char, upper_char, line[1:])

boarding_passes = []
with open('day5.txt') as f:
    line = ' '
    while True: 
        line = f.readline().replace('\n', '')
        if line == '':
            break

        temp_pass = {}
        temp_pass['row'] = binary_search(0, 127, 'F', 'B', line[:-3])
        temp_pass['column'] = binary_search(0, 7, 'L', 'R', line[-3:])
        temp_pass['sid'] = temp_pass['row'] * 8 + temp_pass['column']
        boarding_passes.append(temp_pass)

sids = [p['sid'] for p in boarding_passes]
sids.sort()
i = sids[0]
for s in sids:
    if i != s:
        print(s-1)
        break
    i += 1


