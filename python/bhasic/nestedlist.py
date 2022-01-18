if __name__ == '__main__':
    d = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        d.append([score,name])
    d.sort()
    a = []
    for marks in d:
        if marks[0] != d[0][0]:
            a.append(marks)
    for marks in a:
        if marks[0] == a[0][0]:
            print(marks[1])
