#!/usr/bin/python3.6
import sys

from functools import partial

from sudoku import load_puzzle, validate_puzzle, get_row, get_column,get_block,get_block_for_coord,get_used_numbers,get_free_numbers,iterate_puzzle,last

def print_number(p, desired, row, col, val):
    free = get_free_numbers(p, row, col)
    if col == 0:
        print(row, end='')
    if last(col):
        end = '{0}\n'.format(row)
    else:
        end = ''
    if val == 0 and desired in free:
        print('X ', end=end)
    else:
        print('  ', end=end)

    if col % 3 == 2 and not(last(col)):
        print("|",end='')
    if row % 3 == 2 and last(col):
        print("--------------------")
        
puzzle_file = sys.argv[1]
p = load_puzzle(puzzle_file)
print(" 0 1 2 3 4 5 6 7 8")
iterate_puzzle(p, partial(print_number, p, int(sys.argv[2])))
print(" 0 1 2 3 4 5 6 7 8")
