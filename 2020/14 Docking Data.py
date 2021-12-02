# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/14 Docking Data.txt'

    pi = []
    file = open(fname, 'r', encoding='utf8')

    d = {}
    for line in file:
        line = line.rstrip('\n')

        if line[0:4] == 'mask':
            if len(d) != 0:
                pi.append(d)
                d = {}
            d['mask'] = line[7:]
            d['mem'] = []
        elif line[0:3] == 'mem':
            k, v = line[4:].split('] = ')
            d['mem'].append([int(k), int(v)])

    pi.append(d)
        
    return pi

def part_i():
    res = {}
    for el in puin:
        mask_and = int(el['mask'].replace('X', '1'), base=2)
        mask_or = int(el['mask'].replace('X', '0'), base=2)
        for val in el['mem']:
            res[val[0]] = val[1] & mask_and | mask_or
    
    s = 0
    for r in res:
        s += res[r]
    print(s)

def get_all(x):
    flag = True
    masks = [x]
    while flag:
        flag = False
        n_masks = []
        for mask in masks:
            i = mask.find('X')
            if i != -1:
                flag = True
                n_masks.append(mask[0:i]+'1'+ mask[i+1:])
                n_masks.append(mask[0:i]+'0'+ mask[i+1:])
        if flag:
            masks = n_masks
    return masks

def part_ii():
    res = {}

    for el in puin:
        mask = el['mask']
        for val in el['mem']:
            b = '0'*36 + bin(val[0])[2:]
            b = b[-36:]
            s = ''
            for i in range(36):
                if mask[i] == '0':
                    s += b[i]
                elif mask[i] == '1':
                    s += '1'
                elif mask[i] == 'X':
                    s += 'X'

            mask_l = get_all(s)
            for ml in mask_l:
                res[int(ml, 2)] = val[1]
    
    s = 0
    for r in res:
        s += res[r]
    print(s)

# puin = read_puzzle_input(True)
puin = read_puzzle_input()


part_i()
part_ii()
