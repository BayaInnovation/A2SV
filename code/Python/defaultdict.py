from collections import defaultdict

x, y = map(int,input().split())

a = defaultdict(list)
for i in range(1, x + 1):
    a[input()].append(i)

for i in range(1, y + 1):
    key = input()
    if len(a[key]) > 0:
        print(" ".join(str(c) for c in a[key]))
    else:
        print(-1)