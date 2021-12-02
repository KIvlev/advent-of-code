# -*- coding: UTF8 -*-

from os import path


def read_puzzle_input(fname):

    file = open(fname, 'r', encoding='utf8')

    cnt = 0
    for txt in file:
        lines = txt.rstrip('\n')

    return lines


DAY = "01"
TEST = DAY + '.test.txt'
INPUT = DAY + '.input.txt'

