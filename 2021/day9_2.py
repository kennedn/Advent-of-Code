#!/usr/bin/env python3
from file_handler import advent_downloader, advent_opener
from PIL import Image, ImageShow
import tempfile
import os
from subprocess import call
from dataclasses import dataclass, field
import math

yellow = '\u001b[47;1m\u001b[30;1m'
red = '\u001b[41;1m'
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
        return len(self._basin_set(self))

    def _basin_set(self,cave_point, points=None):
        if points is None: 
            points = set()
        points.add((cave_point.x_pos, cave_point.y_pos))
        bigger_neighbours = [n for n in cave_point.neighbours.values() 
                             if cave_point.height < n.height < 9]
        for n in bigger_neighbours:
            points = self._basin_set(n, points)
        return points

def lerp_color(color1, color2, scaler):
    color = []
    for c1, c2 in zip(color1, color2):
        color.append(int((c1 - c2) * scaler + c2))
    return color

deep = [50, 0, 0]
shallow = [0, 0, 255]
def cave_to_png(rows):
    rgb_pixels = []
    width = len(rows[0])
    height = len(rows)
    for y, row in enumerate(rows):
        for x, val in enumerate(row):
            rgb_pixels.extend(lerp_color(shallow, deep, val/9))

    img = Image.frombytes('RGB', (width, height), bytes(rgb_pixels))
    img = img.resize((width * 4,height * 4))
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, "w") as f:
        f.write(ImageShow._viewers[0].save_image(img))
    with open(path) as f:
        call("im=$(cat); eog $im; rm -f $im", shell=True, stdin=f)
    os.remove(path)



basins = []
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        c = CavePoint(x, y, rows)
        if c.is_lowest:
            basins.append(c.basin_size)

top_three = sorted(basins)[-3:]
top_three_str = ' * '.join(map(str, top_three))
print(f"{top_three_str} = {math.prod(top_three)}")
cave_to_png(rows)