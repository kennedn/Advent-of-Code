#!/usr/bin/env python3
import sys
sys.path.append("..") 
from file_handler import advent_downloader, advent_opener

import re
class Monkey:
    def __init__(self, vars):
        self.items = vars['items']
        self.operation = vars['operation']
        self.operand = vars['operand']
        self.divider = vars['divider']
        self.true = vars['true']
        self.false = vars['false']
        self.count = 0
        self.highest_common_divisor = vars['highest_common_divisor']

    def inspect(self, item):
        op = item if type(self.operand) == str else self.operand

        if self.operation == '+':
            item = (item + op)
        else:
            item = (item * op)

        item %= self.highest_common_divisor

        self.count += 1

        if item % self.divider  == 0:
            return {'monkey': self.true, 'item': item}
        else:
            return {'monkey': self.false, 'item': item}

    
    def inspect_all(self):
        out = []
        while len(self.items) > 0:
            out.append(self.inspect(self.items.pop(0)))
        return out

    def add_item(self, item):
        self.items.append(item)

class MonkeyTime:
    def __init__(self, monkeys):
        self.monkeys = monkeys
    
    def round(self):
        for m in self.monkeys:
            items = m.inspect_all()
            self.process_items(items)

    def count(self):
        counts = []
        for i, m in enumerate(self.monkeys):
            print(f"Monkey {i} inspected items {m.count} times")
            counts.append(m.count)
        counts = sorted(counts, reverse=True)
        return counts[0] * counts[1]

    def process_items(self, items):
        for item in items:
            self.monkeys[item['monkey']].add_item(item['item'])
            
# raw = re.split(r'Monkey \d+:\n',''.join(advent_opener('e.txt')))
raw = re.split(r'Monkey \d+:\n',''.join(advent_downloader(11)))
raw_regex = [re.match(r'^.*Starting items: (?P<items>[\d+, ]+).*Operation: new = old (?P<op>[+*]) (?P<val>\w+).*Test: divisible by (?P<test>\d+).*If true: throw to monkey (?P<true>\d+).*If false: throw to monkey (?P<false>\d+)', m.replace("\n", "")) for m in raw[1:]] 

monkey_vars = [{
    "items": [int(i) for i in m['items'].split(",")],
    "operation": m['op'],
    "operand": int(m['val']) if m['val'].isdigit() else m['val'],
    "divider": int(m['test']),
    "true": int(m['true']),
    "false": int(m['false'])
} for m in raw_regex]

highest_common_divisor = 1
for x in monkey_vars:
  highest_common_divisor *= x['divider']

for i in range(len(monkey_vars)):
  monkey_vars[i]['highest_common_divisor'] = highest_common_divisor

monkeys = []
for v in monkey_vars:
    monkeys.append(Monkey(v))

mt = MonkeyTime(monkeys)



for i in range(10000):
    mt.round()
    print(f"{i}: {mt.count()}")
print(mt.count())


