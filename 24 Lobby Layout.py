# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = '24 test.txt'
    else:
        fname = '24 Lobby Layout.txt'

    file = open(fname, 'r', encoding='utf8')

    pi = []
    for line in file:
        line = line.rstrip('\n')
        pi.append(line)
    return pi

def move(p, m):
    return tuple((p[0]+m[0], p[1]+m[1], p[2]+m[2]))

def decrypt_tiles():
    d2 = set(('se', 'sw', 'nw', 'ne'))
    d1 = set(('e', 'w'))
    rules = {
        'e' : [1, -1,  0],
        'w' : [-1, 1,  0],
        'ne': [1,  0, -1],
        'sw': [-1, 0,  1],
        'se': [0, -1,  1],
        'nw': [0,  1, -1]
        }

    # puin = read_puzzle_input(True)
    puin = read_puzzle_input()

    tiles = set()
    tile_ways = []
    for p in puin:
        tile_way = []
        tile = (0, 0, 0)
        while p != '':
            if p[:2] in d2:
                turn = p[:2]
                p = p[2:]
            elif p[:1] in d1:
                turn = p[:1]
                p = p[1:]
            else:
                print('ooops', p)
            tile_way.append(turn)
            tile = move(tile, rules[turn])
        tile_ways.append([tile_way])
        if tile not in tiles:
            tiles.add(tile)
        else:
            tiles.remove(tile)

    print('part I', len(tiles))

    for i in range(100):
        to_check = set()
        further = set()
        for tile in tiles:
            cnt = 0
            for dir in rules.keys():
                neigh = move(tile, rules[dir])
                if neigh in tiles:
                    cnt += 1
                else:
                    to_check.add(neigh)
            if cnt in (1, 2):
                further.add(tile)

        for tile in to_check:
            cnt = 0
            for dir in rules.keys():
                neigh = move(tile, rules[dir])
                if neigh in tiles:
                    cnt += 1
            if cnt == 2:
                further.add(tile)

        tiles = further
    print('part II', len(tiles))

decrypt_tiles()
