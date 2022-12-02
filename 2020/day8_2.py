#!/usr/bin/env python3
from dataclasses import dataclass
from random import choice

@dataclass
class Op:
    instruction: str
    variable: int
    ran_prior: bool

def toggle_op(op):
    if op.instruction == 'nop':
        op.instruction = 'jmp'
    elif op.instruction == 'jmp':
        op.instruction = 'nop'

instructions = []
with open('day8.txt') as f:
    while True:
        l = f.readline()
        if l == '':
            break
        instructions.append(Op(l.split(" ")[0], int(l.split(" ")[1]), False))

modifiable_instructions =  [i for i, v in enumerate(instructions) if v.instruction != 'acc']

while True:
    candidate_index = choice(modifiable_instructions)
    toggle_op(instructions[candidate_index])
    print(f"Trying candidate {candidate_index}")
    acc = 0
    ptr = 0
    upper = 50000
    loops = True
    while True:
        if ptr >= len(instructions):
            print("Hit end of instructions")
            loops = False
            break

        op = instructions[ptr]
        if upper <= 0:
            break
        upper -= 1

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
    else:
        toggle_op(instructions[candidate_index])