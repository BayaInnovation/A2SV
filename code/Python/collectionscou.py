from collections import Counter
a = input()
b = Counter(map(int,input().split()))
c = input()
d = int(c) 
earnings = 0
for customer in range(d):
    size, x_i = map(int,input().split())
    if size in b and b[size] > 0:
        b[size] -= 1
        earnings += x_i
            
print(earnings)
