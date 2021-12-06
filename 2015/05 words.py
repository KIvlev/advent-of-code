def read_puzzle_input() -> list[str]:

    with open('.data/05.input.txt', encoding='utf8') as fh:
        txt = fh.read()
    
    lines = txt.split('\n')

    return lines

def part_i(lines: list[str]):
    naughty = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'
    cnt = 0
    for line in lines:

        naughty_flag = False
        for n in naughty:
            if n in line:
                naughty_flag = True
                break
        if naughty_flag:
            continue

        vowel_cnt = 0
        for sym in line:
            if sym in vowels:
                vowel_cnt += 1
        if vowel_cnt < 3:
            continue

        for i0 in range(len(line) - 1):
            if line[i0] == line[i0 + 1]:
                cnt += 1
                break
        
    print(cnt)

def part_Ii(lines: list[str]):
    cnt = 0
    for line in lines:
        triple_flag = False
        for i0 in range(1, len(line) - 1):
            if line[i0 - 1] == line[i0 + 1]:
                triple_flag = True
                break
        
        if not triple_flag:
            continue

        pair = ''
        for i0 in range(len(line) - 1):
            pair = line[i0] + line[i0 + 1]
            if pair in line[i0 + 2:]:
                cnt += 1
                break

    print(cnt)


lines = read_puzzle_input()
part_i(lines)
part_Ii(lines)
