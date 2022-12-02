#!/usr/bin/env python3
import re

passports = []
with open("day4.txt") as f:
    line = ' '
    while line != '':
        temp_dict = {}
        while True:
            line = f.readline()
            if line == '' or line == "\n":
                break
            line = line.split(':')
            temp_dict[line[0]] = line[1].replace('\n', '')
        passports.append(temp_dict)

valid_passports = 0
for passport in passports:
    flags = 0
    if all(key in passport for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        if (len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
            flags += 1
        
        if (len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
            flags += 1

        if (len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
            flags += 1

        height = int(passport['hgt'][:-2]) if passport['hgt'][:-2].isnumeric() else 0
        metric = passport['hgt'][-2:] == 'cm'
        if(metric and height >= 150 and height <= 193) or (not metric and height >= 59 and height <= 76):
            flags += 1

        color_regex = re.compile('^#[a-f0-9]{6}$')
        if color_regex.match(passport['hcl']):
            flags += 1

        if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            flags += 1

        if len(passport['pid']) == 9 and passport['pid'].isnumeric():
            flags += 1

        if flags == 7:
            valid_passports += 1
print(valid_passports)
