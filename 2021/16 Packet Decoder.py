import math
from typing import Match


DAY = "16"
TEST_FILENAME = 'test.txt'
DATA_FILENAME = DAY + '.input.txt'

def read_puzzle_input(fname: str) -> list[str]:

    with open('.data/'+fname, encoding='utf8') as fh:
        txt = fh.read()
    
    transmission = [format(int(x, 16), '#06b')[2:] for x in txt]
    
    return ''.join(transmission)

operation = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    4: '',
    5: lambda s: s[0] > s [1],
    6: lambda s: s[0] < s [1],
    7: lambda s: s[0] == s [1],
}

def read_pkg(trs: str):
    vrs = int(trs[:3],2)
    tp = int(trs[3:6],2)
    trs = trs[6:]

    if tp == 4:
        lp = ''
        while True:
            lp += trs[1:5]
            if trs[0] == '0':
                return vrs, int(lp, 2), trs[5:]
            trs = trs[5:]

    sps = []
    if trs[0] == '0':
        trs = trs[1:]
        l = int(trs[:15], 2)
        sp = trs[15: 15 + l]
        trs = trs[15 + l:]
        while sp:
            svrs, vl, sp = read_pkg(sp)
            sps.append(vl)
            vrs += svrs
    else:
        trs = trs[1:]
        cnt = int(trs[:11] ,2)
        trs = trs[11:]
        for i0 in range(cnt):
            svrs, vl, trs = read_pkg(trs)
            sps.append(vl)
            vrs += svrs

    return vrs, operation[tp](sps), trs


input_data = read_puzzle_input(DATA_FILENAME)

vrs, sps, trs = read_pkg(input_data)
print(vrs)
print(sps)
