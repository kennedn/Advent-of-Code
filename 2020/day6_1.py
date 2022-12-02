#!/usr/bin/env python3
groups = []
line = ' '
with open('day6_1.txt') as file:
    while line != '':
        answers = []
        while True:
            line = file.readline()
            if line == '\n' or line == '':
                break
            line = line.replace('\n', '')
            if len(line) > 1:
                for l in line:
                    answers.append(l)
            else:
                answers.append(line)
        groups.append(answers)

print(sum(len(set(a)) for a in groups))