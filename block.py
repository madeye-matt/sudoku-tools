#!/usr/bin/python3.6
import sys

from functools import partial

from sudoku import load_puzzle, validate_puzzle, get_row, get_column,get_block,get_block_for_coord,get_used_numbers,get_free_numbers,iterate_puzzle,get_block_info

def print_free(p, info, row,col, val):
    if val == 0 and row >= info['start_row'] and row < info['end_row'] and col >= info['start_col'] and col < info['end_col']:
        print('({0},{1}) -> {2}'.format(col, row, get_free_numbers(p, row, col)))
        
puzzle_file = sys.argv[1]
target = int(sys.argv[2])
info = get_block_info(target)
p = load_puzzle(puzzle_file)
iterate_puzzle(p, partial(print_free, p, info))
