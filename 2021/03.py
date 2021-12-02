from os import path
from typing import Counter

def read_puzzle_input(fname: str) -> list[int]:

    result = []
    with open('data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
        lines = txt.split('\n')

    for line in lines:
        result.append(int(line))

    return result

def part_i(input: str):
    pass

def part_ii(input: str):
    pass


DAY = "03"
TEST = DAY + '.test.txt'
INPUT = DAY + '.input.txt'

TEST_FILENAME = DAY + '.test.txt'
DATA_FILENAME = DAY + '.input.txt'

test_data = read_puzzle_input(TEST_FILENAME)
input_data = read_puzzle_input(DATA_FILENAME)

print('Part I')
part_i(test_data)
part_i(input_data)

print('\nPart II')
part_ii(test_data)
part_ii(input_data)
