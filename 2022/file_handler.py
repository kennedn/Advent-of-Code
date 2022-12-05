#!/usr/bin/env python3
from variables import cookies
import requests
from io import StringIO
from os.path import isfile

def advent_opener(file_name):
    with open(file_name) as f:
        return f.readlines()

def advent_downloader(day, year=2022):
    txt_filename = f'day_{day}.txt'
    if isfile(txt_filename):
        return advent_opener(txt_filename)

    url = 'https://adventofcode.com/{}/day/{}/input'
    request = requests.get(url.format(year, day), cookies=cookies)
    if request.status_code != 200:
        raise Exception("Day not unlocked yet or network error, status: {}".format(request.status_code))

    lines = [] 
    with StringIO(request.text) as req_file, open(txt_filename, 'w') as txt_file:
        for line in req_file:
            lines.append(line)
            txt_file.write(line)
    return lines
