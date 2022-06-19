if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, float(score)])
    first = []
    set1 = set()
    for i in range(len(records)):
        first.append(records[i][1])
    for i in range(len(first)):
        set1.add(first[i])
    sorted_set = sorted(set1)
    sec_min = list(sorted_set)[1]
    second = []
    for i in range(len(records)):
        if records[i][1] == sec_min:
            second.append(records[i][0])
    second.sort()
    for i in range(len(second)):
        print(second[i])
        