# -*- coding: UTF8 -*-

def read_puzzle_input():
    pi = []
    file = open('.data/02 Password Philosophy.txt', 'r', encoding='utf8')
    for line in file:
        line = line.rstrip('\n')
        line, pwd = line.split(': ')
        line, sym = line.split(' ')
        s_from, s_to = line.split('-')

        pi.append([pwd, sym, int(s_from), int(s_to)])

    return pi

def count_valid_pwds(p_in):
    cntr = 0
    for p in p_in:
        cnt = p[0].count(p[1])
        if cnt in range(p[2], p[3]+1):
            cntr += 1
    print(cntr)

def count_valid_pwds_ii(p_in):
    cntr = 0
    for p in p_in:
        pwd = p[0]
        sym = p[1]
        p1 = p[2] - 1
        p2 = p[3] - 1

        if (pwd[p1] == sym) and (pwd[p2] != sym):
            cntr += 1

        if (pwd[p2] == sym) and (pwd[p1] != sym):
            cntr += 1

    print(cntr)

p_in = read_puzzle_input()
count_valid_pwds(p_in)
count_valid_pwds_ii(p_in)
