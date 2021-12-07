DAY = "06"
TEST = DAY + '.test.txt'
INPUT = DAY + '.input.txt'

TEST_FILENAME = DAY + '.test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[int]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    
    elems = txt.split(',')
    result = [0 for i in range(9)]
    for line in elems:
        result[int(line)] += 1
    
    return result

def count_fish(swarm: list[int], steps: int):
    for i0 in range(steps):
        to_born = swarm[0]
        for i1 in range(8):
            swarm[i1] = swarm[i1+1]
        swarm[6] += to_born
        swarm[8] = to_born

    print(sum(swarm))
    
input_data = read_puzzle_input(DATA_FILENAME)
count_fish(input_data.copy(), 80)
count_fish(input_data, 256)
