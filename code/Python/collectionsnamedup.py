
import collections

st = int(input())
scol = ','.join(input().split())
Student = collections.namedtuple('Student',scol)

sum = 0
for i in range(st):
    row = input().split()
    student = Student(*row)
    sum += int(student.MARKS)

print(sum/st)
