from itertools import *

a = input()
for i,j in groupby(map(int,list(a))):
    print(tuple([len(list(j)), i]) ,end = " ")
