#!/usr/bin/env python3
import requests
from variables import cookies
import json
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='Show timestamps for star gets in AoC private leaderboards')
parser.add_argument('-l', '--leaderboard', nargs='?', const=1, type=str, default='10676', help='private leaderboard code')
args = parser.parse_args() 

j = requests.get(f'https://adventofcode.com/2022/leaderboard/private/view/{args.leaderboard}.json', cookies=cookies).json()

players = [j['members'][i] for i in j['members']]
players.sort(key=lambda p: p['local_score'])


for player in players:
  if player['stars'] != 0:
    print(f"{player.get('name')}:")
  for key, value in sorted(player['completion_day_level'].items()):
      print(f"  day {key}:")
      for key, value in sorted(value.items()):
        print(f"    star {key}: {datetime.fromtimestamp(value.get('get_star_ts'))}")

