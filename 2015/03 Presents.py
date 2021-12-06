def read_input() -> list(list()):
    with open('.data/03.input.txt', encoding='utf8') as fh:
        txt = fh.read()
    mapping = {'>': [1, 0], '<': [-1, 0], '^': [0, 1], 'v': [0, -1]}
    result = []
    for sym in txt:
        result.append(mapping[sym])
    # print(result)
    return (result)


def part_i(way: list(list())):
    visited = {}
    position = [0, 0]
    for p in way:
        pos_key = str(position[0]) + '.' + str(position[1])
        if pos_key not in visited:
            visited[pos_key] = 1
        else:
            visited[pos_key] += 1
        position[0] += p[0]
        position[1] += p[1]
    
    print(len(visited))

def part_ii(way: list(list())):
    visited = {}
    pos_s = [0, 0]
    pos_r = [0, 0]
    santa_flag = True
    for p in way:
        if santa_flag:
            pos_key = str(pos_s[0]) + '.' + str(pos_s[1])
            if pos_key not in visited:
                visited[pos_key] = 1
            else:
                visited[pos_key] += 1
            pos_s[0] += p[0]
            pos_s[1] += p[1]
        else:
            pos_key = str(pos_r[0]) + '.' + str(pos_r[1])
            if pos_key not in visited:
                visited[pos_key] = 1
            else:
                visited[pos_key] += 1
            pos_r[0] += p[0]
            pos_r[1] += p[1]
        santa_flag = not santa_flag
    print(len(visited))


way = read_input()

part_i(way)
part_ii(way)
