# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/12 Rain Risk.txt'

    pi = []
    file = open(fname, 'r', encoding='utf8')

    for line in file:
        line = line.rstrip('\n')
        
        dir = line[0:1]
        dist = int(line[1:])
        pi.append([dir, dist])
        
    return pi

# insts = read_puzzle_input(True)
insts = read_puzzle_input()

# for inst in insts:
#     print(inst)

def move_ferry(drct = 'E'):
    cmps = 'NESW' * 3

    coords = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    for inst in insts:
        if inst[0] in coords:
            coords[inst[0]] += inst[1]
        elif inst[0] == 'F':
            coords[drct] += inst[1]
        elif inst[0] == 'L':
            ind = cmps.index(drct, 4, 8) - inst[1] // 90
            drct = cmps[ind]
        elif inst[0] == 'R':
            ind = cmps.index(drct, 4, 8) + inst[1] // 90
            drct = cmps[ind]
    # print(coords)
    ns = coords['N'] - coords['S']
    we = coords['W'] - coords['E']
    print(abs(ns) + abs(we))

def move_ferry_wp(drct = 'E'):
    wp = {'V': 1, 'H': 10}
    ship = {'V': 0, 'H': 0}

    for inst in insts:
        if inst[0] == 'N':
            wp['V'] += inst[1]
        elif inst[0] == 'S':
            wp['V'] -= inst[1]
        elif inst[0] == 'E':
            wp['H'] += inst[1]
        elif inst[0] == 'W':
            wp['H'] -= inst[1]
        elif inst[0] in 'R':
            if inst[1] == 90:
                wp['V'], wp['H'] = -wp['H'], wp['V']
            if inst[1] == 180:
                wp['V'], wp['H'] = -wp['V'], -wp['H']
            if inst[1] == 270:
                wp['V'], wp['H'] = wp['H'], -wp['V']
        elif inst[0] in 'L':
            if inst[1] == 90:
                wp['V'], wp['H'] = wp['H'], -wp['V']
            if inst[1] == 180:
                wp['V'], wp['H'] = -wp['V'], -wp['H']
            if inst[1] == 270:
                wp['V'], wp['H'] = -wp['H'], wp['V']
        elif inst[0] == 'F':
            ship['V'] += inst[1] * wp['V']
            ship['H'] += inst[1] * wp['H']
    # print(wp)
    # print(ship)
    print(ship['V'] + ship['H'])

move_ferry()
move_ferry_wp()
