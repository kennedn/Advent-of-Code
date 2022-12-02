#!/usr/bin/env python3
from day3_2 import first_bit
from file_handler import advent_downloader, advent_opener

lines = advent_downloader(4)
# lines = advent_opener('day4_example.txt')

drawn_numbers = [int(l) for l in lines.pop(0).split(",")]
lines.pop(0)
boards = []
board = []
while True:
    line = lines.pop(0)
    if line == '\n' or len(lines) == 0:
        boards.append(board)
        board = []
        if len(lines) == 0: break
        continue
    board.append([int(l) for l in list(filter(None, line.strip().split(" ")))])

# Append a list of columns to each board by zipping the rows
for i,rows in enumerate(boards):
    for z in zip(*rows):
        boards[i].append(list(z))

def first_board():
    winner = None
    last_num = None
    for num in drawn_numbers:
        for i, board in enumerate(boards):
            for j, num_list in enumerate(board):
                for k, val in enumerate(num_list):
                    if num == val:
                        last_num = num_list.pop(k)
                        if len(num_list) == 0:
                            winner = True
            if winner != None:
                return last_num, boards[i]

last_num, winner = first_board()
winner_sum = int(sum([item for sub in winner for item in sub]) / 2)
print(f"{last_num * winner_sum = }")


