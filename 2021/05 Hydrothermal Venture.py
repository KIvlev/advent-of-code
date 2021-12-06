from os import path
from typing import Counter


DAY = "05"
TEST = DAY + '.test.txt'
INPUT = DAY + '.input.txt'

TEST_FILENAME = DAY + '.test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[list[int]]:
    result = []
    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
        lines = txt.split('\n')
    
    for line in lines:
        p1, p2 = line.split(' -> ')
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        result.append([int(x1), int(y1), int(x2), int(y2)])

    return result

def part_i(input: list[list[int]]):
    points = {}
    for line in input:
        
        if (line[0] == line[2]):
            y = min(line[1], line[3])
            span = abs(line[1] - line[3]) + 1

            for i0 in range(y, y + span):
                point = str(line[0]) + '.' + str(i0)
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

        elif (line[1] == line[3]):
            x = min(line[0], line[2])
            span = abs(line[0] - line[2]) + 1

            for i0 in range(x, x + span):
                point = str(i0) + '.' + str(line[1])
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

    cnt = 0
    for p in points:
        if points[p] > 1:
            cnt += 1
    print(cnt)

def part_ii(input: list[str]):
    points = {}
    for line in input:

        if (line[0] == line[2]):
            x = line[0]
            y1 = line[1]
            if line[1] < line[3]:
                step_y = 1
                y2 = line[3] + 1
            else:
                step_y = -1
                y2 = line[3] - 1

            for i0 in range(y1, y2, step_y):
                point = f'{x}.{i0}'
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

        elif (line[1] == line[3]):
            y = line[1]
            x1 = line[0]
            if line[0] < line[2]:
                x2 = line[2] + 1
                step_x = 1
            else:
                x2 = line[2] - 1
                step_x = -1

            for i0 in range(x1, x2, step_x):
                point = str(i0) + '.' + str(line[1])
                point = f'{i0}.{y}'
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

        else:
            x1 = line[0]
            if line[0] < line[2]:
                x2 = line[2] + 1
                step_x = 1
            else:
                x2 = line[2] - 1
                step_x = -1

            y1 = line[1]
            if line[1] < line[3]:
                step_y = 1
                y2 = line[3] + 1
            else:
                step_y = -1
                y2 = line[3] - 1
            
            while x1 != x2:
                point = f'{x1}.{y1}'
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1
                x1 += step_x
                y1 += step_y
    cnt = 0
    for p in points:
        if points[p] > 1:
            cnt += 1
    print(cnt)

test_data = read_puzzle_input(TEST_FILENAME)
input_data = read_puzzle_input(DATA_FILENAME)

part_i(input_data)
part_ii(input_data)
