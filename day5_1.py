#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener

# lines = advent_opener('day_5_example.txt')
lines = advent_downloader(5)


lines = [list(map(int, l.replace(' -> ', ',').split(','))) for l in lines]
lines = [[l[0:2],l[2:4]] for l in lines]

# Only consider horizontal or vertical lines for now
lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]


def line_to_points(line):
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]

    if x1 == x2 and y1 == y2:
        return [line[0,0]]
    elif x1 == x2:
        lower, upper = (y1,y2) if y1 < y2 else (y2,y1)
        return [[x1, point] for point in range(lower, upper + 1)]
    elif y1 == y2:
        lower, upper = (x1,x2) if x1 < x2 else (x2,x1)
        return [[point, y1] for point in range(lower, upper + 1)]


   

points_dict = {}

for l in lines:
    points = line_to_points(l)
    for p in points:
        points_dict[str(p)] = points_dict.get(str(p), 0) + 1

intersecting_points = [key for key, item in points_dict.items() if item > 1]
print(intersecting_points)
print(f"{len(intersecting_points) = }")