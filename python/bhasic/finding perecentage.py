if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
for myvalue, value in student_marks.items():
        if query_name == myvalue:
            sum = 0
            count = 0
            for i in value:
                sum += i
                count += 1
            average = sum/count
            print("{:.2f}".format(average))
