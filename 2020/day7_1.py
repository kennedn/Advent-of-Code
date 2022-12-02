#!/usr/bin/env python3

def recurse_bags(bags_dict, bag_name):
    bag = bags_dict.get(bag_name, False)
    if not bag:
        return 0
    if bag.get('shiny gold', False):
        return 1
    for k, v in bag.items():
        if recurse_bags(bags_dict, k):
            return 1
    return 0

line = ' '
bags = {}
with open('day7.txt') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        top_bag = " ".join(line.split()[:2])
        bags[top_bag] = {}
        for item in " ".join(line.replace('.', '').split()[4:]).split(", "):
            item = item.split()
            count = item[0]
            bag = " ".join(item[1:3])
            if bag == 'other bags':
                continue
            bags[top_bag][bag] = count
count = 0
for k, v in bags.items():
    count += recurse_bags(bags, k)
print(count)