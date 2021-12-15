import heapq


DAY = "15"
TEST_FILENAME = 'test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[list[int]]:

    with open('.data/'+fname, encoding='utf8') as fh:
        lines = fh.read().split('\n')

    risks = [list(map(int, line)) for line in lines]
        
    return risks

def part_i(risks: list[list[int]]):
    size_y = len(risks) - 1
    size_x = len(risks[size_y]) - 1
    visited = set()
        
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    paths = [(0, 0, 0)]

    while True:
        risk, x, y = heapq.heappop(paths)

        if (x, y) in visited:
            continue

        if (x, y) == (size_x, size_y):
            print(risk)
            break

        visited.add((x, y))

        for sx, sy in steps:
            nx = x + sx
            ny = y + sy
            if 0 > nx or nx > size_x or 0 > ny or ny > size_y:
                continue
            if (nx, ny) in visited:
                continue
            heapq.heappush(paths, (risk + risks[ny][nx], nx, ny))

def mod_9(value: int) -> int:
    return (value - 1) % 9 + 1

def part_ii(risks: list[list[int]]) -> list[list[int]]:
    size_y = len(risks)
    size_x = len(risks[size_y - 1])

    new_risks = []
    incrs = list(range(5))
    for i0 in range(size_y):
        new_risks.append([mod_9(incr + risk) \
                for incr in incrs for risk in risks[i0]])
    
    for i0 in range(1, 5):
        for i1 in range(size_y):
            risk_row = []
            for i2 in range(size_x * 5):
                risk_row.append(mod_9(new_risks[i1][i2] + i0))
            new_risks.append(risk_row)

    return new_risks

input_data = read_puzzle_input(DATA_FILENAME)

part_i(input_data)
part_i(part_ii(input_data))
