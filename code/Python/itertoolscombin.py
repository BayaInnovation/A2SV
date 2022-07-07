from itertools import combinations

p = input().split()
w = p[0]
d = int(p[1])
for i in range(1,d+1):
    for j in combinations(sorted(w),i):
        print("".join(j))
