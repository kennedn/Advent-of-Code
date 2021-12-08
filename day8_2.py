#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
import itertools as it

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 3,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

digits_invert = {v: k for k, v in digits.items()}

length_map = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

length_map_invert = {v: k for k, v in length_map.items()}

wire_map = {
    'a': 'abcdefg',
    'b': 'abcdefg',
    'c': 'abcdefg',
    'd': 'abcdefg',
    'e': 'abcdefg',
    'f': 'abcdefg',
    'g': 'abcdefg'
}

def get_lengths(digit_array):
    return [length_map[digit] for digit in digit_array]

def reverse_digit_map(digit_map):
    return [c for c in 'abcdefg' if c not in digit_map]

def derive_numbers(wi_map, scrambled_numbers):
    keys, values = zip(*wi_map.items())
    permutations_dicts = [dict(zip(keys, v)) for v in it.product(*values)]
    for m in permutations_dicts:
        m_r = {v:k for k,v in m.items()}
        if len(m_r.keys()) < 7:
            continue
        ret_nums = []
        for num in scrambled_numbers:
            number = ''.join(sorted([m_r[c] for c in num]))
            if number in digits:
                ret_nums.append(digits[number])
                continue
        if len(ret_nums) == 4:
            return int(''.join([str(n) for n in ret_nums]))

# raw = advent_opener("day_8_example.txt")
# raw = advent_opener("day_8_example_short.txt")
raw = advent_downloader(8)
segments = [l.split('|') for l in raw]
for i, seg in enumerate(segments):
    for j, s in enumerate(seg):
        segments[i][j] = s.replace("|", "").replace("\n", "").strip().split(" ")

solve_sum = 0
for seg in segments:
    wmap = dict(wire_map)
    for digit in seg[0]:
        digit_length = len(digit)
        if digit_length in get_lengths([1, 4, 7, 8]):
            real_digit_map = digits_invert[length_map_invert[digit_length]]
            for c in real_digit_map:
                wmap[c] = ''.join([s for s in wmap[c] if s in digit])
            for c in reverse_digit_map(real_digit_map):
                wmap[c] = ''.join([s for s in wmap[c] if s not in digit])
    solve_sum += derive_numbers(wmap, seg[1])
print(solve_sum)
