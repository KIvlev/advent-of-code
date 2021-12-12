DAY = "12"
TEST_FILENAME = 'test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    lines = txt.split('\n')

    caves = {}
    for line in lines:
        line = line.replace('start', 'Start').replace('end', 'End')
        cave_in, cave_out = line.split('-')
        if cave_in not in caves:
            caves[cave_in] = []
        if cave_out not in caves:
            caves[cave_out] = []

        if cave_in != 'End' and cave_out != 'Start':
            caves[cave_in].append(cave_out)

        if cave_out != 'End' and cave_in != 'Start':
            if cave_in not in caves[cave_out] and cave_in != 'Start':
                caves[cave_out].append(cave_in)

    return caves

def walk_i(point, caves, visited, path, paths):
    path.append(point)
    
    if point == 'End':
        paths.append(path)
        return

    if point.islower():
        visited.add(point)

    for next in caves[point]:
        if next.islower() and next in visited:
            continue
        else:
            walk_i(next, caves, visited.copy(), path.copy(), paths)

def part_i(caves: list[str]):
    paths = []
    walk_i('Start', caves, set(), [], paths)
    print(len(paths))

def walk_ii(point, caves, visited, path, paths):
    path.append(point)
    
    if point == 'End':
        paths.append(path)
        return

    if point.islower():
        visited[point] -= 1

    for next in caves[point]:
        if next in visited and visited[next] == 0:
            continue
        else:
            walk_ii(next, caves, visited.copy(), path.copy(), paths)


def part_ii(caves: list[str]):
    paths = []
    all_paths = set()
    small_caves = {}
    for cave in caves:
        if cave.islower():
            small_caves[cave] = 1
    for cave in small_caves:
        to_visit = small_caves.copy()
        to_visit[cave] = 2
        walk_ii('Start', caves, to_visit, [], paths)
        for path in paths:
            all_paths.add(','.join(path))

    print(len(all_paths))

input_data = read_puzzle_input(DATA_FILENAME)

part_i(input_data)
part_ii(input_data)
