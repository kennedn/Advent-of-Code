#!/usr/bin/env python3
from dataclasses import dataclass
from random import choice

@dataclass
class Op:
    instruction: str
    variable: int
    ran_prior: bool


instructions = []
with open('day8.txt') as f:
    while True:
        l = f.readline()
        if l == '':
            break
        instructions.append(Op(l.split(" ")[0], int(l.split(" ")[1]), False))

loops = True
modifiable_instructions =  [i for i, v in enumerate(instructions) if v.instruction != 'acc']
while loops:
    candidate_index = choice(modifiable_instructions)
    candidate_instructions = instructions
    if (candidate_instructions[candidate_index].instruction == 'nop'):
        candidate_instructions[candidate_index].instruction = 'jmp'
    elif (candidate_instructions[candidate_index].instruction == 'jmp'):
        candidate_instructions[candidate_index].instruction = 'nop'
    print(f"Trying candidate {candidate_index}")
    acc = 0
    ptr = 0
    while True:
        if ptr >= len(candidate_instructions):
            print("Hit end of instructions")
            loops = False
            break

        op = candidate_instructions[ptr]
        if op.ran_prior:
            print("Ran into a secondary instructions")
            break
        else:
            op.ran_prior = True

        if op.instruction == 'nop':
            ptr += 1
        elif op.instruction == 'acc':
            acc += op.variable
            ptr += 1
        elif op.instruction == 'jmp':
            ptr += op.variable

    if not loops:
        print(acc)
        break