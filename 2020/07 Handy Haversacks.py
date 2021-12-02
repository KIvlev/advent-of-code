# -*- coding: UTF8 -*-

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/07 Handy Haversacks.txt'

    pi = {}
    file = open(fname, 'r', encoding='utf8')

    for line in file:
        line = line.rstrip('\n')
        key, line = line.split(' bags contain ')
        line = line.replace(' bags.', '')
        line = line.replace(' bag.', '')
        line = line.replace(' bags', '')
        line = line.replace(' bag', '')
        line_l = line.split(', ')
        
        bags = {}
        for l in line_l:
            if l != 'no other':
                v, k = l.split(' ', 1)
                bags[k] = int(v)
        pi[key] = bags

    return pi

def count_bags(clr = 'shiny gold'):
    for bag in pi:
        if clr in pi[bag]:
            bag_set.add(bag)
            count_bags(bag)

def count_bags_s(clr = 'shiny gold'):
    cnt = 1
    for bag in pi[clr]:
        cnt += pi[clr][bag] * count_bags_s(bag)

    return cnt

bag_set = set()
# pi = read_puzzle_input(True)
pi = read_puzzle_input()
count_bags()
print(len(bag_set))

print(count_bags_s() - 1)
