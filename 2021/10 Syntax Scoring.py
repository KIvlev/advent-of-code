DAY = "10"
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    lines = txt.split('\n')

    return lines

def part_i(input: list[str]):
    incomplete_lines = []
    illegal = {')': 3, ']': 57, '}': 1197,'>': 25137}
    sum = 0
    for line in input:
        found = True
        while found:
            found = False
            if '()' in line:
                found = True
                line = line.replace('()', '')
            if '[]' in line:
                found = True
                line = line.replace('[]', '')
            if '{}' in line:
                found = True
                line = line.replace('{}', '')
            if '<>' in line:
                found = True
                line = line.replace('<>', '')
        incomplete_flag = True
        for symbol in line:
            if symbol in ')]}>':
                sum += illegal[symbol]
                incomplete_flag = False
                break
        if incomplete_flag:
            incomplete_lines.append(line)
    
    print(sum)
    return incomplete_lines

def part_ii(input: list[str]):
    closing = {'(': 1, '[': 2, '{': 3,'<': 4}
    score = []
    for line in input:
        sum = 0
        for symbol in line[::-1]:
            sum *= 5
            sum += closing[symbol]
        score.append(sum)
    score.sort()
    print(score[int(len(score) / 2)])

input_data = read_puzzle_input(DATA_FILENAME)

part_ii(part_i(input_data))
