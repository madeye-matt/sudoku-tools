
puzzle_size = 9

valid_values = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

def load_puzzle(filename):
    with open(filename, 'r') as myfile:
        return [[int(c) for c in line.strip()] for line in myfile]

def validate_puzzle_dimensions(p):
    if len(p) != puzzle_size:
        return False
    else:
        invalid = [row for row in p if len(row) != puzzle_size]

        return len(invalid) == 0

def validate_puzzle(p):
    return validate_puzzle_dimensions(p)

def get_row(p, row):
    if row >= 0 and row < puzzle_size:
        return p[row]
    else:
        raise ValueError('invalid row {0}'.format(row))

def get_column(p, col):
    if col >= 0 and col < puzzle_size:
        return [row[col] for row in p]
    else:
        raise ValueError('invalid col {0}'.format(col))

def get_block_info(b):
    if b >= 0 and b < puzzle_size:
        start_row = int(b / 3) * 3
        end_row = start_row + 3
        start_col = b % 3 * 3
        end_col = start_col + 3
        return {
            'start_row' : start_row,
            'end_row' : end_row,
            'start_col' : start_col,
            'end_col' : end_col
        }
    else:
        raise ValueError('invalid block {0}'.format(b))
    
def get_block(p, b):
    if b >= 0 and b < puzzle_size:
        start_row = int(b / 3) * 3
        end_row = start_row + 3
        start_col = b % 3 * 3
        end_col = start_col + 3
        return [[p[row][col] for col in range(start_col,end_col)] for row in range(start_row, end_row)]
    else:
        raise ValueError('invalid block {0}'.format(b))

def get_block_for_coord(row,col):
    br = int(row/3)
    bc = int(col/3)
    return br*3 + bc

def get_used_numbers(p,row,col):
    result = get_row(p,row) + get_column(p,col)
    block = get_block(p, get_block_for_coord(row,col))
    for ex in block:
        result = result + ex

    result = [stripped for stripped in result if stripped != 0]

    result.sort()

    return set(result)

def get_free_numbers(p,row,col):
    return valid_values - get_used_numbers(p,row,col)

def iterate_puzzle(p, fn):
    [[fn(row,col,p[row][col]) for col in range(0,puzzle_size)] for row in range(0, puzzle_size)]

def last(n):
    return n == puzzle_size - 1
