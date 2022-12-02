#!/usr/bin/env python3

def count_bags(bags_dict, bag, count=0, multiplier=1):
    count += sum(bag.values()) * multiplier
    for k, v in bag.items():
        count = count_bags(bags_dict, bags_dict[k], count, multiplier * v)
    return count

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
            bag = " ".join(item[1:3])
            if bag == 'other bags':
                continue
            count = int(item[0])
            bags[top_bag][bag] = count


print(count_bags(bags, bags['shiny gold']))