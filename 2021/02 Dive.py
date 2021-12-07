DAY = "02"
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[ list[str, int] ]:
    result = []
    with open('.data/' + fname, encoding='utf8') as fh:
        txt = fh.read()
        lines = txt.split('\n')

    for line in lines:
        elems = line.split(' ')
        result.append([ elems[0], int(elems[1]) ])

    # print(result)

    return result

def part_i(input: list[ list[str, int] ]):
    x, y = 0, 0
    for elem in input:
        if elem[0] == 'forward':
            x += elem[1]
        elif elem[0] == 'down':
            y += elem[1]
        elif elem[0] == 'up':
            y -= elem[1]
    print(x * y)


def part_ii(input: list[ list[str, int] ]):
    aim_x, aim_y = 0, 0
    sub_x, sub_y = 0, 0

    for elem in input:
        if elem[0] == 'forward':
            sub_x += elem[1]
            sub_y += aim_y * elem[1]
        elif elem[0] == 'down':
            aim_y += elem[1]
        elif elem[0] == 'up':
            aim_y -= elem[1]


    print(sub_x * sub_y)
  


input_data = read_puzzle_input(DATA_FILENAME)
part_i(input_data)
part_ii(input_data)
