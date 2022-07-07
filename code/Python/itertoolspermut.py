from itertools import permutations

a,e = input().split()

words = list(permutations(a,int(e)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')
