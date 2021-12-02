# -*- coding: UTF8 -*-
import string

def read_puzzle_input(test = False):

    if test: 
        fname = 'test.txt'
    else:
        fname = '.data/04 Passport Processing.txt'

    puzzle_input = []

    file = open(fname, 'r', encoding='utf8')

    pass_d = {}
    for line in file:
        line = line.rstrip('\n')

        if line != '':
            line_l = line.split(' ')
            for ln in line_l:
                key, value = ln.split(':')
                pass_d[key] = value
        else:
            puzzle_input.append(pass_d)
            pass_d = {}

    if pass_d != {}:
        puzzle_input.append(pass_d)

    return puzzle_input

def count_valid(pi):
    # required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    cnt = 0
    for p in pi:
        if len(p) == 8: 
            cnt += 1
        elif len(p) == 7:
            if 'cid' not in p:
                cnt += 1

    print(cnt)

def count_valid_ii(pi):
    cnt = 0
    for p in pi:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if 'byr' not in p: continue
        if int(p['byr']) not in range(1920, 2003): continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if 'iyr' not in p: continue
        if int(p['iyr']) not in range(2010, 2021): continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if 'eyr' not in p: continue
        if int(p['eyr']) not in range(2020, 2031): continue

        # hgt (Height) - a number followed by either cm or in:
        #     If cm, the number must be at least 150 and at most 193.
        #     If in, the number must be at least 59 and at most 76.
        if 'hgt' not in p: continue
        if p['hgt'][-2:] not in ('cm','in'): continue

        if p['hgt'][-2:] == 'cm':
            if int(p['hgt'][:-2]) not in range(150, 194): continue

        if p['hgt'][-2:] == 'in':
            if int(p['hgt'][:-2]) not in range(59, 77): continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if 'hcl' not in p: continue
        if p['hcl'][0:1] != '#': continue
        try:
            int(p['hcl'][1:], 16)
        except:
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if 'ecl' not in p: continue
        if p['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if 'pid' not in p: continue
        if len(p['pid']) != 9: continue
        try:
            int(p['pid'])
        except:
            continue

        # cid (Country ID) - ignored, missing or not.

        cnt += 1

    print(cnt)

# pi = read_puzzle_input(True)
pi = read_puzzle_input()

count_valid(pi)
count_valid_ii(pi)