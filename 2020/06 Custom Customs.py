# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/06 Custom Customs.txt'
    pi = []
    file = open(fname, 'r', encoding='utf8')

    group = []
    for line in file:
        line = line.rstrip('\n')
        
        if line == '':
            pi.append(group)
            group = []
        else:
            group.append(line)

    if len(group) > 0:
        pi.append(group)

    return pi

def count_i(pi):
    cnt = 0

    for g in pi:
        ans = set()
        for el in g:
            for sym in el:
                ans.add(sym)
        cnt += len(ans)
    print(cnt)

def count_ii(pi):
    cnt = 0

    for group in pi:
        s = group[0]
        for answers in group:
            ns = ''
            for sym in answers:
                if sym in s:
                    ns += sym
            s = ns
        cnt += len(s)
    print(cnt)

# pi = read_puzzle_input(True)
pi = read_puzzle_input()
count_i(pi)
count_ii(pi)
