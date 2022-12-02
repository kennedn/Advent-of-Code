#!/usr/bin/env python3
import requests
from variables import cookies
import json
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='Show timestamps for star gets in AoC private leaderboards')
parser.add_argument('-l', '--leaderboard', nargs='?', const=1, type=str, default='1505095', help='private leaderboard code')
args = parser.parse_args() 

j = requests.get(f'https://adventofcode.com/2021/leaderboard/private/view/{args.leaderboard}.json', cookies=cookies).json()

for member in j['members'].values():
  if member['stars'] != 0:
    print(f"{member.get('name')}:")
  for key, value in sorted(member['completion_day_level'].items()):
      print(f"  day {key}:")
      for key, value in sorted(value.items()):
        print(f"    star {key}: {datetime.fromtimestamp(value.get('get_star_ts'))}")

