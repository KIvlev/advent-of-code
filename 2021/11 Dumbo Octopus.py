DAY = "11"
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    lines = txt.split('\n')

    octopus = []
    for i0 in range(len(lines)):
        octopus.append([])
        for i1 in range(len(lines[0])):
            octopus[i0].append(int(lines[i0][i1]))
    
    return octopus

def part_i(octopus: list[str]):
    size = len(octopus)
    area = [[-1, -1], [-1, 0], [-1, 1], [0, -1],\
            [0, 1], [1, -1], [1, 0], [1, 1] ]
    sum = 0
    done = False
    i0 = 0
    while not done:
        flashing = True
        flashed = []

        for i1 in range(size):
            for i2 in range(size):
                octopus[i1][i2] += 1

        while flashing:
            flashing = False
            to_flash = []
            for i1 in range(size):
                for i2 in range(size):
                    if octopus[i1][i2] not in flashed:
                        if octopus[i1][i2] > 9:
                            octopus[i1][i2] = 0
                            to_flash.append([i1, i2])
                            flashing = True
            for oct in to_flash:
                for point in area:
                    to_check = [oct[0] + point[0], oct[1] + point[1]]
                    if to_check[0] in range(size) \
                            and to_check[1] in range(size) \
                            and to_check not in to_flash \
                            and to_check not in flashed:
                        octopus[to_check[0]][ to_check[1]] += 1
                flashed.append(oct)

        if i0 == 100:
            print(sum)

        sum += len(flashed)

        i0 += 1
        if (len(flashed) == 100):
            print(i0)
            done = True

        
input_data = read_puzzle_input(DATA_FILENAME)

print('Part I')
part_i(input_data)
