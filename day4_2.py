#!/usr/bin/env python3
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


winner_board = None
winner_idxs = []
last_num = None
for num in drawn_numbers:
    for i, board in enumerate(boards):
        for j, num_list in enumerate(board):
            for k, val in enumerate(num_list):
                if num == val:
                    last_num = num_list.pop(k)
                    if len(num_list) == 0:
                        winner_idxs.append(i)

    if len(winner_idxs) > 0:
        # Construct new board array, removing previous winners for next number draw
        temp_boards = boards
        boards = []
        for i, board in enumerate(temp_boards):
            if i not in winner_idxs:
                boards.append(board)
        # Store last winner from current number draw
        winner_board = temp_boards[winner_idxs[-1]]
        winner_idxs = []

# Flatten remaining numbers and sum them. Divide by 2 because both rows and columns are present
winner_sum = int(sum([num for row in winner_board for num in row]) / 2)
print(f"{last_num} * {winner_sum} = {last_num*winner_sum}")