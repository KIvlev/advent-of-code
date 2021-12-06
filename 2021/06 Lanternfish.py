from os import path
from typing import Counter, Sequence
import collections

DAY = "06"
TEST = DAY + '.test.txt'
INPUT = DAY + '.input.txt'

TEST_FILENAME = DAY + '.test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[int]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
        lines = txt.split(',')
    result = []
    for line in lines:
        result.append(int(line))
    return result

def part_i(input: list[int]):
    swarm = input.copy()
    for i0 in range(80):
        for i1 in range(len(swarm)):
            if swarm[i1] == 0:
                swarm[i1] = 6
                swarm.append(8)
            else:
                swarm[i1] -= 1
    print(len(swarm))

def part_ii(input: list[int]):
    swarm = []
    for i0 in range(9):
        swarm.append(0)
    for f in input:
        swarm[f] += 1
    
    for i0 in range(256):
        to_born = swarm[0]
        for i1 in range(8):
            swarm[i1] = swarm[i1+1]
        swarm[6] += to_born
        swarm[8] = to_born

    print(sum(swarm))
    
test_data = read_puzzle_input(TEST_FILENAME)
input_data = read_puzzle_input(DATA_FILENAME)

part_i(input_data)
part_ii(input_data)
