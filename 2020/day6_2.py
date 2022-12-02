#!/usr/bin/env python3
groups = []
line = ' '
with open('day6_1.txt') as file:
    while line != '':
        answers = {}
        group_count = 0
        while True:
            line = file.readline()
            if line == '\n' or line == '':
                break
            line = line.replace('\n', '')
            if len(line) > 1:
                for l in line:
                    answers[l] = answers.get(l, 0) + 1
            else:
                answers[line] = answers.get(line, 0) + 1
            group_count += 1
        scrubbed_answers = []
        for k, v in answers.items():
            if v == group_count:
                scrubbed_answers.append(k)
        groups.append(scrubbed_answers)

print(sum(len(a) for a in groups))