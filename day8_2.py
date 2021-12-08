#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
import itertools as it

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
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

def get_unique_lengths(length_map):
    len_list = list(length_map.values())
    return [l for l in len_list if len_list.count(l) == 1]

def reverse_digit_map(digit_map):
    return [c for c in 'abcdefg' if c not in digit_map]

def derive_numbers(wire_map, scrambled_numbers):
    keys = list(wire_map.keys())
    values = list(wire_map.values())
    # Get all possible permutations of map from partially resolved wire_map
    permutations = [dict(zip(keys, v)) for v in it.product(*values)]
    # invert maps so they now become lookup tables for scrambled numbers
    permutations = [{v:k for k,v in dict.items()} for dict in permutations]
    # Filter out duds (those that had duplicate values before inversion) 
    permutations = [dict for dict in permutations if len(dict.keys()) == 7]
    for lookup_table in permutations:
        decoded_numbers = []
        for num in scrambled_numbers:
            decoded_number = ''.join(sorted([lookup_table[c] for c in num]))
            if decoded_number in digits:
                decoded_numbers.append(digits[decoded_number])
                continue
        if len(decoded_numbers) == 4:
            return int(''.join([str(n) for n in decoded_numbers]))
    raise Exception("Something went wrong")

# raw = advent_opener("day_8_example.txt")
# raw = advent_opener("day_8_example_short.txt")
raw = advent_downloader(8)
segment_list = [l.split('|') for l in raw]
for i, segments in enumerate(segment_list):
    for j, s in enumerate(segments):
        segment_list[i][j] = s.replace("\n", "").strip().split(" ")

unique_lengths = get_unique_lengths(length_map)
solve_sum = 0
for segments, output in segment_list:
    _wire_map = dict(wire_map)
    for digit in segments:
        digit_length = len(digit)
        # Use known digits (with unique length) to partially solve wire_map
        if digit_length in unique_lengths:
            unscrambled_digit_map = digits_invert[length_map_invert[digit_length]]
            # For each segment in unscrambled digit map, 
            # filter out segments that DO NOT occur in the scrambled digit
            for c in unscrambled_digit_map:
                _wire_map[c] = ''.join([s for s in _wire_map[c] if s in digit])

            # For each segment NOT in unscrambled digit map, 
            # filter out segments that DO occur in the scrambled digit 
            for c in reverse_digit_map(unscrambled_digit_map):
                _wire_map[c] = ''.join([s for s in _wire_map[c] if s not in digit])
    solve_sum += derive_numbers(_wire_map, output)
print(solve_sum)

