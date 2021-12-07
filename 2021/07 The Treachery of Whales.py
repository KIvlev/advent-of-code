def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    
    positions = [int(x) for x in txt.split(',')]

    return positions

def part_i(positions: list[int]):
    min_position = 0
    min_fuel = -1
    for i0 in range(min(positions), max(positions)):
        fuel = 0
        for p in positions:
            fuel += abs(i0 - p)
        if min_fuel == -1:
            min_fuel = fuel
        elif fuel < min_fuel:
            min_fuel = fuel
            min_position = i0
        
    print(min_fuel)
        
def part_ii(positions: list[int]):
    min_position = 0
    min_fuel_sum = -1
    for i0 in range(min(positions), max(positions)):
        fuel_sum = 0
        for p in positions:
            distance = max(p, i0) - min(p, i0) + 1
            fuel_sum += (distance - 1) * distance / 2
        if min_fuel_sum == -1:
            min_fuel_sum = fuel_sum
        elif fuel_sum < min_fuel_sum:
            min_fuel_sum = fuel_sum
            min_position = i0

        
    print(round(min_fuel_sum))

DAY = "07"
DATA_FILENAME = DAY + '.input.txt'

input_data = read_puzzle_input(DATA_FILENAME)

part_i(input_data)
part_ii(input_data)
