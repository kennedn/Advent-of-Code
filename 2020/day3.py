#!/usr/bin/env python3
trees = 0
# corrects = ['#', '#', '#', '#', '#', '.', '#', '.', '#', '#', 
#             '#', '#', '#', '.', '#', '.', '#', '#', '#', '#',
#             '#', '#', '#', '#',]
corrects = ['.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', ]
incorrects = []

slope_types = [[1,1], [3,1], [5,1], [7,1], [1,2]]
slope_results = []
# slope_types = [[1,2]]

with open("day3_line.txt") as f:
    for s in slope_types:
        print(s)
        trees = 0
        x = 0
        f.seek(0)
        line = f.readline()
        curr_line = 1
        i=0
        while True:
            x = (x + s[0]) % (len(line) -1)
            for idx in range(s[1]):
                line = f.readline()
                curr_line += 1

            if line == '':
                slope_results.append(trees)
                break

            c = line[x]
            if c == '#':
                trees += 1
            # incorrects.append(f"curr={curr_line}, x={x},c={c} line={line}")
            # if i < len(corrects) and c != corrects[i]:
            #     break;
            # if i == 20:
            #     break;
            i += 1
for j in incorrects:
    print(j)
product = 1
for item in slope_results:
    product = product * item
print(product)
