# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/16 Ticket Translation.txt'

    file = open(fname, 'r', encoding='utf8')

    flag = 1
    fields = {}
    ticket = []
    nearby = []

    for line in file:
        line = line.rstrip('\n')

        if line == '': 
            flag += 1
            continue

        if flag == 1:
            k, vals = line.split(': ')
            r1, r2 = vals.split(' or ')
            r1b, r1e = r1.split('-')
            r2b, r2e = r2.split('-')
            l = []
            for i in range(int(r1b), int(r1e)+1): 
                l.append(i)
            for i in range(int(r2b), int(r2e)+1): 
                l.append(i)
            fields[k] = l
        elif flag ==2:
            if line != 'your ticket:':
                ts = line.split(',')
                for t in ts: 
                    ticket.append(int(t))
        elif flag ==3:
            if line != 'nearby tickets:':
                nt = []
                ts = line.split(',')
                for t in ts: 
                    nt.append(int(t))
                nearby.append(nt)

    return fields, ticket, nearby

def part_i():
    wrong = []
    non_valid = 0
    vl_s = set()
    for vl in fields.values():
        vl_s.update(set(vl))

    for nts in nearby:
        for nt in nts:
            if nt not in vl_s:
                non_valid += nt
                if nts not in wrong:
                    wrong.append(nts)

    for w in wrong:
        nearby.remove(w)
    print(non_valid)

def part_ii():
    res = []
    fs = set(fields.keys())
    for i in range(len(fields)):
        res.append(fs.copy())

    for nt in nearby:
        for i in range(len(nt)):
            for f in fields:
                if nt[i] not in fields[f]:
                    res[i].remove(f)

    while True:
        one_s = []
        mul_s = []
        for r in res:
            if len(r) == 1:
                one_s.append(r)
            else:
                mul_s.append(r)
        
        for ms in mul_s:
            for os in one_s:
                ms.difference_update(os)
        
        if len(mul_s) == 0:
            break

    m = 1
    for i in range(len(res)):
        for r in res[i]:
            if 'departure' in r:
                m *= ticket[i]
    print(m)
        
    return res

fields, ticket, nearby = read_puzzle_input()

part_i()
part_ii()