# -*- coding: UTF8 -*-


def read_puzzle_input(test = False):

    if test: 
        fig = 939
        line = '7,13,x,x,59,x,31,19'
    else:
        fig = 1000655
        line = '17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,401,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19'

    res = []
    lines = line.replace('x', '0').split(',')
    for l in lines:
        res.append(int(l))

    return fig, res

def part_i():
    # est, sched = read_puzzle_input(True)
    est, sched = read_puzzle_input()
    
    ttw = 1000
    bus_id = 0
    for bus in sched:
        if bus == 0:
            continue
        if bus - est % bus < ttw:
            ttw = bus - est % bus
            bus_id = bus
    print(bus_id * ttw)

def part_ii(line):

    sched = {}
    lines = line.split(',')
    offset = 0
    for l in lines:
        if l != 'x':
            sched[int(l)] = -offset % int(l)
        offset += 1

    values = list(reversed(sorted(sched)))
    vl = sched[values[0]]
    rs = values[0]
    for el in values[1:]:
        while sched[el] != vl % el:
            vl += rs
        rs *= el
    print(vl)

# line = '7,13,x,x,59,x,31,19'
line = '17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,401,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19'

part_i()
part_ii(line)


# calc_i()
# calc_ii(line)
