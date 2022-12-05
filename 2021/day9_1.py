#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
from dataclasses import dataclass, field
yellow = '\u001b[47;1m\u001b[30;1m'
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
            d['left'] = self.rows[self.y_pos][self.x_pos - 1]
        if (self.x_pos + 1 < len(rows[0])):
            d['right'] = self.rows[self.y_pos][self.x_pos + 1]
        if (self.y_pos - 1 >= 0):
            d['up'] = self.rows[self.y_pos - 1][self.x_pos]
        if (self.y_pos + 1 < len(rows)):
            d['down'] = self.rows[self.y_pos + 1][self.x_pos]
        self._neighbours = d
        return self._neighbours
    
    @property
    def is_lowest(self):
        return self.height < min(*self.neighbours.values())

    @property
    def risk_level(self):
        return self.height + 1

cave_points = []
risk_sum = 0
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        c = CavePoint(x, y, rows)
        cave_points.append(c)
        if c.is_lowest:
            print(f"{yellow}{c.height}{reset}", end="")
            risk_sum += c.risk_level
        else:
            print(f"{c.height}", end="")
    print()
        

print(risk_sum)