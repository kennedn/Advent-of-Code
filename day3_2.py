#!/usr/bin/env python3
from file_handler import advent_opener

lines = advent_opener('day3.txt')

length = len(lines[0]) - 1
vals = [int(b, 2) for b in lines]

def first_bit(val, shift):
    return (val >> shift) & 0x01

def eliminator(array, bit_length, one_most_common):
    elim_vals = array
    for shift in reversed(range(bit_length)):
        one_bits = [v for v in elim_vals if first_bit(v, shift) == 1]
        zero_bits = [v for v in elim_vals if first_bit(v, shift) == 0]
        most_common = None
        if len(one_bits) >= len(zero_bits):
            most_common = 1 if one_most_common else 0
        else:
            most_common = 0 if one_most_common else 1
        elim_vals = [v for v in elim_vals if first_bit(v, shift) != most_common]
        if(len(elim_vals) == 1):
            return elim_vals[0]

gamma = eliminator(vals, length, True)
epsilon = eliminator(vals, length, False)
print(epsilon*gamma)