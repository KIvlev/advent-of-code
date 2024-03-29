﻿with open('.data/17.txt', encoding='utf8') as fh:
    FX, TX, FY, TY = list(map(int, fh.read().replace('target area: x=', '')\
                .replace(' y=', '').replace('..', ',').split(',')))

AREA = set([(x, y) for x in range(FX, TX + 1) for y in range(FY , TY + 1)])

def probe (vx, vy):
    my = 0
    coords = (0, 0)
    while coords[1] >= FY:
        coords = (coords[0] + vx,  coords[1] + vy)
        my = max(my, coords[1])
        vx = max(0, vx -1)
        vy -= 1
        if coords in AREA:
            return my
        
    return None

def run_probes():
    probs = []

    for vx in range(1, TX + 1):
        for vy in range(FY-1, -FY+1):
            res = probe(vx, vy)
            if res != None:
                probs.append((res, vx, vy))

    probs.sort(reverse=True)
    print(probs[0][0])
    print(len(probs))

run_probes()
