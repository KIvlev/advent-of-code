# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/09 Encoding Error.txt'

    pi = []
    file = open(fname, 'r', encoding='utf8')

    for line in file:
        line = line.rstrip('\n')
        pi.append(int(line))

    return pi

# puin = read_puzzle_input(True)
# length = 5
puin = read_puzzle_input()
length = 25

def check_current(rec_num):
    for i in range(rec_num - length, rec_num):
        for j in range(i + 1, rec_num):
            if puin[i] + puin[j] == puin[rec_num]:
                return True
    return False

def find_weak():
    for i in range(length, len(puin)):
        if not check_current(i):
            return puin[i]
    return 0

def find_set(fig):
    for i in range(len(puin)):
        sum = 0
        seq = []
        for j in range(i, len(puin)):
            sum += puin[j]
            seq.append(puin[j])
            if sum == fig:
                return min(seq) + max(seq)

weak = find_weak()
print(weak)
print(find_set(weak))