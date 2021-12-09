#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
from dataclasses import dataclass, field
import math

highlight = '\u001b[47;1m\u001b[30;1m'
reset = '\u001b[0m'
# rows = [list(map(int, r.replace("\n", ""))) for r in advent_opener('day_9_example.txt')]
rows = [list(map(int, r.replace("\n", ""))) for r in advent_downloader(9)]

@dataclass
class CavePoint:
    x_pos: int
    y_pos: int
    rows: list
    _neighbours: dict = field(default=None)

    @property
    def height(self):
        return rows[self.y_pos][self.x_pos]

    @property
    def neighbours(self):
        if (self._neighbours is not None):
            return self._neighbours
        d = {}
        if (self.x_pos - 1 >= 0):
            d['left'] = CavePoint(self.x_pos - 1, self.y_pos, self.rows)
        if (self.x_pos + 1 < len(rows[0])):
            d['right'] = CavePoint(self.x_pos + 1, self.y_pos, self.rows)
        if (self.y_pos - 1 >= 0):
            d['up'] = CavePoint(self.x_pos, self.y_pos - 1, self.rows)
        if (self.y_pos + 1 < len(rows)):
            d['down'] = CavePoint(self.x_pos, self.y_pos + 1, self.rows)
        self._neighbours = d
        return self._neighbours
    
    @property
    def is_lowest(self):
        return self.height < min([v.height for v in self.neighbours.values()])

    @property
    def risk_level(self):
        return self.height + 1

    @property
    def basin_size(self):
        if not self.is_lowest:
            return 0
        return len(self._basin_size(self,count={}).keys())
    def _basin_size(self,cave_point, count={}):
        count[cave_point.x_pos,cave_point.y_pos] = 1
        bigger_neighbours = [n for n in cave_point.neighbours.values() 
                             if n.height > cave_point.height and n.height < 9]
        for n in bigger_neighbours:
            count = self._basin_size(n, count)
        return count

basins = []
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        c = CavePoint(x, y, rows)
        if c.is_lowest:
            print(f"{highlight}{c.height}{reset}", end="")
            basins.append(c.basin_size)
        else:
            print(f"{c.height}", end="")
    print()
print(math.prod(sorted(basins)[-3:]))