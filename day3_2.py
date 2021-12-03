#!/usr/bin/env python3
from file_handler import advent_opener

lines = advent_opener('day3.txt')

length = len(lines[0]) - 1
vals = [int(b, 2) for b in lines]
epsilon_vals = vals.copy()
gamma_vals = vals.copy()
gamma = 0
epsilon = 0
for shift in range(length - 1, -1, -1):
    one_bits = [v for v in gamma_vals if (v >> shift) & 0x01 == 1]
    zero_bits = [v for v in gamma_vals if (v >> shift) & 0x01 == 0]
    most_common = None
    if len(one_bits) >= len(zero_bits):
        most_common = 1
    else:
        most_common = 0
    gamma_vals = [v for i, v in enumerate(gamma_vals) if (v >> shift) & 0x01 == most_common]
    if(len(gamma_vals) == 1):
        gamma = gamma_vals[0]
        break

print(gamma)
for shift in range(length - 1, -1, -1):
    one_bits = [v for v in epsilon_vals if (v >> shift) & 0x01 == 1]
    zero_bits = [v for v in epsilon_vals if (v >> shift) & 0x01 == 0]
    most_common = None
    if len(one_bits) >= len(zero_bits):
        most_common = 1
    else:
        most_common = 0
    epsilon_vals = [v for i, v in enumerate(epsilon_vals) if (v >> shift) & 0x01 != most_common]
    if(len(epsilon_vals) == 1):
        epsilon = epsilon_vals[0]
        break

print(epsilon*gamma)