DAY = "03"
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    
    lines = txt.split('\n')

    return lines

def part_i(input: list[str]):
    cnt0, cnt1 = [], []
    size = len(input[0])
    for i in range(size):
        cnt0.append(0)
        cnt1.append(0)

    for line in input:
        for i in range(len(input[0])):
            if line[i] == '0':
                cnt0[i] += 1
            else:
                cnt1[i] += 1

    gamma_s, gamma_r = '', ''
    for i in range(size):
        if cnt1[i] >= cnt0[i]:
            gamma_s += '1'
            gamma_r += '0'
        else:
            gamma_s += '0'
            gamma_r += '1'

    print(int(gamma_s, 2) * int(gamma_r,2))

def part_ii(input: list[str]):

    size = len(input[0])

    ox_list = input.copy()
    for i1 in range(size):
        cnt1, cnt0 = 0, 0
        ox1, ox0 = [], []
        for line in ox_list:
            if line[i1] == '1':
                cnt1 += 1
                ox1.append(line)
            else:
                cnt0 += 1
                ox0.append(line)

        if cnt1 >= cnt0:
            ox_list = ox1.copy()
        else:
            ox_list = ox0.copy()

        if len(ox_list) <= 1:
            break
    
    # CO2
    co_list = input.copy()
    for i1 in range(size):
        cnt0, cnt1 = 0, 0
        co0, co1 = [], []
        for line in co_list:
            if line[i1] == '0':
                cnt0 += 1
                co0.append(line)
            else:
                cnt1 += 1
                co1.append(line)

        if cnt0 <= cnt1:
            co_list = co0.copy()
        else:
            co_list = co1.copy()

        if len(co_list) <= 1:
            break
    
    print(int(ox_list[0], 2) * int(co_list[0], 2))


input_data = read_puzzle_input(DATA_FILENAME)
part_i(input_data)
part_ii(input_data)
