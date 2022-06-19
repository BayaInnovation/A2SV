if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sonuc = 0
    aver = float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        sonuc += i
    aver = sonuc / len(student_marks[query_name])
    print("%.2f" %aver)