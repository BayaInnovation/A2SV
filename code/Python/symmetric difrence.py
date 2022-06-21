# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
stud1 = set(list(map(int, input().split())))
n = int(input())
set2 = set(list(map(int, input().split())))
#print (stud1)
#print (set2)

n1 = stud1.difference(set2)
n2 = set2.difference(stud1)
L = [str(x) for x in n1] + [str(x) for x in n2]
L.sort(key = int)
#print (L)
print ('\n'.join(L))