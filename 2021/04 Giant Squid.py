DAY = "04"
DATA_FILENAME = DAY + '.input.txt'


def unpack_line(line: str) -> list[int]: 
    line = line.strip().replace('  ', ' ')
    result = [int(x) for x in line.split(' ')]
    return result

def read_puzzle_input(fname: str):

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
        lines = txt.split('\n')

    # number_seq = lines[0].split(',')

    number_seq = [int(x) for x in lines[0].split(",")]
    lines.pop(0)
    array_size = int(len(lines) / 6)
    boards = []
    # list_of_arrays = []
    for i0 in range(array_size):
        board = []
        line_list = []
        line_list.append(unpack_line(lines[i0*6+1]))
        line_list.append(unpack_line(lines[i0*6+2]))
        line_list.append(unpack_line(lines[i0*6+3]))
        line_list.append(unpack_line(lines[i0*6+4]))
        line_list.append(unpack_line(lines[i0*6+5]))

        # square
        for line in line_list:
            board.append(set(line))
    
        # list_of_arrays.append(line_list)

        for i1 in range(5):
            column = set()
            for i2 in range(5):
                column.add(line_list[i2][i1])
        
            board.append(set(column))

        boards.append(board)        

    # for line 
    return number_seq, boards

def part_i():
    number_seq, boards = read_puzzle_input(DATA_FILENAME)
    for num in number_seq:
        for board in boards:
            for line in board:
                if num in line:
                    line.remove(num)
                if len(line) == 0:
                    elems = set()
                    for b in board:
                        elems = elems.union(b)
                    if num in elems:
                        elems.remove(num)
                    rest_sum = sum(elems)

                    print(num * rest_sum)

                    return

def part_ii():
    number_seq, boards = read_puzzle_input(DATA_FILENAME)
    win_boards = []
    for num in number_seq:
        for i0 in range(len(boards)):
            board = boards[i0]
            if i0 in win_boards:
                continue

            flag = True
            for line in board:
                if num in line:
                    line.remove(num)
                if len(line) == 0:
                    flag = False
            
            if flag:
                continue

            win_boards.append(i0)

            if len(boards) ==  len(win_boards):
                for i1 in range(len(boards)):
                    if i1 in win_boards:
                        continue
                elems = set()
                for b in boards[i0]:
                    elems = elems.union(b)
                elems.discard(num)
                rest_sum = sum(elems)
                print(num * rest_sum)

part_i()
part_ii()
