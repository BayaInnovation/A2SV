st, sub = map(int, input().split())
lst = []
for i in range(sub):
    lst.append(map(float, input().split())) 
for j in zip(*lst):
    print(sum(j) / len(j))