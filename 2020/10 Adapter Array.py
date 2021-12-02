# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/10 Adapter Array.txt'

    pi = []
    file = open(fname, 'r', encoding='utf8')

    for line in file:
        line = line.rstrip('\n')
        pi.append(int(line))

    return sorted(pi)

def make_chain():
    diff1, diff3 = 1, 1
    for i in range (1, len(puin)):
        d = puin[i] - puin[i - 1]
        if d == 1:
            diff1 += 1
        elif d ==3:
            diff3 += 1
    joltage = max(puin) + 3

    # print(f'Joltage: {joltage} | d1:d3 {diff1}:{diff3} | answer is {diff1 * diff3}')
    print(diff1 * diff3)

def count_ways():
    ways = {0:1}
    for el in puin:
        ways[el] = 0
        if el - 1 in ways:
            ways[el] += ways[el-1]
        if el - 2 in ways:
            ways[el] += ways[el-2]
        if el - 3 in ways:
            ways[el] += ways[el-3]
        # print(ways)
    return(ways[max(puin)])

# puin = read_puzzle_input(True)
puin = read_puzzle_input()
make_chain()

# part 2
print(count_ways())
