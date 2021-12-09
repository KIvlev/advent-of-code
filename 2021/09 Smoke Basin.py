DAY = "09"
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    lines = txt.split('\n')

    return lines


def part_i(input : list[str]):
    heightmap = []

    size_x = len(input[0])
    size_y = len(input)
    
    heightmap.append('@' * (size_x + 2))
    for line in input:
        heightmap.append('@' + line + '@')
    heightmap.append('@' * (size_x + 2))

    sum = 0
    for y in range(1, size_y + 1):
        for x in range(1, size_x + 1):
            if heightmap[y][x] < heightmap[y-1][x] and \
                    heightmap[y][x] < heightmap[y+1][x] and \
                    heightmap[y][x] < heightmap[y][x-1] and \
                    heightmap[y][x] < heightmap[y][x+1]:
                sum += int(heightmap[y][x])+1
    print(sum)

def make_step(x ,y, heightmap, checked, basin):
    route = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    
    if f'{x}.{y}' in checked:
        return
    
    checked.add(f'{x}.{y}')
    if heightmap[y][x] == '9':
        return

    basin.add(f'{x}.{y}')
    for step in route:
        make_step(x + step[0], y + step[1], heightmap, checked, basin)

def part_ii(input: list[str]):
    heightmap = []
    size_x = len(input[0])
    size_y = len(input)
    
    heightmap.append('9' * (size_x + 2))
    for line in input:
        heightmap.append('9' + line + '9')
    heightmap.append('9' * (size_x + 2))

    checked = set()
    basins = []
    basin_size = []
    for y in range(1, size_y + 1):
        for x in range(1, size_x + 1):
            if f'{x}.{y}' not in checked:
                basin = set()
                make_step(x, y, heightmap, checked, basin)
                if len(basin) != 0:
                    basins.append(basin)
                    basin_size.append(len(basin))
    
    basin_size.sort(reverse=True)
    print(basin_size[0] * basin_size[1] * basin_size[2])


input_data = read_puzzle_input(DATA_FILENAME)

part_i(input_data)
part_ii(input_data)
