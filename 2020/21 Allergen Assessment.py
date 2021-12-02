# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = '21 test.txt'
    else:
        fname = '.data/21 Allergen Assessment.txt'

    file = open(fname, 'r', encoding='utf8')

    pi = []
    for line in file:
        line = line.rstrip('\n')
        l1, l2 = line.split(' (contains ')
        s1 = set(l1.split(' '))
        s2 = set(l2[:-1].split(', '))
        pi.append([s1, s2])

    return pi

def part_i():
    food = {}
    for elem in ingred_n_allergens:
        for allergen in elem[1]:
            # print(allergen)
            if allergen not in food:
                food[allergen] = elem[0].copy()
            else:
                food[allergen].intersection_update(elem[0])
    
    for i in range(100):
        for feed in food:
            if len(food[feed]) == 1:
                for feed_ii in food:
                    if len(food[feed_ii]) > 1:
                        food[feed_ii].difference_update(food[feed])

    ingred = set()
    for feed in food:
        ingred.update(food[feed])

    all_ingreds = set()
    for elem in ingred_n_allergens:
        all_ingreds.update(elem[0])

    diff = all_ingreds.difference(ingred)

    cnt = 0
    for elem in ingred_n_allergens:
        for d in diff:
            if d in elem[0]:
                cnt += 1
    print(cnt)

    food_ii = []
    for f in food:
        s = ''
        for el in food[f]:
            s += el
        food_ii.append([f, s])
    for f in sorted(food_ii):
        print(f'{f[1]},',end='')

ingred_n_allergens = read_puzzle_input()

part_i()
