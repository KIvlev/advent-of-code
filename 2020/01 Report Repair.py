def read_puzzle_input():
    file = open('.data/01 Report Repair.txt', 'r', encoding='utf8')
    report = []
    for line in file:
        report.append(int(line.rstrip('\n')))
    return report

def find_2020_pair(report):
    for i1 in range(len(report)):
        for i2 in range(i1, len(report)):
            if report[i1] + report[i2] == 2020:
                print(report[i1] * report[i2])
                return

def find_2020_triple(report):
    for i1 in range(len(report)):
        for i2 in range(i1, len(report)):
            for i3 in range(i2, len(report)):
                if report[i1] + report[i2] + report[i3] == 2020:
                    print(report[i1] * report[i2]  * report[i3])
                    return

report = read_puzzle_input()

find_2020_pair(report)
find_2020_triple(report)
