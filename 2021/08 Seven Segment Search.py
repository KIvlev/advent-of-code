DAY = "08"
TEST = DAY + '.test.txt'
INPUT = DAY + '.input.txt'

TEST_FILENAME = DAY + '.test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[list[str], list[str]]:

    with open('.data/'+fname, encoding='utf8') as fh:
        lines = fh.read().split('\n')
    
    result = []
    for l in lines:
        input, output = l.split(' | ')

        result.append([
                [''.join(sorted(c)) for c in input.split(' ')],
                [''.join(sorted(c)) for c in output.split(' ')]
                ])
        
    return result


def part_i(patterns: list[list[str], list[str]]):
    mapping1478 = {2: 1, 3: 7, 4: 4, 7: 8}
    cnt = 0
    for pattern in patterns:
        # print(pattern[0])
        # print(pattern[1])
        for p in pattern[1]:
            # 1, 7, 4, 8
            if len(p) in mapping1478:
                cnt += 1
                # print('   ', p, mapping1478[len(p)])
    print(cnt)


def identify(input: list[str]) -> dict[str]:
    res = {}
    to_identify =  {input[i]: 
                        {
                        'els': set(input[i]),
                        'size': len(input[i]), 
                        'val': -1
                        }
                    
            for i in range(10)}

    patterns = {i: '' for i in range(10)}
    alphabet = {}

    for elem in to_identify:
        if (len(elem)) == 2:
            to_identify[elem]['val'] = 1
            res[elem] = 1
            patterns[1] = elem
        elif (len(elem)) == 3:
            to_identify[elem]['val'] = 7
            res[elem] = 7
            patterns[7] = elem
        elif (len(elem)) == 4:
            to_identify[elem]['val'] = 4
            res[elem] = 4
            patterns[4] = elem
        elif (len(elem)) == 7:
            to_identify[elem]['val'] = 8
            res[elem] = 8
            patterns[8] = elem

    # a
    alphabet['a'] = set(patterns[7]).difference(set(patterns[1]))
    for elem in to_identify:
        to_identify[elem]['els'].difference_update(alphabet['a'])

    # g
    alphabet['g'] = {}
    for elem in input:
        if len(elem) in [5, 6]:
            if alphabet['g'] == {}:
                alphabet['g'] = set(elem)
            else:
                alphabet['g'] = alphabet['g'].intersection(set(elem))
    alphabet['g'] = alphabet['g'].difference(alphabet['a'])
    for elem in to_identify:
        to_identify[elem]['els'].difference_update(alphabet['g'])

    # e
    letter_d = {}
    for elem in input:
        if len(elem) in [5, 6]:
            for letter in alphabet:
                elem = elem.replace(''.join(alphabet[letter]), '')
            for el in elem:
                if el not in letter_d:
                    letter_d[el] = 1
                else:
                    letter_d[el] += 1
    for elem in letter_d:
        if letter_d[elem] == 3:
            alphabet['e'] = set(elem)
    for elem in to_identify:
        to_identify[elem]['els'].difference_update(alphabet['e'])

    # c
    for elem in to_identify:
        if to_identify[elem]['size'] == 5 \
                and len(to_identify[elem]['els']) == 2:
            for el_2 in to_identify:
                if to_identify[el_2]['size'] == 2:
                    alphabet['c'] = \
                        to_identify[elem]['els'].intersection(to_identify[el_2]['els'])
    for elem in to_identify:
        to_identify[elem]['els'].difference_update(alphabet['c'])

    # f
    for elem in to_identify:
        if to_identify[elem]['size'] == 2:
            alphabet['f'] = to_identify[elem]['els'].copy()
    for elem in to_identify:
        to_identify[elem]['els'].difference_update(alphabet['f'])

    # d
    for elem in to_identify:
        if to_identify[elem]['size'] == 5 \
                and len(to_identify[elem]['els']) == 1:
            alphabet['d'] = to_identify[elem]['els'].copy()

        if to_identify[elem]['size'] == 6 \
                and len(to_identify[elem]['els']) == 1:
            alphabet['b'] = to_identify[elem]['els'].copy()



    # print('*'*20)
    # for elem in to_identify:
    #     print(elem, to_identify[elem])

    # print('')
    # print(alphabet)
    # print('')
    # print(patterns)
    
    result = {}
    for letter in alphabet:
        result[''.join(alphabet[letter])] = letter
    return result

def convert(pattern, alphabet):
    patterns = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, \
                'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9
        }

    res = ''
    for el in pattern:
        res += alphabet[el]
        
    res = ''.join(sorted(res))

    return patterns[res]

def part_ii(patterns: list[list[str], list[str]]):
    sum = 0
    for pattern in patterns:
        alphabet = identify(pattern[0])
        res = 0
        for i0 in range(4):
            res += pow(10, 3-i0) * convert(pattern[1][i0], alphabet)
        sum += res
    print(sum)





test_data = read_puzzle_input(TEST_FILENAME)
input_data = read_puzzle_input(DATA_FILENAME)

# print('Part I')
# part_i(test_data)
# part_i(input_data)

print('\nPart II')
# part_ii(test_data)
part_ii(input_data)
