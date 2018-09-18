#!/usr/bin/python3.6
import sys

from functools import partial

from sudoku import load_puzzle, validate_puzzle, get_row, get_column,get_block,get_block_for_coord,get_used_numbers,get_free_numbers,iterate_puzzle

def print_free(p, row,col, val):
    if val == 0:
        print('({0},{1}) -> {2}'.format(col, row, get_free_numbers(p, row, col)))
    else:
        print('({0},{1}) -> {2}'.format(col, row, val))
        
puzzle_file = sys.argv[1]
p = load_puzzle(puzzle_file)
iterate_puzzle(p, partial(print_free, p))
