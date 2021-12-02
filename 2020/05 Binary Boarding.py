# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/05 Binary Boarding.txt'

    puzzle_input = []

    file = open(fname, 'r', encoding='utf8')

    # pass_d = {}
    for line in file:
        line = line.rstrip('\n')

        puzzle_input.append(line)

    return puzzle_input

def bp_to_bin(b_pass):

    s = b_pass[0:7]
    s = s.replace('B', '1')
    s = s.replace('F', '0')
    
    c = b_pass[7:]
    c = c.replace('R', '1')
    c = c.replace('L', '0')

    return int(s, base=2), int(c, base=2)

def sanity_check(b_passes):
    max_id = 0
    bps = []
    for bp in b_passes:
        row, col = bp_to_bin(bp)
        id = row * 8 + col
        max_id = max(max_id, id)
        bps.append([row, col, id])
    print(max_id)
    return bps

def find_seat_id(passes):
    passes.sort(key=lambda id: id[2])
    for i in range(1, len(passes)):
        dlt = passes[i][2] - passes[i-1][2]
        if dlt == 2:
            print(passes[i][2]-1)

# passes = read_puzzle_input(True)
passes = read_puzzle_input()

bps = sanity_check(passes)
find_seat_id(bps)

