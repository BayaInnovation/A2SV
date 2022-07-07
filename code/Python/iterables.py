from itertools import combinations

x = int(input())
z = input().split()
y = int(input())

comb_list = list(combinations(z, y))
a_list = [e for e in comb_list if 'a' in e]
print(len(a_list) / len(comb_list))