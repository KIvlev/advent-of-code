# -*- coding: UTF8 -*-
def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '08 Handheld Halting.txt'

    pi = []
    file = open(fname, 'r', encoding='utf8')

    for line in file:
        line = line.rstrip('\n')
        key, value = line.split(' ')
        pi.append([key, int(value), 0])

    return pi

def copy_list(pi):
    r = []
    for p in pi:
        r.append(p.copy())
    return r

def first_loop(pi):
    op = 0
    acc = 0
    while True:
        if op >= len(pi):
            break

        if pi[op][2] == 1:
            break
        pi[op][2] += 1
        if pi[op][0] == 'nop':
            op += 1
        elif pi[op][0] == 'acc':
            acc += pi[op][1]
            op += 1
        elif pi[op][0] == 'jmp':
            op += pi[op][1]

    return op, acc

def change_op():
    for i in range(len(puin)):
        pic = copy_list(puin)
        if pic[i][0] == 'jmp':
            pic[i][0] = 'nop'
        elif pic[i][0] == 'nop':
            pic[i][0] = 'jmp'

        op, acc = first_loop(pic)
        if op == len(puin):
            print(op, acc)

puin = read_puzzle_input()

op, acc = first_loop(copy_list(puin))
print(op, acc)
change_op()