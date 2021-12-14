from collections import Counter

DAY = "14"
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    polymer, lines = txt.split('\n\n')
    
    rules = {}
    for line in lines.split('\n'):
        f, s = line.split(' -> ')
        rules[f] = s

    return polymer, rules

def produce(ps, rules, iters):
    polymer = Counter()

    for i0 in range(len(ps) - 1):
        polymer[ps[i0:i0+2]] += 1
    
    for iter in range(iters):
        polymer_next = Counter()
        for plm in polymer:
            m = rules[plm]
            polymer_next[plm[0] + m] += polymer[plm]
            polymer_next[m + plm[1]] += polymer[plm]

        polymer = polymer_next

    stats = Counter()
    for k, m in polymer.items():
        stats[k[0]] += m
        stats[k[1]] += m
    stats[ps[0]] += 1
    stats[ps[-1]] += 1

    print((max(stats.values()) - min(stats.values())) // 2)

polymer, rules = read_puzzle_input(DATA_FILENAME)

produce(polymer, rules, 10)
produce(polymer, rules, 40)