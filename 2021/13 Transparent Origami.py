DAY = "13"
TEST_FILENAME = 'test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str):

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    lines = txt.split('\n')

    dots = []
    folds = []

    for line in lines:
        if line == '':
            continue
        elif 'fold along' in line:
            coord, value = line.replace('fold along ', '').split('=')
            folds.append([coord, int(value)])
        else:
            x,y = line.split(',')
            dots.append([int(x), int(y)])

    return dots, folds

def fold_paper(dots, fold):
    new_dots = []
    for dt in dots:
        if fold[0] == 'x':
            x = dt[0] if dt[0] < fold[1] else 2 * fold[1] - dt[0]
            y = dt[1]
        else:
            x = dt[0]
            y = dt[1] if dt[1] < fold[1] else 2 * fold[1] - dt[1]

        if [x, y] not in new_dots:
            new_dots.append([x, y])
        
    return new_dots

def part_i(dots, folds):
    for fold in folds:
        dots = fold_paper(dots, fold)
        print(f'folding: {fold[0]}:{fold[1]} -> {len(dots)} dots')
    
    size_x, size_y = 0, 0
    for d in dots:
        size_x = max(size_x, d[0])
        size_y = max(size_y, d[1])

    code = []
    for i0 in range(size_y + 1):
        code.append(' '*size_x)

    for d in dots:
        code[d[1]] = code[d[1]][:d[0]] + '#' + code[d[1]][d[0]+1:]

    print('')
    for c in code:
        print(c)

dots, folds = read_puzzle_input(DATA_FILENAME)

part_i(dots, folds)
