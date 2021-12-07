DAY = "01"
DATA_FILENAME = DAY + '.input.txt'


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

input_data = read_puzzle_input(DATA_FILENAME)
part_i(input_data)
part_ii(input_data)
