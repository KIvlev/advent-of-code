def read_puzzle_input(fname: str) -> list[int]:

    result = []
    with open('.data/' + fname, encoding='utf8') as fh:
        txt = fh.read()
        lines = txt.split('\n')

    for line in lines:
        result.append(int(line))

    return result

def part_i(input: str):
    cnt = 0
    for i in range(len(input)-1):
        if input[i+1] > input[i]:
            cnt += 1
    print(cnt)

def part_ii(input: str):
    cnt = 0
    for i in range(len(input)-3):
        msr_i = input[i] + input[i+1] + input[i+2]
        msr_ii = input[i+1] + input[i+2] + input[i+3]
        if msr_ii > msr_i:
            cnt += 1

    print(cnt)


DAY = "01"
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
